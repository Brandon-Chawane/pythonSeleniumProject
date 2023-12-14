

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.saucedemo.com")
driver.maximize_window()
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, 'login-button').click()

product = driver.find_element(By.XPATH, "//span[@class='title'][contains(.,'Products')]").text

if product == 'Products':
    assert True
    print("verification was successful")
else:
    print("verification was unsuccessful")
    assert False

driver.close()
