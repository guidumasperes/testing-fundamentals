from selenium import webdriver
import random

#Get our browser
driver = webdriver.Firefox()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

#Get our elements
input_a = driver.find_element_by_xpath('//*[@id="sum1"]')
input_b = driver.find_element_by_xpath('//*[@id="sum2"]')

#Generate random numbers
number_a = random.randint(0, 9)
number_b = random.randint(0, 9)

#Input these numbers
input_a.send_keys(number_a)
input_b.send_keys(number_b)

#Grab button
button = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')

#Click to sum
button.click()

#Grab output
output = driver.find_element_by_xpath('//*[@id="displayvalue"]')

#Check for expected output
try:
    assert number_a+number_b is int(output.text)
except AssertionError:
    print("It's not working!!! :(")
    print(f'Sum is {number_a+number_b} and result is {output.text}')
else:
    print("It's working!!! :)")