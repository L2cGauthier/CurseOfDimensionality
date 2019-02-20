# An illustration to the "curse of dimensionality"

This project is a learning experiment. It's aimed at visualizing the so-called curse of dimensionality and its implications

## The curse of dimensionality

In machine learning, the curse of dimensionality is a phenomenon that appears when considering spaces with a high number of dimensions. Indeed, if we have some data points in R<sup>p</sup> (observations with p features), the higher p, the more adding an additional dimension will increase the volume of the space containing the data points.

In other words, if we have just a few observations and a lot of features, the available data will become sparse, and distance-based algorithm (like k-NN) a lot less relevant. A simple illustration can be obtained with the following process.


```

For numbers of dimension between 1 and 100
	Generate 10k pairs of points which coordinates are uniformly distributed in [0,1]
	Calculate the average, and minimum distance among those pairs
Plot the average and minimum distance among pairs with respect to the number of dimensions

```

## Visualization

If we consider spaces of dimension 1 to 100, and measure the mean and minimum distances between 10k pairs of random points with coordinates in [0,1], we obtain the following plot.


![Curse of dimensionality visualization](https://github.com/L2cGauthier/CurseOfDimensionality/blob/master/Results/100D-10kpairs.png?raw=true)


We observe that the average distance between pairs is increasing steadily and rapidly. To be more precise, given the fact we generated points which coordinates are uniformly distributed in [0,1], if the number of pair generated is high enough, we can write the function f associating to the number of dimension with the average distance between pairs as:


<a href="https://www.codecogs.com/eqnedit.php?latex=f(x)&space;=&space;\sqrt{\sum_{i=1}^{x}(\frac{1}{2})^{2}}&space;=&space;\frac{1}{2}\sqrt{x}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;\sqrt{\sum_{i=1}^{x}(\frac{1}{2})^{2}}&space;=&space;\frac{1}{2}\sqrt{x}" title="f(x) = \sqrt{\sum_{i=1}^{x}(\frac{1}{2})^{2}} = \frac{1}{2}\sqrt{x}" /></a>


The minimum distance between pairs is always smaller than the mean but increases at roughly the same rate as the mean distance.



