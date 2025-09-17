# Movie Recommendation System

Overview
This project is a Python-based movie recommendation system that scrapes movie data (titles, years, and ratings) from IMDb’s Top 250 Movies page ([https://www.imdb.com/chart/top/](https://www.imdb.com/chart/top/)) using Selenium and BeautifulSoup. It extracts up to 10 movies and recommends the highest-rated one. The project is designed for beginners, demonstrating web scraping with dynamic content handling.

## Features

Scrapes movie titles, release years, and IMDb ratings.
Recommends the movie with the highest rating.
Handles dynamic web content using Selenium.
Outputs a formatted list of scraped movies.

Prerequisites
To run this project, you need:

Python 3.x: Download from [https://www.python.org/downloads/](https://www.python.org/downloads/).
Libraries:
selenium: For rendering dynamic web content.
beautifulsoup4: For parsing HTML.
Install with: `pip install selenium beautifulsoup4`

ChromeDriver: Matches your Chrome browser version. Download from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) and place in the project directory or system PATH.
Google Chrome: Ensure Chrome is installed.

Installation

Install Python: Verify with python --version or python3 --version.
Install Libraries:pip install selenium beautifulsoup4


Install Libraries:pip install selenium beautifulsoup4

Install ChromeDriver:
Download the version matching your Chrome browser (check Chrome version via Menu > Help > About Google Chrome).
Place chromedriver in the project folder or add to PATH.
Create a directory (e.g., movie-recommender).
Save the script as movie_recommender.py.

Clone or Create Project:
Create a directory (e.g., movie-recommender).
Save the script as movie_recommender.py.

Usage

Run the Script:python movie_recommender.py
Title: The Shawshank Redemption
Year: 1994
Rating: 9.2

Scraped Movies:
1. The Shawshank Redemption (1994) - Rating: 9.2
2. The Godfather (1972) - Rating: 9.1
...


Troubleshooting:
No movies found: Check HTML selectors in Chrome Developer Tools (right-click a movie title → Inspect). Update classes in the script if needed.
Selenium errors: Ensure ChromeDriver matches Chrome version.
HTTP errors: Verify internet connection or try a different User-Agent.



Code Explanation
The script (movie_recommender.py) performs the following:

Selenium Setup: Uses Chrome in headless mode to load the IMDb page and render JavaScript content.
Webpage Fetching: Accesses https://www.imdb.com/chart/top/ and retrieves the rendered HTML.
HTML Parsing: Uses BeautifulSoup to parse the HTML.
Data Extraction:
Targets movie containers with <div class="sc-15ac7568-0 jQHOho cli-children">.
Extracts:
Title: From <h3 class="ipc-title__text">, removing numbering (e.g., "1. ").
Year: From the first <span class="cli-title-metadata-item">.
Rating: From <span class="ipc-rating-star--rating">, handling formats like "9.2/10".




Recommendation: Selects the movie with the highest rating and prints it along with all scraped movies (up to 10).

Limitations

Dynamic Selectors: IMDb’s HTML classes (e.g., sc-15ac7568-0) may change, requiring updates to selectors.
Dynamic Content: Requires Selenium due to JavaScript rendering.
Ethical Scraping: Check https://www.imdb.com/robots.txt to ensure compliance. Consider using an API (e.g., OMDb) for production use.

Future Enhancements

Add genre filtering using additional scraping or an API.
Implement user input for preferences (e.g., minimum rating).
Cache scraped data to reduce requests.
Use an API (e.g., OMDb: [http://www.omdbapi.com/](http://www.omdbapi.com/)) for more reliable data.

License
This project is for educational purposes. Ensure compliance with IMDb’s terms of service when scraping.