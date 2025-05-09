import time
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

message_to_post = input("Digite a mensagem de texto a ser publicada no seu Linkedin: ")

load_dotenv("D:\EnvironmentVariables\.env")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/login/pt")

email_field = driver.find_element(By.XPATH, '//*[@id="username"]')
time.sleep(2)
email_field.click()
email_field.send_keys(os.getenv("email_linkedin"))
time.sleep(2)

password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
time.sleep(2)
password_field.click()
password_field.send_keys(os.getenv("password_linkedin"), Keys.ENTER)
time.sleep(4)

insert_field = driver.find_element(By.CSS_SELECTOR, ".share-box-feed-entry__top-bar")
time.sleep(2)
insert_field.click()
time.sleep(4)

text_field = driver.find_element(By.CSS_SELECTOR, ".ql-container p")
text_field .click()
text_field .send_keys(message_to_post)
time.sleep(4)

post_button = driver.find_element(By.CSS_SELECTOR, ".share-box_actions span")
time.sleep(2)
post_button.click()
time.sleep(2)

print("Mensagem publicada!")

driver.quit()