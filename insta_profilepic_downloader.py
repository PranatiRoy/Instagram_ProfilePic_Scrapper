from selenium import webdriver
cd="C:\\Users\\Pranati\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
chrome_browser = webdriver.Chrome(cd)


user_handle=input("Enter the user handle of the profile: ")
fixed_url='https://www.instagram.com/'

# creating the url to the profile
url=fixed_url+user_handle

chrome_browser.get(url)

filename= user_handle+'.jpg'

# we will try to extract the image using the xpath for the profile images of public profile. Tis will fail if the profile is private.
# in that cse, the except block will be executed where the xpath for the profile image of private profiles is given.
try:
    image=chrome_browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div/span/img')
except:
    #For private accounts
    image=chrome_browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div/div/button/img')


 # extrcating the image link   
imageSrc=image.get_attribute('src')

path="D:\\"+filename

import urllib.request
# donloading and saving the image
urllib.request.urlretrieve(imageSrc,path)

print("The profile pic has been downloaded at: "+path)
