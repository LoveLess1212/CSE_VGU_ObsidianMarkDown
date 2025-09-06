```
use aiken/builtin
use aiken/crypto.{ScriptHash}
use aiken_design_patterns/merkelized_validator.{WithdrawRedeemer} as merkelized_validator
use aiken_design_patterns/utils.{sum_of_squares}
use cardano/address.{Credential}
use cardano/transaction.{OutputReference, Transaction}

// Definition of a custom validator for spending transactions
validator spending_example(stake_validator: ScriptHash) {
  spend(m_x: Option<Int>, y: Int, _own_ref: OutputReference, tx: Transaction) {
    expect Some(x) = m_x
    expect [sum] =
      [x, y]
        |> merkelized_validator.delegated_compute(
            stake_validator,
            builtin.un_i_data,
            builtin.un_i_data,
            tx.redeemers,
          )
    sum < 42
  }

  else(_) {
    fail
  }
}

// Definition of a custom validator for withdrawal transactions
validator logic_example {
  withdraw(
    redeemer: WithdrawRedeemer<Int, Int>,
    _own_credential: Credential,
    _tx: Transaction,
  ) {
    merkelized_validator.withdraw(sum_of_squares, redeemer)
  }

  else(_) {
    fail
  }
  ```
```
use aiken_design_patterns/multi_utxo_indexer as multi_utxo_indexer
use aiken_design_patterns/stake_validator as stake_validator
use aiken_design_patterns/utils.{authentic_input_is_reproduced_unchanged}
use cardano/address.{Address, Credential, Script}
use cardano/assets
use cardano/transaction.{Output, OutputReference, Transaction}

validator example(
  state_token_symbol: assets.PolicyId,
  state_token_name: assets.AssetName,
) {
  spend(_datum, _redeemer, own_ref: OutputReference, tx: Transaction) {
    expect Output {
      address: Address { payment_credential: Script(own_hash), .. },
      ..
    } = utils.resolve_output_reference(tx.inputs, own_ref)
    stake_validator.spend(
      own_hash,
      fn(r) {
        expect coerced: Pairs<Int, Int> = r
        when coerced is {
          [] -> False
          _ -> True
        }
      },
      fn(qty) { qty > 0 },
      tx,
    )
  }

  withdraw(
    redeemer: List<Pair<Int, Int>>,
    stake_cred: Credential,
    tx: Transaction,
  ) {
    multi_utxo_indexer.withdraw(
      fn(in_utxo, out_utxo) {
        authentic_input_is_reproduced_unchanged(
          state_token_symbol,
          Some(state_token_name),
          in_utxo,
          out_utxo,
        )
      },
      redeemer,
      stake_cred,
      tx,
    )
  }

  else(_) {
    fail
  }
}
```

```
use aiken/collection/list
use aiken/crypto.{ScriptHash}
use aiken/fuzz
use aiken_design_patterns/stake_validator as stake_validator
use aiken_design_patterns/utils as utils
use cardano/address.{Address, Credential, Script}
use cardano/assets.{Value}
use cardano/transaction.{Input, NoDatum, Output, Transaction, placeholder}

/// Use this function inside your withdrawal script to validate all the inputs
/// coming from the script's spend endpoint. This is an important detail, as the
/// validator needs to guarantee an exact number of inputs are spent.
///
/// The validations you can perform are:
/// - On single inputs (for each spent input)
/// - Validation on each input, and each of its corresponding outputs
/// - On the number of outputs for each input
pub fn withdraw(
  input_validator: fn(Input) -> Bool,
  input_output_validator: fn(Output, Output) -> Bool,
  output_value_and_count_validator: fn(Value, Int) -> Bool,
  redeemer: Pairs<Int, List<Int>>,
  stake_cred: Credential,
  tx: Transaction,
) -> Bool {
  stake_validator.withdraw(
    fn(indices, own_validator, tx) {
      let Transaction { inputs, outputs, .. } = tx
      let
        processed_indices,
        _,
        _,
        _,
      <-
        utils.foldl4(
          inputs,
          indices,
          -1,
          -1,
          0,
          fn(input, remaining_indices, in0, out0, i, return) {
            let next_i = i + 1
            let Input { output: in_utxo, .. } = input
            when in_utxo.address.payment_credential is {
              Script(script) ->
                if script == own_validator {
                  when remaining_indices is {
                    [] -> fail @"More UTxOs are spent than specified"
                    [Pair(in1, outs), ..rest_of_indices] ->
                      if i == in1 && in1 > in0 {
                        expect input_validator(input)?
                        let
                          new_latest_out_ix,
                          total_output_value,
                          output_count,
                        <-
                          utils.foldl3(
                            outs,
                            out0,
                            assets.zero,
                            0,
                            fn(
                              curr_out_ix,
                              prev_out_ix,
                              value_so_far,
                              count,
                              inner_return,
                            ) {
                              if curr_out_ix > prev_out_ix {
                                expect Some(out_utxo) =
                                  outputs |> list.at(curr_out_ix)
                                if input_output_validator(in_utxo, out_utxo) {
                                  inner_return(
                                    curr_out_ix,
                                    assets.merge(value_so_far, out_utxo.value),
                                    count + 1,
                                  )
                                } else {
                                  fail @"Validation on an input with one of its corresponding outputs failed"
                                }
                              } else {
                                fail @"All output indices must be in ascending order"
                              }
                            },
                          )
                        if output_value_and_count_validator(
                          total_output_value,
                          output_count,
                        ) {
                          return(
                            rest_of_indices,
                            in1,
                            new_latest_out_ix,
                            next_i,
                          )
                        } else {
                          fail @"Validation on the output count failed"
                        }
                      } else {
                        fail @"Input and output indices must be in ascending orders"
                      }
                  }
                } else {
                  return(remaining_indices, in0, out0, next_i)
                }
              _ -> return(remaining_indices, in0, out0, next_i)
            }
          },
        )
      (processed_indices == [])?
    },
    redeemer,
    stake_cred,
    tx,
  )
}

fn tests_fuzzer() -> Fuzzer<
  (ScriptHash, List<Input>, List<Output>, Pairs<Int, List<Int>>),
> {
  let script_hash <- fuzz.and_then(fuzz.bytearray_fixed(28))
  let wallet_inputs <- fuzz.and_then(utils.user_inputs_fuzzer())
  let script_inputs <-
    fuzz.and_then(
      fuzz.list_between(
        utils.specific_script_input_fuzzer(script_hash, NoDatum),
        1,
        10,
      ),
    )
  let inputs = list.concat(wallet_inputs, script_inputs) |> utils.sort_inputs
  let (script_input_indices, script_outputs) =
    list.indexed_foldr(
      inputs,
      ([], []),
      fn(i, input, acc) {
        let (i_indices, outputs) = acc
        when input.output.address.payment_credential is {
          Script(_) ->
            (
              i_indices |> list.push(i),
              outputs
                |> list.push(input.output)
                |> list.push(input.output)
                |> list.push(input.output)
                |> list.push(input.output)
                |> list.push(input.output),
            )
          _ -> acc
        }
      },
    )
  let redeemer =
    script_input_indices
      |> list.indexed_foldr(
          [],
          fn(i, script_input_index, acc) {
            list.push(
              acc,
              Pair(script_input_index, list.range(i * 5, i * 5 + 4)),
            )
          },
        )
  fuzz.constant((script_hash, inputs, script_outputs, redeemer))
}
```