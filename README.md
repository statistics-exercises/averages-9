# Computing moments about the mean

The rth central moment of a data set is given by:

![](https://render.githubusercontent.com/render/math?math=\mu_r=\frac{1}{n}\sum_{i=1}^{n}(X_i-\overline{X})^r\qquad\textrm{where}\qquad\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_i)

The first central moment is always guaranteed to be zero.  The higher central moments do not need to be zero, however.  We can examine how the rth central moment of the distribution depends on the number of random variables it is computed from by writing a code that is similar to the code that we wrote to calculate how the rth moment depends on the number of random variables it is calculated from.  Within the loop in such a code we will need to evaluate the current esimate for ![](https://render.githubusercontent.com/render/math?math=\overline{X}) first.  We can then compute ![](https://render.githubusercontent.com/render/math?math=(X_i-\overline{X})) and thus accumulate the sum in the numerator of the the left-most equation above.

__To complete this exercise I want you to draw a graph showing how the values of these moments about the mean depend on the number of samples they are computed from.__  When you complete this coding task a graph is generated.  On this graph:

1. The black points indicate how the second moment about the mean changes as n increases
2. The blue points indicate how the third moment about the mean changes as n increases
3. The green points indicate how the fourth moment about the mean changes as n increases

You can use the variable called `ssum1` to accumulate the numerator in the expression for ![](https://render.githubusercontent.com/render/math?math=\overline{X}). `ssum2`, `ssum3` and `ssum4` can be then be used to accumulate the numerator in the expression for the central moment above with r=2, r=3 and r=4 respectively. The elements of the NumPy array `indices` should be set equal to 1, 2, 3, ...

  
