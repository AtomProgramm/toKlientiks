import time  #for wait of loading
from selenium import webdriver 



# ----system settings-----
driverBrowserExecutablePath = "C:/chromedriver.exe"

#-site and account data-
urlRootWebPage="https://klientiks.ru/"
urlLoginPage="https://klientiks.ru/login"
accountPassword = "992927" 
accountLogin = "9213582436" #for login using phone number
phoneCountry = "RU" #to select phone countr (pattern of number)



#> get driver and open sing in page
driver = webdriver.Chrome(driverBrowserExecutablePath)
driver.get(urlLoginPage); #Open sing in page
time.sleep(6) # wait load page

#> sing in
idElementLogin = "label-phone"
elementLoginInput = driver.find_element_by_id(idElementLogin)
elementLoginInput.click()
elementLoginInput.send_keys(accountLogin)
print("Typed login")
idElementPhoneCountry = "label-autocompleteCountry"
elementInputPhoneCountry = driver.find_element_by_id(idElementPhoneCountry)
elementInputPhoneCountry.send_keys(phoneCountry)
print("Typed phone phone country")
idElementPassword = "label-password"
elementPasswordInput = driver.find_element_by_id(idElementPassword)
elementPasswordInput.send_keys(accountPassword)
print("Typed password")
xpatchElementButtonSubmitSingIn = "/html/body/div[3]/div[2]/div/div[4]/div/div/div[1]/div[1]/div[2]/form/div[5]/div/div[2]/button"
elementSingInButton = driver.find_element_by_xpath(xpatchElementButtonSubmitSingIn)
elementSingInButton.click()
print("Click button sing in")

time.sleep(15) #Let see something
driver.quit()



# Создать на нашем сайте пустой аккаунт, в качестве имени при регистрации нужно указать "Тестовое задание"
# Добавить 50 клиентов с различными датами рождения с 01.01.1970 по 31.12.2000.
# У клиентов должен быть указан код. У первого из клиентов - равен 1, у второго - 2, у последующих - сумме кодов двух предыдущих клиентов.
# Клиентам, которым сейчас > 30 лет, предоставляется скидка на все услуги 7%; клиентам, которым сейчас от 20 до 30 лет, предоставляется скидка на все услуги 5%; клиентам, которым сейчас до 20 лет, предоставляется скидка на все услуги 3%
# Стоимость услуг в компании > 1100 рублей
# Скидка предоставляется только на первый визит, дальше всем предоставляется скидка 10%
# В качестве результата предоставьте логин и пароль доступа в аккаунт, где задание выполнено.
# С уважением,
# Клиентикс CRM