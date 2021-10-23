import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"

querystring = {"query":"USA"}

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "cf842575a8mshee407cfe04a3c28p12983fjsn5ba5d3e4874e"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)