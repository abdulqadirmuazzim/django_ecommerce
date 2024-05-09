from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

web = webdriver.Edge()

web.get("http://127.0.0.1:8000/")
time.sleep(100)

web.find_element(By.PARTIAL_LINK_TEXT, "Ho").click()

time.sleep(10)

web.find_element(By.LINK_TEXT, "Shop").click()


web.find_element(By.LINK_TEXT, "Why Us").click()


web.find_element(By.LINK_TEXT, "Testimonial").click()


web.find_element(By.LINK_TEXT, "Contact Us").click()

time.sleep(20)
web.quit()


# Create your tests here.
