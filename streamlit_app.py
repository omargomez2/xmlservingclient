#--------------------
# 
# Author: OG
# Description: Streamlit app that consumes an xml document from url: https://xmlserving.fly.dev/employees
# url: 
#-----------

import streamlit
import pandas

streamlit.title("List of Employees")

feed_url = 'https://xmlserving.fly.dev/employees'
df = pd.read_xml(feed_url)

streamlit.dataframe(df)
