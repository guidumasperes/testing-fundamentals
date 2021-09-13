from selenium import webdriver

#Get gecko driver(our browser)
driver = webdriver.Firefox()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html') #Go to our testing page

#Find input element by xpath
input_elem = driver.find_element_by_xpath('//*[@id="user-message"]')

#Input some text
input_elem.send_keys('Hello World!')

#Find button element by xpath
button_elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')

#Click on button
button_elem.click()

#Get outputed text
inner_text = driver.find_element_by_xpath('//*[@id="display"]')

#Compare to see if it's ok
try:
    assert 'Hellow World!' == inner_text.text
except AssertionError:
    print('Ops, something is wrong :(')
