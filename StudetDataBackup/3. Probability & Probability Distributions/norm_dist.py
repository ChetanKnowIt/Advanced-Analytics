from scipy.stats import norm

norm.cdf(58, 64, 4)

norm.sf(200, 180, 30)

norm.ppf(0.95, 100, 15)

norm.sf(2000, 1678, 500)

norm.ppf(0.9, 1678, 500)

norm.cdf(1900, 1678, 500) - norm.cdf(1000, 1678, 500)

norm.ppf(0.98, 313, 57)

norm.ppf(0.9, 93, 22)

p_a = norm.sf(450, 313, 57)
p_b = norm.sf(150, 93, 22)
p_a + p_b - p_a*p_b

