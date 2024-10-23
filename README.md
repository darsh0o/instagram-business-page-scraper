# instagram-business-page-scraper
Fetching public info of business pages (Link in Bio for this case but what to extract can be altered accordingly by modifying the class identifier and selector based on the new classes)

This project is a simple web scraper designed to extract bio links from Instagram profiles. It logs into Instagram, visits each profile, and scrapes the bio link (if available). The extracted data is saved into a CSV file for easy access.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/darsh0o/instagram-business-page-scraper.git
   cd instagram-bio-scraper
   '''
2. **Install dependencies**:
   Install the necessary Python packages by running the following command:
   ```bash
   pip install -r requirements.txt
   '''
3. **Run the scraper**:
   - To start scraping Instagram bio links, run the following command:
   ```bash
   python insta_biolinks.py
   ```
4. **Monitor the progress**:
   - As the scraper runs, it will display progress messages in the terminal, logging whether it successfully logged into Instagram, accessed a profile, and extracted a bio link.
   - Any errors such as missing elements, timeouts, or invalid URLs will also be logged in the terminal, and the script will proceed to the next profile.

5. **Check the output**:
   - Once the scraping process is complete, an output file named `instagram_bio_links.csv` will be created in the project directory. This file will contain the following columns:
     - `Instagram URL`: The URL of the Instagram profile.
     - `Bio URL`: The extracted bio link (or "N/A" if no link was found).

6. **Optional**:
   - You can modify the list of Instagram URLs to be scraped by editing the `instagram_urls` variable inside `insta_biolinks.py`. Simply add or remove URLs as needed.

## Project Files

- **`insta_biolinks.py`**: The main Python script that automates the login to Instagram, scrapes the bio links from profiles, and saves the results to a CSV file.
- **`requirements.txt`**: Contains the necessary Python packages for running the script.
- **`instagram_bio_links.csv`**: The output file where the scraped Instagram URLs and bio links will be saved.

## Explanation of Code Logic

1. **`configure_driver()`**: Sets up the Chrome WebDriver for browser automation. This includes options such as headless mode for running the script without opening a visible browser window.

2. **`login_to_instagram()`**: Automates logging into Instagram by filling in the provided username and password. It waits for page elements to load and handles potential errors, such as timeouts or incorrect login fields.

3. **`extract_bio_url()`**: Extracts the bio URL from the Instagram profile by locating the appropriate HTML element on the profile page. If no bio URL is found, it returns "N/A".

4. **`scrape_instagram_links()`**: This is the core function responsible for navigating to each Instagram profile, extracting the bio link, and handling any errors such as missing elements or timeouts. The results are appended to a list and later written to a CSV file.

5. **`main()`**: Manages the entire process. It first logs into Instagram, then iterates through the list of Instagram profile URLs to scrape bio links, and finally saves the data into a CSV file.

## Dependencies

This project uses several Python libraries, which are listed in the `requirements.txt` file:
- `selenium`: For automating web browsing and interaction.
- `webdriver-manager`: To automatically manage and install the correct version of ChromeDriver for Selenium.
- `pandas`: For data manipulation and exporting results to CSV.
- `requests`: For handling HTTP requests (if needed for additional functionality).
- `coloredlogs`: For colorful logging output in the terminal.

To install all dependencies, run:
```bash
pip install -r requirements.txt
```

