# Custom Instructions for Bachelor Thesis Project

## Project [[OPERATING SYS/context]]

### Overview
- **Title**: Choreographed [[Process]] Enactment on Cardano: A decentralized Application for Service Orchestration
- **Domain**: Computer Science - [[Blockchain]] (Cardano)

### Technical Stack
- **[[Smart Contract]]**
  - Aiken for contract development
- **Frontend Framework**
  - NextJS
  - TailwindCSS
  - Flowbite components
  - MeshJS for contract construction
- **BPMN Tooling**
  - chor-js for BPMN visualization
  - Custom XML parser for BPMN processing
- **[[Process]] Model**
  - Choreography BPMN with penalty patterns (EDOC 2024)
- **Storage**
  - IPFS with Pinata provider
- **Token**
  - Native [[tokens]] for service [[Thesis(possible)/Token/Metadata|metadata]]

## Technical Framework

### [[Smart Contract]] Implementation
1. **State Channel-Inspired Approach**
   - Off-chain state management
   - Multi-party confirmation mechanism
   - Non-enforced state transitions
   - Party signature validation

2. **Hybrid Escrow-Marketplace [[Validator]]**
   - Multi-step escrow functionality
   - Marketplace integration
   - State transition validation
   - [[parties|Participant]] [[role]] management

3. **State Management**
   - Off-chain state tracking
   - On-chain state verification
   - Party confirmation handling
   - Dispute resolution mechanisms

### Implementation Patterns
1. **State Channel Patterns**
   - Off-chain state updates
   - Multi-signature validation
   - State [[synchronization]]
   - Dispute handling

2. **Escrow-Marketplace Integration**
   - Multi-step [[Cardano Transaction|transaction]] flow
   - [[Role]]-based access control
   - Price and payment handling
   - State transition rules

### BPMN Processing and Visualization
1. **BpmnParser Implementation**
   - Element extraction:
     - ID
     - Type
     - Name
     - Outgoing connections
   - JSON transformation for Cardano compatibility
   - Focus on EDOC 2024 patterns
   - Linear flow processing (start to end)

2. **Chor-js Integration**
   - Viewer customization:
     - Element highlighting capability
     - Current state visualization
     - Navigation through button interactions
   - [[Process]] flow visualization:
     - Start event identification
     - Route selection interface
     - Current element highlighting

3. **State Management**
   - One-directional flow implementation
   - [[Cardano Transaction|Transaction]]-based state transitions
   - Multi-party agreement mechanism
   - Future extensibility:
     - [[Cardano Transaction|Transaction]] output [[datum]] querying
     - Historical state reconstruction
     - State [[synchronization]] capabilities

## Writing Guidelines

### Literature Review Focus
- Emphasis on Choreography BPMN [[concepts]]
- EDOC 2024 penalty patterns
- Cardano technical architecture
- [[Smart contract]] implementation patterns
- Decentralized storage patterns

### Technical Documentation Requirements
1. **Required Diagrams**
   - Choreography pattern implementation
   - Penalty mechanism design
   - Architecture overview
   - [[Smart contract]] state transitions
   - Storage architecture and data flow
   - Token [[Thesis(possible)/Token/Metadata|metadata]] structure
   - BPMN parsing workflow
   - Component interaction architecture
   - State transition flow
   - Future state [[synchronization]] design

2. **Implementation Documentation**
   - BpmnParser architecture and functionality
   - Chor-js customization details
   - State transition mechanisms
   - Token [[Thesis(possible)/Token/Metadata|metadata]] structure
   - Future enhancement possibilities

3. **[[Process]] Flow Documentation**
   - Element extraction [[process]]
   - State transition logic
   - User interaction patterns
   - [[Blockchain]] integration points

### Implementation Details
1. **Core Components**
   - Penalty pattern implementation
   - Choreography state management
   - MeshJS integration patterns
   - Token design and [[Thesis(possible)/Token/Metadata|metadata]] structure
   - IPFS integration and data management
   - Technology evolution challenges

2. **State Channel Implementation**
   - Off-chain vs on-chain state management
   - Party confirmation mechanisms
   - State [[synchronization]] patterns
   - [[Security]] considerations

3. **Escrow-Marketplace Analysis**
   - Multi-step [[Cardano Transaction|transaction]] design
   - [[Role]] management
   - State transition rules
   - Integration patterns

## Component Architecture

### BpmnParser Class
- XML parsing functionality
- Element extraction logic
- Sequence flow mapping
- [[Process]] navigation support

### Integration Points
- Parser-to-Viewer communication
- Element ID-based highlighting
- State transition management
- Token [[Thesis(possible)/Token/Metadata|metadata]] validation

## Assumptions and Constraints
- Token [[Thesis(possible)/Token/Metadata|metadata]] integrity assumed
- Parser state validity guaranteed
- Linear progression flow
- Multi-party confirmation requirement

## Evaluation Criteria

### Functional Requirements
- Accurate XML parsing
- Correct element highlighting
- Valid state transitions
- Multi-party confirmation
- Token [[Thesis(possible)/Token/Metadata|metadata]] handling

### Technical Requirements
- Parser performance
- State transition reliability
- Component integration effectiveness
- [[Blockchain]] interaction efficiency