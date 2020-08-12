# Points in ellipse
This program gets a list of equidistant points arround a given ellipse.
The method is the following:

1. Enter the ellipse x-radius as $a$ and y-radius as $b$
2. Enter the number of points as $n$
3. Calculate the perimeter of the ellipse (an approximate) as $p$
4. Calculate the distance between points ($p/n$) as $l$
5. Put an initial point in the ellipse, for example the point $(a,0)$
6. Calculate the angle $\theta$ of a vector with length $l$ so its initial point
is the point selected in step 5, and its final points is in the ellipse.
7. Save the final point of the vector in step 6, and use it to repeat from 
step 5.

To calculate the angle in step 6, solve the following equation by approximation
(like bisection method):

$$\left(x_1,y_1\right) = 
\left(x_0,y_0\right) + 
L\times\begin{pmatrix}cos\theta\\sin\theta\end{pmatrix}$$

$$x_1=x_0 + L\times cos\theta$$

$$y_1=y_0 + L\times sin\theta$$

$$\frac{x_1^2}{a^2}+\frac{y_1^2}{b^2}=1,$$

$$f(x)=
\frac{(x_0+L\times cos\theta)^2}{a^2} +
\frac{(y_0+L\times sin\theta)^2}{b^2}
= 0$$
$$Solve\space f(x) = 0$$

## Dependences
Used pygame library for drawing the points