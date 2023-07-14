from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open Flipkart website
driver.get("https://www.flipkart.com/")

# Close the login popup if it appears
try:
    close_button = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")
    close_button.click()
except:
    pass

# Search for the phone
search_box = driver.find_element(By.XPATH, "//input[@title='Search for products, brands and more']")
search_box.send_keys("phone")
search_box.submit()

# Wait for the search results to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-id]")))

# Select the first search result
first_result = driver.find_element(By.XPATH, "//div[@data-id]")
first_result.click()

# Switch to the new window
driver.switch_to.window(driver.window_handles[-1])

# Wait for the "Add to Cart" button to be clickable
add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button")))

# Add the phone to the cart
add_to_cart_button.click()

# Close the browser
driver.quit()
