#--------------------
# 
# Author: OG
# Description: Streamlit app that consumes an xml document from url: https://xmlserving.fly.dev/employees
# url: 
#-----------

import streamlit
import xml.etree.ElementTree as et
import pandas as pd


streamlit.title("List of Employees")

feed_url = 'https://xmlserving.fly.dev/employees'

xml_data = open(feed_url, 'r').read()  # Read file
root = et.XML(xml_data)  # Parse XML

data = []
cols = []
for i, child in enumerate(root):
    data.append([subchild.text for subchild in child])
    cols.append(child.tag)

df = pd.DataFrame(data).T  # Write in DF and transpose it
df.columns = cols  # Update column names

#print(df)

streamlit.dataframe(df)
