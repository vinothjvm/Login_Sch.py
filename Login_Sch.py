import schedule
import datetime
import time
import pyotp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# User credentials
username = 'TR2616'
password = 'Umayal@88'
totp_key = '5L7PD64WMA765ZD3BHGP46NA2PK35TZG'
print("Started at:", datetime.datetime.now())
def run_script():
    # Generate TOTP token
    totp = pyotp.TOTP(totp_key)
    token = totp.now()

    # Start the WebDriver
    driver = webdriver.Chrome()  # Make sure to have the appropriate WebDriver installed
    driver.get("https://tc.algomojo.com/#/")

    # Login process
    driver.find_element(By.NAME, 'clnt_id').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'yob').send_keys(token)
    driver.find_element(By.NAME, 'submit').click()
    # Wait for the page to load
    WebDriverWait(driver, 500).until(EC.url_to_be("https://tc.algomojo.com/ammain.html#/summary"))
    driver.get("https://tc.algomojo.com/ammain.html#/mystrategies")
    WebDriverWait(driver, 500).until(EC.url_to_be("https://tc.algomojo.com/ammain.html#/mystrategies"))
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="client_table"]/tbody[10]/tr[1]/td[8]').click()

    # Close the driver after a delay
    time.sleep(10)
    driver.quit()
    print("Execution completed at:", datetime.datetime.now())

# Schedule the job to run every day at 8 am
schedule.every().day.at("08:40").do(run_script)

# Keep the script running to allow the scheduler to work
while True:
    schedule.run_pending()
    time.sleep(60)  # Sleep for 60 seconds
    