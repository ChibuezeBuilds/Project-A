from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Set up Selenium with Chrome
options = Options()
options.headless = True  # Run without opening browser
driver = webdriver.Chrome(options=options)  # Ensure ChromeDriver is in PATH or specify path

# Fetch IMDb Top 250 Movies page
url = "https://www.imdb.com/chart/top/"
try:
    driver.get(url)
    page_source = driver.page_source
except Exception as e:
    print(f"Error fetching webpage: {e}")
    driver.quit()
    exit()
driver.quit()

# Parse HTML
soup = BeautifulSoup(page_source, "html.parser")

# Extract one movie
movie = soup.find("div", class_="sc-15ac7568-0")  # Parent class
if movie:
    # Title
    title_elem = movie.find("h3", class_="ipc-title__text")
    title = title_elem.text.strip().split(". ", 1)[-1] if title_elem else "N/A"  # Remove "1. "
    
    # Year (first span in metadata)
    year_elem = movie.find("span", class_="cli-title-metadata-item")
    year = year_elem.text.strip() if year_elem else "N/A"
    
    # Rating (try common class, adjust if needed)
    rating_elem = movie.find("span", class_="ipc-rating-star--rating")
    rating_text = rating_elem.text.strip() if rating_elem else "0.0"
    try:
        rating = float(rating_text.split("/")[0]) if "/" in rating_text else float(rating_text)
    except ValueError:
        rating = 0.0
    
    print(f"Recommended Movie: {title} ({year}) - Rating: {rating}")
else:
    print("No movie found. Check parent class or dynamic content.")