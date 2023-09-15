import json
import argparse

DATA_FILE = "./data.json"

def fetch_country_data():
    with open(DATA_FILE) as f:
        data = json.load(f)
        return data
    
def lookup_country_name(country_code, data):
    if country_code in data["data"]:
        return data["data"][country_code]["name"]
    else:
        return f"Country code {country_code} not found."

def main():
    parser = argparse.ArgumentParser(description="Country Lookup Service")
    parser.add_argument("--countryCode", nargs="+", help="List of country codes to lookup")

    args = parser.parse_args()

    data = fetch_country_data()

    if args.countryCode:
        for country_code in args.countryCode:
            country_name = lookup_country_name(country_code.upper(), data)
            print(f"{country_code}: {country_name}")

if __name__ == "__main__":
    main()           