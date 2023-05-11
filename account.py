from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random
import string
user_id=[]


for _ in range(3):

    driver=webdriver.Chrome("C:/Users/naren/Desktop/New folder/chromedriver.exe")
    driver.get("https://signup.live.com/?lic=1")
    time.sleep(1)
    mail=driver.find_element("id","MemberName")
    letters=string.ascii_letters
    new_id=''.join(random.choice(letters) for i in range(10))+"@outlook.com"
    print(new_id)
    user_id.append(new_id)
    mail.send_keys(new_id)
    time.sleep(1)
    btn=driver.find_element("id","iSignupAction")
    btn.click()
    time.sleep(3)


    pwd=driver.find_element("id","PasswordInput")
    pwd.send_keys("hello@1890")
    time.sleep(3)
    btn=driver.find_element("id","iSignupAction")
    btn.click()
    time.sleep(3)


    f_name=driver.find_element("id","FirstName")
    f_name.send_keys("goup")
    l_name=driver.find_element("id","LastName")
    l_name.send_keys("chopra")
    btn=driver.find_element("id","iSignupAction")
    btn.click()
    time.sleep(3)



    sel_m=Select(driver.find_element("id","BirthMonth"))
    sel_m.select_by_value(str(random.randint(1,12)))
    sel_d=Select(driver.find_element("id","BirthDay"))
    sel_d.select_by_value(str(random.randint(1,28)))
    year=driver.find_element("id","BirthYear")
    year.send_keys("1990")
    btn=driver.find_element("id","iSignupAction")
    btn.click()
    time.sleep(30)


    n_stay=driver.find_element("id","idBtn_Back")
    n_stay.click()
    time.sleep(1)


    # driver.get('https://rewards.bing.com/')
    # time.sleep(7)
    # btn=driver.find_element("id","start-earning-rewards-link")
    # btn.click()
    time.sleep(1)
    driver.close()
print(user_id)






