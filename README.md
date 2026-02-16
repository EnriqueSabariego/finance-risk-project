# CAC 40 Market Risk Analysis

This project demonstrates a **Market Risk Engine** for the CAC 40 index using Python. It showcases the full risk analysis workflow commonly used in banking, asset management, and quantitative finance. The focus is on **Value-at-Risk (VaR)**, **Expected Shortfall (ES)**, backtesting, and **improving risk estimates using GARCH models**.

---

## **Project Objectives**

- Analyze CAC 40 daily returns from 2010 to 2024.
- Compute descriptive statistics: mean, volatility, skewness, and kurtosis.
- Estimate market risk using:
  - **Parametric VaR** (assuming normal distribution)
  - **Historical VaR** (empirical distribution)
  - **Expected Shortfall (ES)**
- Implement **rolling VaR** to capture time-varying risk.
- Perform **backtesting using Kupiec Test** to validate the models.
- Enhance risk estimation using **GARCH(1,1) conditional volatility**.
- Compare static and dynamic VaR to demonstrate the importance of modeling volatility clustering.

---

## **Data**

- Source: Yahoo Finance (`^FCHI`)
- Frequency: Daily
- Period: 2010-01-01 to 2024-12-31
- Adjusted closing prices are used for calculations.

---

## **Methodology**

### **1. Descriptive Analysis**

- Compute daily log returns: `r_t = ln(P_t / P_(t-1))`
- Analyze statistical properties:
  - Skewness: indicates asymmetry of returns
  - Excess kurtosis: measures tail risk (fat tails)

### **2. Value-at-Risk (VaR) & Expected Shortfall (ES)**

- **Parametric (Gaussian) VaR & ES**
  - Assumes returns are normally distributed
  - VaR: threshold loss at 99% confidence
  - ES: average loss beyond VaR
- **Historical VaR & ES**
  - Uses empirical distribution of returns
  - Captures fat tails naturally

### **3. Rolling VaR & Backtesting**

- Rolling 1-year (250 days) window
- Count VaR violations (days where losses exceed VaR)
- Kupiec Test:
  - Statistical test for validating if the model correctly estimates the violation rate

### **4. GARCH-based VaR**

- Fit **GARCH(1,1)** to model time-varying volatility
- Compute conditional daily volatility
- Estimate **dynamic VaR** using GARCH σ_t
- Backtest GARCH VaR with Kupiec Test
- Compare results with static parametric model

---

## **Key Findings**

- CAC 40 returns exhibit:
  - Slight negative skewness (left-tailed)
  - High excess kurtosis (fat tails)
- **Parametric VaR (Gaussian)** underestimates risk:
  - Higher number of violations than expected
  - Kupiec test strongly rejects the model at 1% level
- **GARCH VaR** improves risk estimation:
  - Lower violation ratio, closer to theoretical 1%
  - Captures volatility clustering in turbulent market periods
- Historical VaR/ES also better reflects tail risk compared to parametric Gaussian approach

---

## **Visualizations**

The notebook includes:

- Histogram of returns with Parametric & Historical VaR/ES
- Rolling Parametric VaR with highlighted violations
- GARCH(1,1) conditional volatility over time
- GARCH-based VaR with backtested violations

All visualizations are embedded in the notebook (`cac40-risk-analysis.ipynb`) for easy reference.

---

## **How to Run**

1. Clone the repository:

```bash
git clone https://github.com/EnriqueSabariego/finance-risk-project.git
cd finance-risk-project
