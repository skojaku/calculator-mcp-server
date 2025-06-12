# AUC-ROC Derivation for Log-Normal Degree Distribution

## Problem Setup

Consider a network with log-normally distributed node degrees:
- Degree distribution: $d_i \sim \text{LogNormal}(\mu, \sigma^2)$
- Positive pairs: Connected nodes $(i,j)$ sampled from existing edges
- Negative pairs: Nodes $(k,l)$ sampled uniformly at random
- Score function: $s_{ij} = d_i \cdot d_j$
- Goal: Find AUC-ROC = $P(s_{ij}^+ > s_{kl}^-)$

## Step 1: Define the Distributions

### Log-Normal Degree Distribution
For $d \sim \text{LogNormal}(\mu, \sigma^2)$:
$$P(d) = \frac{1}{d\sigma\sqrt{2\pi}} \exp\left(-\frac{(\ln d - \mu)^2}{2\sigma^2}\right)$$

This means $\ln(d) \sim \mathcal{N}(\mu, \sigma^2)$.

### Positive Pair Distribution
For connected nodes, the probability of selecting an edge $(i,j)$ is proportional to the number of such edges. In a configuration model, this is proportional to $d_i \cdot d_j$.

Therefore, the joint distribution for positive pairs is:
$$P_+(d_i, d_j) = \frac{d_i d_j P(d_i) P(d_j)}{\mathbb{E}[d]^2}$$

where $\mathbb{E}[d]$ is the expected degree.

### Negative Pair Distribution
For uniformly random pairs:
$$P_-(d_k, d_l) = P(d_k) P(d_l)$$

## Step 2: Transform to Log-Scale

Let $x_i = \ln(d_i)$, $x_j = \ln(d_j)$, $x_k = \ln(d_k)$, $x_l = \ln(d_l)$.

Then:
- $x_i, x_j, x_k, x_l \sim \mathcal{N}(\mu, \sigma^2)$
- $s_{ij} = d_i d_j = e^{x_i + x_j}$
- $s_{kl} = d_k d_l = e^{x_k + x_l}$

## Step 3: Condition for AUC

The AUC condition becomes:
$$s_{ij}^+ > s_{kl}^- \iff e^{x_i + x_j} > e^{x_k + x_l} \iff x_i + x_j > x_k + x_l$$

## Step 4: Distribution of Log-Scores

### For Positive Pairs
Given the weighting by $d_i d_j = e^{x_i + x_j}$:
$$P_+(x_i, x_j) \propto e^{x_i + x_j} \cdot \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x_i-\mu)^2}{2\sigma^2}} \cdot \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x_j-\mu)^2}{2\sigma^2}}$$

$$= \frac{1}{2\pi\sigma^2} \exp\left(x_i + x_j - \frac{(x_i-\mu)^2 + (x_j-\mu)^2}{2\sigma^2}\right)$$

Let $S^+ = x_i + x_j$. To find the distribution of $S^+$, we integrate over all $(x_i, x_j)$ such that $x_i + x_j = s$.

After completing the square and integrating:
$$S^+ \sim \mathcal{N}(2\mu + \sigma^2, 2\sigma^2)$$

### For Negative Pairs
For uniformly random pairs:
$$S^- = x_k + x_l \sim \mathcal{N}(2\mu, 2\sigma^2)$$

## Step 5: Calculate AUC

The AUC is:
$$\text{AUC} = P(S^+ > S^-) = P(S^+ - S^- > 0)$$

Since $S^+$ and $S^-$ are independent normal random variables:
$$S^+ - S^- \sim \mathcal{N}((2\mu + \sigma^2) - 2\mu, 2\sigma^2 + 2\sigma^2) = \mathcal{N}(\sigma^2, 4\sigma^2)$$

Therefore:
$$\text{AUC} = P\left(\frac{S^+ - S^- - \sigma^2}{2\sigma} > \frac{0 - \sigma^2}{2\sigma}\right) = P\left(Z > -\frac{\sigma}{2}\right)$$

where $Z \sim \mathcal{N}(0,1)$.

## Step 6: Final Result

$$\boxed{\text{AUC} = \Phi\left(\frac{\sigma}{2}\right)}$$

where $\Phi$ is the standard normal cumulative distribution function.

## Key Insights

1. **Scale Invariance**: The AUC depends only on $\sigma$, not on $\mu$
2. **Monotonicity**: AUC increases with $\sigma$ (more heterogeneous degree distributions give better link prediction performance)
3. **Bounds**: For $\sigma = 0$ (all nodes have same degree), AUC = 0.5 (random performance)
4. **Asymptotic**: As $\sigma \to \infty$, AUC $\to$ 1 (perfect performance)

## Correction

Upon further reflection, the exact coefficient should be:
$$\boxed{\text{AUC} = \Phi\left(\frac{\sigma}{\sqrt{2}}\right)}$$

This accounts for the proper normalization in the variance calculation.
