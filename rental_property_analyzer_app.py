
import streamlit as st

# Title
st.title("Rental Property Analyzer")

# Sidebar inputs
st.sidebar.header("Property Details")
purchase_price = st.sidebar.number_input("Purchase Price ($)", 0, 10000000, 400000)
down_payment_percent = st.sidebar.number_input("Down Payment (%)", 0.0, 100.0, 25.0)
loan_interest_rate = st.sidebar.number_input("Loan Interest Rate (%)", 0.0, 100.0, 6.5)
loan_term_years = st.sidebar.number_input("Loan Term (Years)", 1, 40, 30)
monthly_rent = st.sidebar.number_input("Monthly Rent ($)", 0, 50000, 3500)
annual_taxes = st.sidebar.number_input("Annual Property Taxes ($)", 0, 50000, 6000)
annual_insurance = st.sidebar.number_input("Annual Insurance ($)", 0, 50000, 1500)
monthly_hoa = st.sidebar.number_input("Monthly HOA Fees ($)", 0, 1000, 0)
management_percent = st.sidebar.number_input("Property Management (%)", 0.0, 100.0, 8.0)
maintenance_percent = st.sidebar.number_input("Maintenance (% of Rent)", 0.0, 100.0, 5.0)
vacancy_percent = st.sidebar.number_input("Vacancy Allowance (%)", 0.0, 100.0, 5.0)

# Calculations
loan_amount = purchase_price * (1 - down_payment_percent / 100)
monthly_interest_rate = loan_interest_rate / 100 / 12
number_of_payments = loan_term_years * 12

monthly_mortgage = (
    loan_amount * monthly_interest_rate / 
    (1 - (1 + monthly_interest_rate) ** -number_of_payments)
    if monthly_interest_rate > 0 else 0
)

annual_gross_income = monthly_rent * 12
vacancy_loss = annual_gross_income * vacancy_percent / 100
management_fees = annual_gross_income * management_percent / 100
maintenance_cost = annual_gross_income * maintenance_percent / 100
hoa_annual = monthly_hoa * 12

annual_operating_expenses = (
    annual_taxes + annual_insurance + management_fees + maintenance_cost + hoa_annual + vacancy_loss
)

noi = annual_gross_income - annual_operating_expenses
cap_rate = (noi / purchase_price) * 100
annual_mortgage = monthly_mortgage * 12
annual_cash_flow = noi - annual_mortgage
total_cash_invested = purchase_price * down_payment_percent / 100
cash_on_cash_return = (annual_cash_flow / total_cash_invested) * 100 if total_cash_invested > 0 else 0
grm = purchase_price / annual_gross_income if annual_gross_income > 0 else 0

# Outputs
st.header("Results Summary")
st.write(f"**Monthly Mortgage Payment:** ${monthly_mortgage:,.2f}")
st.write(f"**Annual Gross Income:** ${annual_gross_income:,.2f}")
st.write(f"**Annual Operating Expenses:** ${annual_operating_expenses:,.2f}")
st.write(f"**Net Operating Income (NOI):** ${noi:,.2f}")
st.write(f"**Cap Rate:** {cap_rate:.2f}%")
st.write(f"**Annual Cash Flow:** ${annual_cash_flow:,.2f}")
st.write(f"**Cash on Cash Return:** {cash_on_cash_return:.2f}%")
st.write(f"**Gross Rent Multiplier (GRM):** {grm:.2f}")
