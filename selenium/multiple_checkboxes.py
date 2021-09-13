from selenium import webdriver

#Get driver and go to the page
driver = webdriver.Firefox()
driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')

#Find button to check all checkboxes
button_elem = driver.find_element_by_xpath('//*[@id="check1"]')

#Click on the button
button_elem.click()

#Find all divs that contain our wanted checkboxes
checkboxes = driver.find_elements_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div')

#Loop through then grabbing checkboxes and checking if they are all checked and putting result in an array
result = []
for checkbox in checkboxes:
    input = checkbox.find_element_by_tag_name('input')
    result.append(input.is_selected())

try:
    assert all(result)
except AssertionError:
    print('Something went wrong, not all checkboxes are selected :-(')
else:
    print('Everything looks fine :)')