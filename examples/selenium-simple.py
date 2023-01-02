from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

browser = webdriver.Chrome()
browser.get("https://www.airbnb.com/experiences/272085")
title = (
    WebDriverWait(driver=browser, timeout=10)
    .until(visibility_of_element_located((By.CSS_SELECTOR, "h1")))
    .text
)
content = browser.page_source
print(title)
print(content)
browser.close()
