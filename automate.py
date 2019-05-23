from selenium import webdriver
# import config

# must install ChromeDriver https://sites.google.com/a/chromium.org/chromedriver/downloads
username = input("What is your github username? ")
pw = input("Enter your password to sign in ")
# automate github login
browser = webdriver.Chrome()

browser.get("https://github.com")

# selenium has all different methods to target html fields
signin = browser.find_element_by_link_text("Sign in")
# simulate click
signin.click()

# find input fields
user_input_field = browser.find_element_by_id("login_field")
password_field = browser.find_element_by_id("password")

# simulate key input
user_input_field.send_keys(username)
password_field.send_keys(pw)
password_field.submit()

profile_link = browser.find_element_by_class_name("user-profile-link")
label = profile_link.get_attribute("innterHTML")
# assertion
assert username in label

browser.quit()