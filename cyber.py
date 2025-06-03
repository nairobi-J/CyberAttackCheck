
from serpapi import GoogleSearch
import csv
api_key = "9c135c7a24855570d8a719b68875b2b890c1e0f935ab3ee2970158b52e6615a3"
params = {
    "q": "site:.bd",  # Replace with your query
    "engine": "google",
    "api_key": api_key  # Replace with your API key
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






