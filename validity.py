import requests

websites = [
    "https://rupalibank.com.bd/",
    "https://pbi.gov.bd/",
    "https://grs.gov.bd/",
    "https://aisd.edu.bd/",
    "https://bup.edu.bd/",
    "http://kpmg.com.bd/",
    "https://swap.com.bd/",
    "https://parjatan.gov.bd/",
    "https://easyfashion.com.bd/",
    "https://a2i.gov.bd/"
]

def validate_websites(websites):
    valid_websites = []
    for website in websites:
        try:
            response = requests.get(website, timeout=10)
            if response.status_code == 200:
                print(f"{website} is accessible.")
                valid_websites.append(website)
            else:
                print(f"{website} returned status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {website}: {e}")
    return valid_websites

valid_websites = validate_websites(websites)
print("Valid Websites:", valid_websites)
