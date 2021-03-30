from selenium import webdriver
cd="C:\\Users\\Pranati\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
chrome_browser = webdriver.Chrome(cd)


user_handle=input("Enter the user handle of the profile: ")
fixed_url='https://www.instagram.com/'

url=fixed_url+user_handle

chrome_browser.get(url)

filename= user_handle+'.jpg'


try:
    image=chrome_browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div/span/img')
except:
    #For private accounts
    image=chrome_browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div/div/button/img')

imageSrc=image.get_attribute('src')

path="D:\\"+filename

import urllib.request

urllib.request.urlretrieve(imageSrc,path)

print("The profile pic has been downloaded at: "+path)
