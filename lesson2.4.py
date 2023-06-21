from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
first_name = browser.find_element(By.NAME, "firstname").send_keys("Evgeniya")
last_name = browser.find_element(By.NAME, "lastname").send_keys("Rodionova")
email = browser.find_element(By.NAME, "email")
email.send_keys("123654789@gmail.com")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "stepic_file.txt")
file_button = browser.find_element(By.ID, "file").send_keys(file_path)
browser.find_element(By.CSS_SELECTOR, "button.btn").click()
sleep(5)