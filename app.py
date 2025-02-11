# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:22:34 2025

@author: debjyoti

ref: https://www.youtube.com/watch?v=43RJ3JByygE&list=PL2VXyKi-KpYtZzm1K8UKnnBzsOCtekhKq
"""

import streamlit as st

# st.set_page_config(layout="wide")

st.title("Tax Calculator for Salaried Person") 
st.header("New Regime: FY 2025-2026 (AY 2026-2027)", divider="rainbow")


st.header("tax calculation")
gross_income = st.number_input("Enter your gross salary : ")
if st.button("Calculate"):   
    if gross_income > 1275000:
        taxable_gross_income = gross_income - 75000
        if taxable_gross_income > 2400000:
            tax = 400000*0.75  + (taxable_gross_income - 2400000)*0.3
        elif taxable_gross_income > 2000000:
            tax = 400000*0.5 + (taxable_gross_income - 2000000)*0.25
        elif taxable_gross_income > 1600000:
            tax = 400000*0.3 + (taxable_gross_income - 1600000)*0.2
        else:
            tax = 400000*0.15 + (taxable_gross_income - 1200000)*0.15
        
        st.write("\n==================================================")
        st.write("\nStandard deduction (INR): 75000")
        st.write (f"\nYearly taxable gross income (after SD) is (INR): {taxable_gross_income}")
        st.write("\n==================================================")
        st.write (f"\nYearly net tax payable is (INR): {tax}")
        st.write (f"\nMonthly net tax payable is (INR): {tax/12}")
        st.write("\n==================================================")
        st.write (f"\nMonthly in-hand approximate salary (INR): {(taxable_gross_income-tax)/12}")
        st.write("\n==================================================")
    else:
        st.write("\n==================================================")
        st.write (f"\nMonthly tentative in-hand salary (INR): {gross_income/12}")
        st.write("\nHurray ! No tax to be paid...")
        st.write("\n==================================================")