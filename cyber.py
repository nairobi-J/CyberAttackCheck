import os

from serpapi import GoogleSearch
import csv
API_KEY = os.getenv("api_key");
params = {
    "q": "site:.bd",  # Replace with your query
    "engine": "google",
    "api_key": API_KEY  # Replace with your API key
}

search = GoogleSearch(params)
results = search.get_dict()

domains = []

for result in results.get("organic_results", []):
    domains.append(result["link"])

with open("bd_domains.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Domain"])
    for domain in domains:
        writer.writerow([domain])

print("Scraping complete. Data saved to bd_domains.csv")






