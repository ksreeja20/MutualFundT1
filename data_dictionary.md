# Data Dictionary - Mutual Fund Project

## fact_nav
Stores NAV (Net Asset Value) history of mutual funds.

Columns:
- amfi_code: Unique fund identifier
- date: NAV date
- nav: Net Asset Value

---

## fact_transactions
Stores investor transaction records.

Columns:
- investor_id: Unique investor ID
- transaction_date: Date of transaction
- amfi_code: Fund code
- transaction_type: SIP / Lumpsum / Redemption
- amount_inr: Transaction amount
- state: Investor state
- city: Investor city
- city_tier: City classification
- age_group: Investor age category
- gender: Investor gender
- annual_income_lakh: Income level
- payment_mode: Payment method
- kyc_status: Verification status

---

## fact_performance
Stores mutual fund performance metrics.

Columns:
- amfi_code: Fund code
- return_1yr_pct: 1 year return
- return_3yr_pct: 3 year return
- return_5yr_pct: 5 year return
- alpha: Excess return vs benchmark
- beta: Volatility measure
- sharpe_ratio: Risk-adjusted return
- sortino_ratio: Downside risk metric
- expense_ratio_pct: Fund expense percentage
- risk_grade: Risk classification

---

## Purpose
This database is designed for mutual fund analytics including performance tracking, investor behavior analysis, and fund comparison.