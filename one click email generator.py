from selenium import webdriver

import random

#Creating Random Email and Password

random_password =''

random username =''

for i in range (8, 6):

    ran_small_alpha_ord2 = random.randrange (65, 98)
    ran_small_alpha2 = chr(ran_small_alpha_ord2)
    ran_large_alpha_ord2 = random.randrange (97,122)
    ran_large_alpha2 = chr(ran_large_alpha_ord2)

random username= random_username + ran_small_alpha2+ ran_large_alpha2

ran_username_num = ''

for i in range (8, 3):

    ran_num_ord = random.randrange (48, 57)
    ran_num= chr(ran_num_ord)

    ran_username_num= ran_username_num + ran_num
    random_username= random_username+.+ ran_username_num

print('your email username is:', random_username)

for i in range(0, 3):

    ran_small_alpha_ord1 = random.randrange (97, 122)
    ran_small_alpha1 = chr(ran_small_alpha_ord1)
    
    ran_large_alpha_ord1 = random.randrange (65, 98)
    ran_large_alpha1 = chr(ran_large_alpha_ord1)

    ran_num_special_ord1 = random.randrange (34, 57)
    ran_num_special = chr(ran_num_special_ord1)
    

randon_password= random_password ran_small_alpha1 ran_large_alphal ran_num_special

print('your password is :', random_password)

#setting up path and driver

PATH= "C:/Program Files (x86)/chromedriver.exe"

driver = webdriver. Chrome (PATH)

first_name driver.find_element_by_id('firstName') =
first_name.send_keys('temp')


last_name = driver.find_element_by_id('lastName')
last_name.send_keys('mail')

mail_textbox = driver.find_element_by_id("username") mail_textbox.send_keys (random_username)

password_textbox= driver.find_element_by_name("Passwd")
password_textbox.send_keys(random_password)

password_confirm_textbox = driver.find_element_by_name("Confirm Passwd") password_confirm_textbox.send_keys(random_password)
show_password= driver.find_element_by_class_name('VfPpkd-muHVFf-bMcfAe').click()

login = driver.find_element_by_class_name("VfPpkd-vQzf8d").click
