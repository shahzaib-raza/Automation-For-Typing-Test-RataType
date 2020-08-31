import selenium
from selenium.webdriver.common.keys import Keys
import time

dpath = input('Enter path of driver: ')
email = input('Enter the login Email of Ratatype: ')
paswd = input('Enter the password of Ratatype: ')
print('For 40 wpm speed enter time of delay 0.27 sec')
t = float(input('Enter time delay: '))

driver = selenium.webdriver.Chrome(executable_path=dpath)
driver.get('https://www.ratatype.com/typing-test/')
time.sleep(2)

log = driver.find_element_by_xpath('/html/body/header/div/nav/div[2]/ul[2]/li/a[1]')
log.click()
mail = driver.find_element_by_id('email')
mail.send_keys(email)
password = driver.find_element_by_id(paswd)
password.send_keys('austin881')
driver.find_element_by_xpath('/html/body/section/div/div/div/div/form/div[3]/button').click()

time.sleep(2)

driver.find_element_by_xpath('/html/body/div[2]/nav/ul/li[3]/a').click()

time.sleep(2)

button = driver.find_element_by_xpath('/html/body/section/div[1]/div/div/div/div/a')
button.click()
time.sleep(2)
start = driver.find_element_by_id('startButton')
start.click()
main_text = driver.find_element_by_class_name('mainTxt').text
print(main_text)
send = driver.find_element_by_id('certificateInput')
for word in main_text:
    for letter in word:
        send.send_keys(letter)
        time.sleep(t)

