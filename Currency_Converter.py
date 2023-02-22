#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import requests


# In[2]:


def currency_converter():
    api_key = "rrjYTNnfAcgvNeVBTa9tWhCE0cV4hxaOl2u7rZJR" # Replace with your API key
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}"
    #print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Parse JSON object
        #exchange_rates = json.loads(json_data)["data"]
        return data
    else:
        print("No data")
        return None


# In[3]:


json_data = currency_converter()
print(json_data)
print(type(json_data))
json_data = json.dumps(json_data) # Converting to string from dictionary
print(type(json_data))
# Parse JSON object


# In[5]:


exchange_rates = json.loads(json_data)["data"]


currency1 = input("Enter a base currency: ").upper()
amount = input(f"Enter an amount in {currency1}: ")
currency2 = input("Enter a currency to convert to: ").upper()


#  conversion
conversion = exchange_rates.get(currency2) / exchange_rates.get(currency1)


# In[6]:


# Print the result
print(f"1 {currency1} = {conversion:.2f} {currency2}")
final_converted = float(amount) * conversion
print(f'The total amount after converted to  {currency2} is {final_converted:.2f}')


# In[ ]:




