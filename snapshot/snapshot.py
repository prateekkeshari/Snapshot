from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# create a list of URLs to capture
urls = ['https://www.getyourguide.careers', 'https://www.facebook.com', 'https://www.twitter.com']

# create a webdriver instance
driver = webdriver.Chrome()

# iterate through the list of URLs
for url in urls:
    # navigate to the URL
    driver.get(url)
    
    # wait for the page to load completely
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    
    # wait for 3 seconds to ensure all content is loaded
    time.sleep(3)
    
    # take a screenshot and save it locally
    filename = url.split('//')[1] + '.png'  # extract the domain name from the URL
    driver.save_screenshot(filename)
    
# close the webdriver instance
driver.quit()
