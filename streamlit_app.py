#--------------------
# 
# Author: OG
# Description: Streamlit app that consumes an xml document from url: https://xmlserver.fly.dev/employees
# url: https://omargomez2-xmlservingclient-streamlit-app-jd58e7.streamlit.app/
#-----------

import streamlit
import requests
import pandas as pd

url = 'https://xmlserver.fly.dev/employees'
response  = requests.get(url, headers = {"Accept":"application/xml"})
df = pd.read_xml(response.content)                               

streamlit.title("List of Employees")

streamlit.dataframe(df)
