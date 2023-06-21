from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, "//div[1]/div[1]/input")
    input1.send_keys("I")
    input2 = browser.find_element(By.XPATH, "//div[1]/div[2]/input")
    input2.send_keys("I")
    input3 = browser.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3)>input")
    input3.send_keys("M")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(3)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)

browser.quit()

