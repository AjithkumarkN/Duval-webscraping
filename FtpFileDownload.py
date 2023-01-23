from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from pathlib import Path
class FtpFileDownlod():
    options = Options()  
    options.add_argument("--headless") 
    download_path = str(Path.home() / "Downloads")
    chrome_prefs = {"download.default_directory":download_path} 
    options.experimental_options["prefs"] = chrome_prefs
    s = Service(executable_path='/media/funbook/74622996-999c-45ee-b9ae-bc3cde298dc4/funbook/chrome-driver/chromedriver')
    driver = webdriver.Chrome(service=s,options=options)
    clerk_url='https://ftp.duvalclerk.com/'
    driver.get(clerk_url)
    driver.implicitly_wait(2)
    driver.find_element(By.CSS_SELECTOR,'#user-box-text').send_keys('ftp dualclerk username')
    driver.find_element(By.CSS_SELECTOR,'#pword-box-text').send_keys('ftp dualclerk password')
    driver.find_element(By.CSS_SELECTOR,'#btn-LoginButton').click()
    click_action=ActionChains(driver)
    casefile_folder=driver.find_element(By.CSS_SELECTOR,'#ListFiles-row-0')
    click_action.double_click(casefile_folder).perform()
    time.sleep(2)
    file_location=driver.find_element(By.XPATH,"/html[1]/body[1]/div[55]/div[5]/span[1]/span[1]/span[1]/span[2]/span[1]/span[1]/span[2]/span[1]/span[last()-1]")
    click_action.double_click(file_location).perform()
    store_filelocation_detail=[]
    store_filelocation_detail.append(file_location.text.split('.'))
    filename=store_filelocation_detail[0][0]