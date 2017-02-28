#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from SimpleFunctions import sendEmail, takeScreenshot_Chrome, createFolder, takeScreenshot

from selenium.webdriver.chrome.options import Options

strBrowser = "Mobile"
imgDirName = createFolder(strBrowser)
errorMsg = "Default Error Message"
success = True
strSendTo = 6 #Default value

# Setup ChromeDriver for mobile emulation
mobile_emulation = { 
			#"deviceName": "Apple iPhone 3GS"
			#"deviceName": "Apple iPhone 4"
			#"deviceName": "Apple iPhonea 5"
			#"deviceName": "Apple iPhone 7"
			"deviceName": "Apple iPhone 6 Plus"
			#"deviceName": "BlackBerry Z10"
			#"deviceName": "BlackBerry Z30"
			#"deviceName": "Google Nexus 4"
			#"deviceName": "Google Nexus 5"
			#"deviceName": "Google Nexus S"
			#"deviceName": "HTC Evo, Touch HD, Desire HD, Desire"
			#"deviceName": "HTC One X, EVO LTE"
			#"deviceName": "HTC Sensation, Evo 3D"
			#"deviceName": "LG Optimus 2X, Optimus 3D, Optimus Black"
			#"deviceName": "LG Optimus G"
			#"deviceName": "LG Optimus LTE, Optimus 4X HD" 
			#"deviceName": "LG Optimus One"
			#"deviceName": "Motorola Defy, Droid, Droid X, Milestone"
			#"deviceName": "Motorola Droid 3, Droid 4, Droid Razr, Atrix 4G, Atrix 2"
			#"deviceName": "Motorola Droid Razr HD"
			#"deviceName": "Nokia C5, C6, C7, N97, N8, X7"
			#"deviceName": "Nokia Lumia 7X0, Lumia 8XX, Lumia 900, N800, N810, N900"
			#"deviceName": "Samsung Galaxy Note 3"
			#"deviceName": "Samsung Galaxy Note II"
			#"deviceName": "Samsung Galaxy Note"
			#"deviceName": "Samsung Galaxy S III, Galaxy Nexus"
			#"deviceName": "Samsung Galaxy S, S II, W"
			#"deviceName": "Samsung Galaxy S4"
			#"deviceName": "Sony Xperia S, Ion"
			#"deviceName": "Sony Xperia Sola, U"
			#"deviceName": "Sony Xperia Z, Z1"
			#"deviceName": "Amazon Kindle Fire HDX 7″"
			#"deviceName": "Amazon Kindle Fire HDX 8.9″"
			#"deviceName": "Amazon Kindle Fire (First Generation)"
			#"deviceName": "Apple iPad 1 / 2 / iPad Mini"
			#"deviceName": "Apple iPad 3 / 4"
			#"deviceName": "BlackBerry PlayBook"
			#"deviceName": "Google Nexus 10"
			#"deviceName": "Google Nexus 7 2"
			#"deviceName": "Google Nexus 7"
			#"deviceName": "Motorola Xoom, Xyboard"
			#"deviceName": "Samsung Galaxy Tab 7.7, 8.9, 10.1"
			#"deviceName": "Samsung Galaxy Tab"
			#"deviceName": "Notebook with touch"
			
			# Or specify a specific build using the following two arguments
			#"deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
		    #"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
	}
		
# Define a variable to hold all the configurations we want
chrome_options = webdriver.ChromeOptions()
		
# Add the mobile emulation to the chrome options variable
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
		
# Create driver, pass it the path to the chromedriver file and the special configurations you want to run
#wd = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=chrome_options)
wd = webdriver.Chrome(executable_path='C:\Selenium IE\ChromeDriver\chromedriver.exe', chrome_options=chrome_options)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://bankofamerica.corporateperks.com")
    time.sleep(10)

    # Go to Savings and Rewards 
    #wd.get("http://bankofamerica.corporateperks.com/holiday/index/uSource/echom")
    wd.get("http://bankofamerica.corporateperks.com/store/index/shome/1/uSource/echom/type/homepage/guid/94CF1F36-61BD-448B-84C0-173DAEB17B6B")
    time.sleep(8)
    fileName = imgDirName + '/1_Homepage.png'
    takeScreenshot(fileName, wd, 0)

    # Flowers home page
    #wd.get("http://bankofamerica.corporateperks.com/flowers/home")
    wd.get("http://bankofamerica.corporateperks.com/flowers/home/guid/94CF1F36-61BD-448B-84C0-173DAEB17B6B")
    time.sleep(8)
    fileName = imgDirName + '/2_Flowers_Home.png'
    takeScreenshot(fileName, wd, 0)

    # Flowers index page
    #wd.get("http://bankofamerica.corporateperks.com/flowers/home")
    wd.get("http://bankofamerica.corporateperks.com/flowers/index/guid/94CF1F36-61BD-448B-84C0-173DAEB17B6B")
    time.sleep(8)
    fileName = imgDirName + '/3_Flowers_Index.png'
    takeScreenshot(fileName, wd, 0)

    # Vday page
    #wd.get("http://bankofamerica.corporateperks.com/flowers/index")
    wd.get("http://bankofamerica.corporateperks.com/store/index/c/973/type/holidayelectronics/uSource/RDRCAT/guid/94CF1F36-61BD-448B-84C0-173DAEB17B6B")
    time.sleep(8)
    fileName = imgDirName + '/4_Electronics.png'
    takeScreenshot_Chrome(fileName, wd, 1)

    
    # Send email
    emailCase = 1
    strSubject = "BoA Mobile Pages Check"
    strSendTo = 7 # For default
    strEmailText = "Please find attached screenshots for Bank of America on mobile site. \n\n Thanks."
    sendEmail(strSubject, strEmailText, imgDirName, emailCase, strSendTo)


except Exception as e:
	errorMsg = str(e)
	print e
	success = False
	
finally:
    wd.quit()
    if not success:
        strSubject = "Error in Mobile BoA"
        strEmailText = "Error encountered in script for BoA Corp Perks (mobile site) - \n\n" + errorMsg + "\n\n Thanks."
        emailCase = 2 # For failure
        sendEmail(strSubject, strEmailText, imgDirName, emailCase, strSendTo)
        raise Exception("Test failed.")
