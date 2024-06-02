


# Prob Dist
pd.crosstab(index=X1, columns=X2, margins=True)
### Joint Prob Dist          Conditional Prob Dist Columns 
normalize = all          normalize = columns

# Binom Dist
### PMF
from scipy.stats import binom
   ```
   binom.pmf(k,n,p)
   ```
### CDF
   ```
   binom.cdf(k,n,p)
   ```
### SF
   ```
   binom.sf(k,n,p)
   ```   


# Poisson Dist
### PMF
from scipy.stats import poisson
   ```
   poisson.pmf(k,mu)
   ```
### CDF
   ```
   poisson.cdf(k,mu)
   ```
### SF
   ```
   poisson.sf(k,mu)
   ```   


# Norm Dist
### PDF
from scipy.stats import norm
   ```
   norm.pdf(x, mu, sd)
   ```
### CDF
   ```
   norm.cdf(x, mu, sd)
   ```
### PPF
   ```
   norm.ppf(x, mu, sd)
   ```

# Hypothesis Testing
### 1 samp
from scipy.stats import ttest_1samp

pg = pd.read_csv("PlantGrowth.csv")

ttest_1samp(pg['weight'], popmean=6,   alternative="two-sided")

alternative can be greater than

less than

### paired or ttest_rel
rvs1 = stats.norm.rvs(loc=5,scale=10,size=500)

rvs2 = (stats.norm.rvs(loc=5,scale=10,size=500) +

...         stats.norm.rvs(scale=0.2,size=500))

stats.ttest_rel(rvs1,rvs2)

(0.24101764965300962, 0.80964043445811562)

### bartlett and indentical 
bartlett(chilled['uptake'], unchilled['uptake'])

if h0 then equal_var = True

if h1 then equal_var = False

ttest_ind(chilled['uptake'], unchilled['uptake'],equal_var=True)


### ANOVA

###Yield

agr = pd.read_csv("Yield.csv")

agr_ols = ols('Yield ~ Treatments', data=agr).fit()

table = anova_lm(agr_ols, typ=2)

print(table)

######## Post Hoc Tukey HSD ################

compare = pairwise_tukeyhsd(agr['Yield'], agr['Treatments'], alpha=0.05)

dd = pd.DataFrame(compare._results_table.data)
.
.
.
### Chi-Square

from scipy.stats import chi2_contingency

housing = pd.read_csv("Housing.csv")

ctab = pd.crosstab(housing['prefarea'], housing['gashw'])

test_statistic, p_value, df, expected_frequencies = chi2_contingency(ctab)

print(p_value)



# Regression

from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score

lr = LinearRegression()

lr.fit(X,y)

y_pred=lr.predict(X)

r2_score(y,y_pred)



# polynomial

####degree = 2

poly = PolynomialFeatures(degree=2)

poly.fit(X_train)



X_trn_poly = poly.transform(X_train)

X_tst_poly = poly.transform(X_test)



lr = LinearRegression()

lr.fit(X_trn_poly,y_train)

y_pred = lr.predict(X_tst_poly)

print(r2_score(y_test, y_pred))



######Using Pipeline#############

from sklearn.pipeline import Pipeline

poly = PolynomialFeatures(degree=2)

lr = LinearRegression()

pipe = Pipeline([('Polynomial',poly),('LIN',lr)])



pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)

print(r2_score(y_test, y_pred))

# Correlation matrix

pizza.corr()


# Efficient Data Analytics
---

###### _understanding Apache Arrow with different architectures_



### Arrow Function Mapping to x86 and ARM64 Vector Instructions

| Arrow Function             | Description                          | x86 Vector Instructions                | ARM64 Vector Instructions               |
|----------------------------|--------------------------------------|----------------------------------------|-----------------------------------------|
| **Load/Store**             | Load/store data from/to memory       | `VMOVDQU`, `VMOVDQA`, `VMOVUPS`, `VMOVAPS` | `LD1`, `ST1` (multiple variants)        |
| **Add**                    | Element-wise addition                | `VPADDQ` (int), `VADDPS` (float), `VADDPD` (double) | `ADD`, `FADD`                           |
| **Subtract**               | Element-wise subtraction             | `VPSUBQ` (int), `VSUBPS` (float), `VSUBPD` (double) | `SUB`, `FSUB`                           |
| **Multiply**               | Element-wise multiplication          | `VPMULLD` (int), `VMULPS` (float), `VMULPD` (double) | `MUL`, `FMUL`                           |
| **Divide**                 | Element-wise division                | `VDIVPS` (float), `VDIVPD` (double)    | `FDIV`                                  |
| **Comparison**             | Element-wise comparison              | `VPCMPGTQ` (int), `VCMPPS` (float), `VCMPPD` (double) | `CMP`, `FCMP`                           |
| **Logical AND**            | Bitwise AND                          | `VPAND`                                | `AND`                                   |
| **Logical OR**             | Bitwise OR                           | `VPOR`                                 | `ORR`                                   |
| **Logical XOR**            | Bitwise XOR                          | `VPXOR`                                | `EOR`                                   |
| **Shuffle**                | Rearrange elements                   | `VPSHUFB`, `VPERM2F128`, `VPERMD`      | `TBL`, `VTBL`                           |
| **Horizontal Add**         | Sum of adjacent pairs                | `VPHADDW`, `VHADDPS`, `VHADDPD`        | `ADDP`                                  |
| **Reduction Sum**          | Sum of all elements                  | `VPREDUCEADD`                          | `ADDV`, `FADDV`                         |
| **Masking**                | Apply mask to elements               | `VMASKMOVPS`, `VMASKMOVPD`, `VBLENDVPS` | `BIC` (bitwise clear), `BIT` (bitwise insert) |
| **Convert to Float**       | Convert integer to float             | `VCVTDQ2PS`, `VCVTQQ2PS`               | `SCVTF`                                 |
| **Convert to Integer**     | Convert float to integer             | `VCVTPS2DQ`, `VCVTPS2QQ`               | `FCVTZS`                                |
| **Broadcast**              | Broadcast scalar across vector       | `VPBROADCASTD`, `VPBROADCASTQ`, `VBROADCASTSS` | `DUP`, `LD1R`                          |
| **Blending**               | Merge elements based on mask         | `VBLENDVPS`, `VBLENDVPD`               | `BIT` (bitwise insert)                  |



### Comparison of Ampere ARM Processors and Modern x86 Processors

| Feature                      | Ampere ARM Processors                           | Modern x86 Processors                             |
|------------------------------|-------------------------------------------------|---------------------------------------------------|
| SIMD Instruction Set         | NEON                                            | SSE, SSE2, SSE3, SSSE3, SSE4, AVX, AVX2, AVX-512  |
| Advanced Vector Extension    | SVE, SVE2                                       | AVX, AVX2, AVX-512                                |
| Vector Register Width        | NEON: 128-bit, SVE: 128 to 2048-bit             | SSE: 128-bit, AVX: 256-bit, AVX-512: 512-bit      |
| Floating-Point Support       | Single, Double, and Half-Precision (NEON, SVE)  | Single, Double-Precision (SSE, AVX)               |
| Data Types                   | Integer, Floating-Point (NEON, SVE)             | Integer, Floating-Point (SSE, AVX)                |
| Instruction Set Extensions   | NEON, SVE                                       | SSE, AVX, AVX2, AVX-512                           |
| Application Domain           | HPC, Cloud Computing, Signal Processing         | General Computing, HPC, AI, Scientific Computing  |






## License

MIT - **Free Software, Hell Yeah!**


