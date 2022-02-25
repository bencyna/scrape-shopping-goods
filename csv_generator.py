from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
import time


class CSVGenerator():
    def __init__(self, details):
        self.docs_link = "https://docs.google.com/forms/d/e/1FAIpQLScJgj9qt8jUbq9GmWMAC5jZnjf9EKzhtjW23D-MeKlILwO-TA/viewform?usp=sf_link"
        ser = Service(r"C:\Development\chromedriver")
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=options)
        self.details = details

    def fill_in_form(self):
        pass
