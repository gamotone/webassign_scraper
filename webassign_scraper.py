#!/usr/bin/python3

import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


#########
# setup #
#########


# create a text file
# type your username on the first line 
# password on the second line
# phone number in '5551234567' format with quotes on third line
# api key on fourth line

with open('/home/deeb/scraper/creds.txt') as f:
    user = f.readline().strip()
    pw = f.readline().strip()
    phone = f.readline().strip()
    key = f.readline().strip()

# runs headless firefox in the background
# comment this section out during first run to watch selenium run through
options = Options()
options.add_argument('-headless')
browser = webdriver.Firefox(options=options)



#########################
# traversing first page #
#########################



# uncomment the line below during first run to watch selenium
# browser = webdriver.Firefox()
browser.get('https://www.webassign.net/wa-auth/login')
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("cengagePassword")
username.send_keys(user)
password.send_keys(pw)
submitButton = browser.find_element_by_name("Login") 
submitButton.click()



###############
# second page #
###############



# uncomment section below if there is a server warning message
# browser.get('https://www.cengage.com/dashboard/#/my-dashboard/authenticated')
# continueButton = browser.find_element_by_class_name('close')
# continueButton.click()
browser.get('https://www.cengage.com/dashboard/#/login')
username = browser.find_element_by_id("emailId")
password = browser.find_element_by_id("password")
username.send_keys(user)
password.send_keys(pw)
anotherButton = browser.find_element_by_xpath("//button[@value='Sign In']")
anotherButton.click()



##############
# third page #
##############



# uncomment if server warning is present
# browser.get(
# 	'https://www.cengage.com/dashboard/#/my-dashboard/authenticated?page=')
wait = WebDriverWait(browser, 10)
original_window = browser.current_window_handle
assert len(browser.window_handles) == 1

# change the text()="" to your course name and number
# locate element <a class="courseTitleLink ng-binding">use-this-text-here</a>
wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//a[text()="Math 123 1234"]'))).click()



##############
# final page #
##############



# switches focus to the new tab cengage opens
wait.until(EC.number_of_windows_to_be(2))
for window_handle in browser.window_handles:
    if window_handle != original_window:
        browser.switch_to.window(window_handle)
        break

# delays until 'grades' element loads
wait.until(EC.presence_of_element_located((By.ID, 'js-student-home-grades')))

# assigns inner HTML text of the 'grades' element to a variable
grade_check = browser.find_element_by_xpath(
    "//div[@id='js-student-home-grades']").text

# converts inner HTML text to a string
grade = str(grade_check)

# if this is the first time running this script a reference file will be made
# on subsequent runs of this script the ref.txt file will not be overwritten
if os.path.isfile('./ref.txt'):
    pass
else:
    with open('ref.txt', 'w') as g:
        g.write(grade)



###############
# quick tests #
###############



# quick and dirty check to see if it scraped the correct string
# print(grade + "\n")

# compares newly scraped grade to the reference file
# print("grades updated!" if grade != open('ref.txt').read() else "no change")

# this api will send a generic sms if your grade has been updated
# you only get one freebie
#
# requests.post('https://textbelt.com/text', {
#   'phone': '5551234567',
#   'message': 'Hello world',
#   'key': 'textbelt',
# })

# request is as follows with custom message
# custom sms messages can be purchased on website
# key variable needs api-key
if grade != open('ref.txt').read():
    requests.post('https://textbelt.com/text', {
        'phone': phone,
        'message': 'New WebAssign Data!' + grade,
	'key': key,
    })
else:
    pass

browser.quit()
