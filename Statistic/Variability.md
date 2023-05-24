> is used to measure the spread of the data in a distribution
> It is usually accompanies the central tendency as basic [[Descriptive Statistics]] for a set of data

* Variability serves both as a descriptive measure and as an importatn component of most inferential statistics
* In the context of inferential statistics, variability provides a measure of *how accurately any individual data point or sample represent the entire population*
	* When the population  [[Variability]] is small, all of the data points are clustered close together and any individual data point or sample will necessarily provides a good representation of the entire set.
	* On the other hand, when variability is large and data are widely spread, it is easy for one or two extreme data points to give a distorted picture of the general population
## Measures of Variability 
* Variability can be measure with
	* The range
	* The interquartile range
	* The standard deviation/variance
* In each case, variability is determined by measuring *distance*
### Range
* the difference between largest and smallest data point
* Highly affected by outliers
* Bes for symmetric data with no outliers
### Interquartile 
* 3rd quartile - 1st quartile -> the middle half of the data
* $IQR = Q3 - Q1$
* Robust to outliers or extreme observations
* Works well for skewed data.
### Sample variance
* It is the average of the squared deviations from the mean
	1. Find the difference  between each data point and mean
	2. Square the differences, and add them up
	3. Divide by one less than the number of data points
* ${s^{2}}=\frac{\sum{(x_{i}- x_a)}^2}{(n-1)}$
### Population variance
* It is the average of the squared deviations from the mean
### Sample Standard deviation 
* is the square root of variance
* ![[Pasted image 20230408215126.png]]
### Properties of the Standard Deviation
* If a constant is added to every data point in a distribution, the standard deviation will not be changed.
* If you visualize the data points in a frequency distribution histogram, then adding a constant will move each data point so that the entire distribution is shifted to a new location
* The center of the distribution (the mean) changes, but the std deviation remains the same.
* If each data point is multiplied by a constant, the standard deviation will be multiplied by the same constant.
* Multiplying by a constant will multiply the distance between data points, and because the standard deviation is a measure of distance, it will also be multiplied.
* If you are given numerical values for the mean and the standard deviation, you should be able to construct a visual image of the distribution of data points
* As a general rule, about 70% of the data points will be within one standard deviation of the mean, and about 95% of the data points will be within a distance of two standard deviations of the mean.
### Chebychev's Theorem
![[Pasted image 20230408221241.png]]
* Regardless of how the data are distributed, at least 100(1-1/k^2)% of the values will fall within k standard deviations of the mean (for k>1)
* ![[Pasted image 20230408221410.png]]
### Empirical Rule
* If the data distribution is bell-shaped, then the interval:
* ![[Pasted image 20230408221447.png]]
* ![[Pasted image 20230408221502.png]]
* The most appropriate measure of variability depends on the shape of the data's distribution 
## Choosing Appropriate Measure of Variability
* If data are symmetric, with no serious outliers, use range and standard deviation.
* If data are skewed, and/or have serious outliers use IQR
* *If comparing variation across two data sets, use coefficient of variation*

#STATISTIC 