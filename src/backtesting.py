import numpy as np
from scipy.stats import chi2

# -----------------------------
# Rolling VaR
# -----------------------------
def rolling_var_parametric(returns, window=250, alpha=0.01):
    rolling_var = []
    for i in range(window, len(returns)):
        sample = returns[i-window:i]
        mu_roll = sample.mean()
        sigma_roll = sample.std()
        z = norm.ppf(alpha)
        rolling_var.append(mu_roll + z*sigma_roll)
    return np.array(rolling_var)

# -----------------------------
# Violations y Kupiec Test
# -----------------------------
def violations(returns, var_series, window=0):
    return returns[window:] < var_series

def kupiec_test(n_violations, total_obs, alpha=0.01):
    N = total_obs
    x = n_violations
    LR = -2 * (
        ((N - x) * np.log(1 - alpha) + x * np.log(alpha)) -
        ((N - x) * np.log(1 - x/N) + x * np.log(x/N))
    )
    p_value = 1 - chi2.cdf(LR, df=1)
    return LR, p_value
