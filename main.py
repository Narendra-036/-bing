from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time



driver =webdriver.Chrome("C:\\Users\\naren\\Desktop\\New folder\\chromedriver.exe")
driver.get("https://rewards.bing.com")


# sign in process
# i0116
mail=driver.find_element("id","i0116")
mail.send_keys("njibhuvgy2@outlook.com")
# idSIButton9
time.sleep(1)
next_button=driver.find_element("id","idSIButton9")
next_button.click()
time.sleep(1)
pwd=driver.find_element("id","i0118")
pwd.send_keys("hello@1890")
time.sleep(1)

sign_button=driver.find_element("id","idSIButton9")
sign_button.click()
time.sleep(1)


# stay sign in ki button
# idBtn_Back
idBtn_Back= driver.find_element("id","idBtn_Back")
idBtn_Back.click()

# extension..........................
driver.get("https://www.bing.com")

# driver.execute_script("window.open('https://www.bing.com')")
search=driver.find_element("id","sb_form_q")
search.send_keys("sdfghjk")
search.send_keys(Keys.RETURN)
# search
# time.sleep(30)

for i in range(2):
    search=driver.find_element("id","sb_form_q")
    # time.sleep(20)
    search.send_keys(f"hello{i}")
    search.send_keys(Keys.RETURN)
    time.sleep(5)

# time.sleep(45)

