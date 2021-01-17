from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:/Users/Nitin/Development/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
driver.get(url="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102713980&keywords=python%20developer&location=India")


sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(3)

user_name = driver.find_element_by_id("username")
user_name.send_keys("nky7988@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("8810nky@#0")
password.send_keys(Keys.ENTER)


jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")
for job in jobs:
    job.click()

    try:
        time.sleep(5)
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(2)
        phone_button = driver.find_element_by_css_selector(".ember-view .display-flex input")
        if phone_button.text is None:
            phone_button.send_keys("8810367295")
        submit_button = driver.find_element_by_name("Submit application")

    except NoSuchElementException:
        time.sleep(2)
        cancel_button = driver.find_element_by_css_selector("#artdeco-modal-outlet button")
        cancel_button.click()
        time.sleep(2)
        discard_button = driver.find_elements_by_css_selector(".artdeco-modal .artdeco-modal__actionbar button")
        discard_button[1].click()
    else:
        submit_button.click()


time.sleep(5)
driver.quit()


