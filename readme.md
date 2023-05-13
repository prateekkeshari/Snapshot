# Taking Screenshots of Multiple Web Pages using Selenium

This is a Python script that uses the Selenium library to take screenshots of multiple web pages and save them locally. 

## Requirements

To run this script, you need to have the following installed:

-  Python 3
-  Selenium
-  ChromeDriver

You can install Selenium and other required libraries using pip:

```
pip install selenium
```

You can download ChromeDriver from the official website: https://sites.google.com/a/chromium.org/chromedriver/downloads

## Usage

1. Open the script in a text editor.
2. Modify the `urls` list to include the URLs of the web pages you want to capture.
3. Run the script using the following command:

```
python screenshot.py
```

The script will launch a Chrome browser window and navigate to each URL in the `urls` list. It will wait for each page to load completely, then take a screenshot of the page and save it locally with a filename based on the domain name of the URL.

## Customization

You can customize the script to suit your needs by modifying the following variables:

-  `urls`: a list of URLs to capture
-  `driver`: the webdriver instance to use (default is Chrome)
-  `wait_time`: the number of seconds to wait for the page to load completely (default is 2)

## Notes

-  This script is intended for educational purposes only. Please respect the terms of service of the websites you are capturing screenshots of.
-  This script may not work with all websites, as some websites may have measures in place to prevent automated scraping.
-  This script captures screenshots of the entire page, including content that may not be visible in the browser window.