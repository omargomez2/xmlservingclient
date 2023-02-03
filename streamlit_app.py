#--------------------
# 
# Author: OG
# Description: Streamlit app that consumes an xml document from url: https://xmlserving.fly.dev/employees
# url: 
#-----------

import streamlit
import pandas as pd
import requests
import lxml

res = requests.get('https://xmlserving.fly.dev/employees')
doc = lxml.html.parse(res.content)

#df = pd.read_xml('https://xmlserving.fly.dev/employees', xpath="./item")                               

streamlit.title("List of Employees")

#xml_data = open(feed_url, 'r').read()  # Read file
#root = et.XML(xml_data)  # Parse XML

#data = []
#cols = []
#for i, child in enumerate(root):
#    data.append([subchild.text for subchild in child])
#    cols.append(child.tag)

#df = pd.DataFrame(data).T  # Write in DF and transpose it
#df.columns = cols  # Update column names

#print(data)

#streamlit.dataframe(df)
