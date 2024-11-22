"""
=========================
Main Automation Script
=========================

**Do not modify the code** in this file.

You may update the argument for the `wait_load(sec)` function in the `run()` method,
depending on the quality of your WiFi connection.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from gh import student_scores
import time
from keys import *


def wait_load(sec):
    time.sleep(sec)


class Auto_Grader:
    def __init__(self, url):
        self.driver = webdriver.Chrome()    # Set up the WebDriver
        self.url = url                      # Berea College Moodle Link

    def open_browser(self):
        self.driver.get(self.url)

    def input_value(self, find_value, key_value):
        try:
            label = self.driver.find_element(By.ID, find_value)
            label.clear()
            label.send_keys(key_value)
        except Exception as e:
            print(f"Error inputing the text: {e}")

    def click_btn(self, find_type, finding, btn_type):
        try:
            button = self.driver.find_element(find_type, finding)
            button.click()
            print(f"{btn_type} button got clicked successfully.")
        except Exception as e:
            print(f"Error clicking the link: {e}")

    def login_account(self):
        # TA Account
        self.input_value("name", username)
        self.input_value("password", password)
        # Click the login button
        self.click_btn(By.CSS_SELECTOR, "button[type='submit']", "Login Account")

    def grade(self, student_name, student_grade):
        wait_load(2)
        # Find student name
        label = self.driver.find_element(By.CLASS_NAME, "form-control")
        label.send_keys(student_name)
        wait_load(2)
        label.send_keys(Keys.ENTER)
        # Grade
        wait_load(2)
        self.input_value("id_grade", student_grade)
        self.click_btn(By.NAME, "savechanges", "Save changes")

    def run(self):
        self.open_browser()
        # Click "Log in" link
        self.click_btn(By.XPATH, f"//a[@href='{login_link}']", "Log in")

        wait_load(1)

        # Login account
        self.login_account()

        # Wait till you confirm DUO
        wait_load(5)

        # When DUO accepted there is a btn
        self.click_btn(By.ID, "trust-browser-button", "DUO confirm")

        # Wait till web loads
        wait_load(6)

        # Click the course link
        self.click_btn(By.XPATH, f"//a[@href='{course_link}']", "226 course")

        # Click quiz link
        wait_load(1)
        self.click_btn(By.XPATH, f"(//li[@id='section-1']//a)[{1 + grading_quiz}]", "Pick Quiz")
        wait_load(1)

        # Click grade btn
        self.click_btn(By.CLASS_NAME, "btn-primary", "Grade")

        # Wait till web uploads
        wait_load(5)

        # Grade
        for student_data in student_scores:
            for name in student_data:
                self.grade(name, student_data[name])

        # Wait to observe the action before closing the browser
        input("Press Enter to close the browser...")

        self.driver.quit()  # Close the browser


if __name__ == "__main__":
    register = Auto_Grader(web_link)
    register.run()
