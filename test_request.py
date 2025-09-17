import requests

url = "https://www.imdb.com/chart/top/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/117.0.0.0 Safari/537.36"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print("Webpage accessed successfully!")
    print(response.text[:500])  # Print first 500 characters of HTML
except requests.RequestException as e:
    print(f"Error fetching webpage: {e}")