import requests

# Public API example
url = "https://restcountries.com/v3.1/all"

response = requests.get(url)

if response.status_code == 200:
    countries = response.json()
    print("Total countries:", len(countries))
    print("First country:", countries[0]["name"]["common"])
else:
    print("Request failed:", response.status_code)
