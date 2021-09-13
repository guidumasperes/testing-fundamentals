from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')

checkbox_elem = driver.find_element_by_xpath('//*[@id="isAgeSelected"]')

checkbox_elem.click()

output_elem = driver.find_element_by_xpath('//*[@id="txtAge"]')

try:
    assert output_elem.text == 'Success - Check box is checked'
except AssertionError:
    print('Ops, something went wrong :(')
else:
    print('Everything went well, neat! :)')