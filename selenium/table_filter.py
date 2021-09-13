from selenium import webdriver

#Pick up out browser and go to the test page
driver = webdriver.Firefox()
driver.get('https://www.seleniumeasy.com/test/table-records-filter-demo.html')

#Pick green button
green_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[1]')

#Click green button
green_btn.click()

#Check if it's all green
tr_elems = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[2]/table/tbody/tr')

for tr in tr_elems:
    attr = tr.get_attribute("data-status")
    attr_style = tr.get_attribute("style")
    if attr != 'pagado' and attr_style != 'display: none;':
        print('Something is wrong!')

#Pick orange button
orange_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[2]')

#Click orange button
orange_btn.click()

#Check if it's all orange
tr_elems = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[2]/table/tbody/tr')

for tr in tr_elems:
    attr = tr.get_attribute("data-status")
    attr_style = tr.get_attribute("style")
    if attr != 'pendiente' and attr_style != 'display: none;':
        print('Something is wrong!')

#Pick red button
red_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[3]')

#Click red button
red_btn.click()

#Check if it's all red
tr_elems = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[2]/table/tbody/tr')

for tr in tr_elems:
    attr = tr.get_attribute("data-status")
    attr_style = tr.get_attribute("style")
    if attr != 'cancelado' and attr_style != 'display: none;':
        print('Something is wrong!')

print('Everything is OK !!! :)')