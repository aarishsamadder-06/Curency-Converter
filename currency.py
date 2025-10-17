import requests

API_KEY = 'fca_live_lVMX46daHiJQEMpgeD5IZeiVItXnDoKQOsU8WjtI'
BASE_URL = "https://api.freecurrencyapi.com/v1/latest"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}?apikey={API_KEY}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("API request failed with status:", response.status_code)
            return None
        data = response.json()
        return data.get("data")  # Returns only the rates dictionary
    except Exception as e:
        print("Error:", e)
        return None

while True:
    bas = input("Enter the base currency (q for quit): ").upper()
    
    if bas == "Q":
        print("Exiting...")
        break
    
    if bas not in CURRENCIES:
        print("Invalid currency. Please try again.")
        continue

    data = convert_currency(bas)
    if data:
        print(f"Conversion rates based on {bas}:")
        for ticker, value in data.items():
            # Skip the base currency itself
            if ticker == bas:
                continue
            print(f"{ticker}: {value}")
        print("-" * 30)
    else:
        print("Failed to fetch currency data. Try again.")

