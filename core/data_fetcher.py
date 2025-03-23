import os
import pandas as pd
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
CRUNCHBASE_API_KEY = os.getenv("CRUNCHBASE_API_KEY")
API_URL = "https://api.crunchbase.com/v3.1/organizations"

class DataFetcher:
    def __init__(self):
        if not CRUNCHBASE_API_KEY:
            raise ValueError("Missing Crunchbase API Key. Please set it in .env file.")
        self.api_key = CRUNCHBASE_API_KEY

    def fetch_startup_data(self, query: str, limit: int = 10):
        """Fetches startup data from Crunchbase based on a search query."""
        params = {
            "user_key": self.api_key,
            "query": query,
            "limit": limit
        }
        response = requests.get(API_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("items", [])
        else:
            print(f"Error fetching data: {response.status_code}")
            return []

    def save_to_csv(self, data, filename="startup_data.csv"):
        """Saves fetched data to a CSV file."""
        if not data:
            print("No data to save.")
            return
        
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

# Example usage
if __name__ == "__main__":
    fetcher = DataFetcher()
    startups = fetcher.fetch_startup_data("AI")
    fetcher.save_to_csv(startups)
