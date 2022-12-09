from scipy.stats import poisson
import numpy as np

poisson.pmf(5, 12)

poisson.cdf(12, 12)

poisson.sf(14, 12)

ks = np.arange(10, 16)

s = 0
for i in ks:
    s = s + poisson.pmf(i, 12)
print(s)
# OR

poisson.cdf(15, 12) - poisson.cdf(9, 12)

#2.
poisson.sf(70, 56)

poisson.cdf(19, 56)

#3.
poisson.sf(5, 4)

poisson.cdf(2, 4)
