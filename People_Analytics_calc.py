#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import random
import numpy as np

# Function to generate a random dataset
def generate_random_data(num_records=100):
    names = [f"Person {i}" for i in range(1, num_records + 1)]
    ids = [f"ID{i:03d}" for i in range(1, num_records + 1)]
    current_lms = [f"Manager {random.randint(1, 20)}" for _ in range(num_records)]
    last_lms = [f"Manager {random.randint(1, 20)}" for _ in range(num_records)]
    salary_hike = [round(random.uniform(3, 15), 2) for _ in range(num_records)]  # % hike
    trainings = [random.choice(['Python', 'Data Science', 'Machine Learning', 'Leadership', 'Communication', 'None']) for _ in range(num_records)]
    skills = [random.sample(['Python', 'R', 'SQL', 'Excel', 'Tableau', 'Power BI', 'Leadership', 'Management', 'Communication'], random.randint(3, 6)) for _ in range(num_records)]
    market_skills = ['Python', 'Machine Learning', 'Data Science', 'Leadership']  # Skills in demand
    
        # Simulated market value and future company demand
    future_market_value = [round(random.uniform(50, 150), 2) for _ in range(num_records)]  # Simulated value in currency units (e.g., K dollars)
    future_company = [random.choice(['Google', 'Amazon', 'Facebook', 'Microsoft', 'Apple', 'None']) for _ in range(num_records)]
    package_offer = [round(value * 1.2, 2) for value in future_market_value]  # 20% higher than current market value

    data = {
        'Name': names,
        'ID': ids,
        'Current_LM': current_lms,
        'Last_LM': last_lms,
        'Last_Salary_Hike (%)': salary_hike,
        'New_Trainings': trainings,
        'Skills': skills,
        'Future_Market_Value (K)': future_market_value,
        'Future_Company_Demand': future_company,
        'Suggested_Package_Offer (K)': package_offer
    }
    
    return pd.DataFrame(data)


# In[3]:


# Generate the random dataset
df = generate_random_data()


# In[4]:


df


# In[5]:


# Streamlit application
st.title("People Analytics Tool")

# Input fields
st.subheader("Enter Employee Details")
input_name = st.text_input("Name")
input_id = st.text_input("ID")

# Filter data based on input
if input_name and input_id:
    employee_data = df[(df['Name'] == input_name) & (df['ID'] == input_id)]
    
    if not employee_data.empty:
        st.write("### Employee Information:")
        st.write(f"**Current Line Manager:** {employee_data.iloc[0]['Current_LM']}")
        st.write(f"**Last Line Manager:** {employee_data.iloc[0]['Last_LM']}")
        st.write(f"**Last Recorded Salary Hike:** {employee_data.iloc[0]['Last_Salary_Hike (%)']}%")
        st.write(f"**New Trainings Taken:** {employee_data.iloc[0]['New_Trainings']}")
        st.write(f"**Skills:** {', '.join(employee_data.iloc[0]['Skills'])}")
        
        # Determine skills in market demand
        skills_in_demand = list(set(employee_data.iloc[0]['Skills']) & set(market_skills))
        st.write(f"**Skills in Market Demand:** {', '.join(skills_in_demand) if skills_in_demand else 'None'}")
        
        st.write(f"**Future Market Value:** {employee_data.iloc[0]['Future_Market_Value (K)']}K")
        st.write(f"**Future Company Demand:** {employee_data.iloc[0]['Future_Company_Demand']}")
        st.write(f"**Suggested Package Offer:** {employee_data.iloc[0]['Suggested_Package_Offer (K)']}K")
    else:
        st.write("No employee found with the given Name and ID.")

