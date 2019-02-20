# An illustration to the "curse of dimensionality"

This project is a learning experiment. It's aimed at visualizing the so-called curse of dimensionality and its implications

## The curse of dimensionality



```


```

## Visualization

If we consider spaces of dimension 1 to 100, and measure the mean and minimum distances between 10k pairs of random points with coordinates in [0,1], we obtain the following plot.

![Curse of dimensionality visualization](https://github.com/L2cGauthier/CurseOfDimensionality/blob/master/Results/100D-10kpairs.png?raw=true)

We observe that the average distance between pair is increasing steadily and rapidly. In fact given the fact we generated points which coordinates are uniformly distributed in [0,1], we can write the function f associating to the number of dimension the average distance between pairs as:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(x)&space;=&space;\sqrt{\sum_{i=1}^{x}(\frac{1}{2})^{2}}&space;=&space;\frac{1}{2}\sqrt{x}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;\sqrt{\sum_{i=1}^{x}(\frac{1}{2})^{2}}&space;=&space;\frac{1}{2}\sqrt{x}" title="f(x) = \sqrt{\sum_{i=1}^{x}(\frac{1}{2})^{2}} = \frac{1}{2}\sqrt{x}" /></a>

The minimum distance between pair is always smaller than the mean but increases at roughly the same rate as the mean distance.



