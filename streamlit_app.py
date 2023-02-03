#--------------------
# 
# Author: OG
# Description: Streamlit app that consumes an xml document from url: https://xmlserving.fly.dev/employees
# url: 
#-----------

import streamlit
import requests
import pandas as pd

url = 'https://xmlserving.fly.dev/employees'
response  = requests.get(url, headers = {"Accept":"application/xml"})
df = pd.read_xml(response.content)                               

streamlit.title("List of Employees")

streamlit.dataframe(df)
