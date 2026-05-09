import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pytestDemo.test_demo1 import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)
#service_obj = Service("E:/chromedriver-win64/chromedriver-win64/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

driver.get("https://adnabu-store-assignment1.myshopify.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
search_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//summary[@aria-label='Search']")))
search_icon.click()

search_input = driver.find_element(By.XPATH, "//input[@id='Search-In-Modal']")
search_input.send_keys("Snowboard")

product_xpath = "//p[contains(@class, 'predictive-search__item-heading') and contains(text(), 'The Complete Snowboard')]"

# 2. Wait for the element to be visible and clickable
product_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, product_xpath))
)

# 3. Click the product
product_element.click()

# 3. Locate the "Add to cart" button using the ID provided in your HTML
add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.ID, "ProductSubmitButton-template--19850788667482__main")));
add_to_cart_btn.click()
print("Product added to cart successfully")