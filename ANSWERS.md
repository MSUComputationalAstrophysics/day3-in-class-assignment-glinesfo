plots.png has my functions, solutions.py has my code.

I used two functions: f = abs(x)^0.25 and f = 5 sinx/(x-1) +1

The first one breaks Newton's method, since the sharp derivative on the cusp
causes it to diverge. This only happens though when the exponent is less than
1/2, and for abs(x)^3/4 Newton's method finds the root just fine. The bisection
method and Brent's method do not apply here, since there is no sign change
across the root.

The second method doesn't break the methods, but it is difficult to work with.
It's suppose to be similar to a function we ran into doing RMHD simulations. At
one point we needed to find the positive root of this equation. However, they
where often close together, so it is difficult to create an interval with a
sign change. Additionally, the bump after the greater root will cause Newton's
method to diverge if it starts after this bump. Adding more trouble, the
function was undefined/complex for x < const. I think we used some combination
of trying Newton's method first, then if that failed, going through the pain of
numerically bounding the root and then using bisection method. Sometimes there
was no root (and no solution) so the root bounding method might also fail,
wasting CPU time (and a solution would be instead interpolated from nearby
points). Also, this was all on GPUs, so we did root findings on grids at a
time. If on point in the grid failed, all the other points would have to wait
on that point as it went through a more robust root finding method. We also had
to make sure that none of the other points went through the new method (to
match CPU results) but without slowing the code down with if statements.
Instead, it was a ton of tertiary a?b:c statements. Although it doesn't break
the methods, it was still hard to work with.
