from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

binom.pmf(k=5, n=40, p=0.25)

ks = np.arange(0,11)

s = 0
for i in ks:
    s = s + binom.pmf(k=i, n=40, p=0.25)
print(s)
 
# OR

binom.cdf(k=10, n=40, p=0.25)

binom.sf(k=19, n=40, p=0.25)

binom.stats( n=40, p=0.25)


###########  Prob Plot ################
ks = np.arange(0,41)
probs = binom.pmf(ks, n=40, p=0.25)

plt.bar(ks, probs)
plt.xlabel("Ks")
plt.ylabel("PMF")
plt.show()

#######################################
# 2.
binom.pmf(k=5, n=20, p=0.15)

binom.sf(12, 20, 0.15)

binom.cdf(10, 20, 0.15)

###########  Prob Plot ################
ks = np.arange(0,21)
probs = binom.pmf(ks, n=20, p=0.15)

plt.bar(ks, probs)
plt.xlabel("Ks")
plt.ylabel("PMF")
plt.show()

# 3.
binom.pmf(0, 20, 0.35)

binom.pmf(10, 20, 0.35)

binom.cdf(10, 20, 0.35)

binom.sf(13, 20, 0.35)
