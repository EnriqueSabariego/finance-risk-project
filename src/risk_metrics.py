import numpy as np
from scipy.stats import norm, skew, kurtosis

# -----------------------------
# Estadísticas básicas
# -----------------------------
def log_returns(prices):
    return np.log(prices / prices.shift(1)).dropna()

def descriptive_stats(returns):
    stats = {
        'mean': returns.mean(),
        'volatility': returns.std(),
        'skewness': skew(returns),
        'kurtosis': kurtosis(returns)
    }
    return stats

# -----------------------------
# VaR y ES
# -----------------------------
def var_parametric(returns, alpha=0.01):
    mu = returns.mean()
    sigma = returns.std()
    z = norm.ppf(alpha)
    return mu + z * sigma

def es_parametric(returns, alpha=0.01):
    mu = returns.mean()
    sigma = returns.std()
    z = norm.ppf(alpha)
    return mu - sigma * (norm.pdf(z) / alpha)

def var_historical(returns, alpha=0.01):
    return np.percentile(returns, alpha*100)

def es_historical(returns, alpha=0.01):
    var_thresh = var_historical(returns, alpha)
    return returns[returns <= var_thresh].mean()
