user_id=['CoYPcYYGWC@outlook.com', 'AkQuYCkSaQ@outlook.com', 'SAQkhtvJsP@outlook.com',"YkkjKhTksu@outlook.com","GxvmQLXPzM@outlook.com","TRyYdctPCX@outlook.com",'obkXppCriJ@outlook.com', 'xZKGDZzQiK@outlook.com', 'MBgFjPzCGo@outlook.com','kcbUtKIRve@outlook.com', 'PcZXPBryuc@outlook.com', 'tGHnRUnUiQ@outlook.com',"sxRUlrgeSb@outlook.com"]
print(len(user_id))

from selenium import webdriver
import time 
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument("--auto-open-devtools-for-tabs")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"C:/Users/naren/Desktop/New folder/chromedriver.exe")
driver.get("https://selenium.dev/documentation/en/")
time.sleep(6)
driver.get("https://www.google.com")
time.sleep(30)