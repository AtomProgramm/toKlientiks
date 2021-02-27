import time  #for wait of loading
import datetime #for birth of client manipulation
from selenium import webdriver 
import random

# ----system settings-----
driverBrowserExecutablePath = "C:/chromedriver.exe"
secondsToWaitLoadelementOnPage = 1
secondsToWaitLoadPage = 10

#-site and account data-
urlRootWebPage="https://klientiks.ru/"
urlLoginPage="https://klientiks.ru/login"
accountPassword = "992927" 
accountLogin = "9213582436" #for login using phone number
phoneCountry = "RU" #to select phone countr (pattern of number)
birthFirstClient = datetime.datetime(1970, 1, 1)
birthLastClient =  datetime.datetime(2000, 12, 31)
countClient = 50
startCodeClient = 1



#> get driver and open sing in page
driver = webdriver.Chrome(driverBrowserExecutablePath)
driver.get(urlLoginPage); #Open sing in page
time.sleep(secondsToWaitLoadPage) # wait load page

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
elementSingInButton.click() # Click button sing in and sing in
print("Clicked button sing in")
time.sleep(secondsToWaitLoadPage) # wait load page

#jump to clients page
xpatchRefClientsPage = '/html/body/div[3]/div[1]/div[1]/div[5]/a'
refClientPage = driver.find_element_by_xpath(xpatchRefClientsPage)
refClientPage.click()
print("Clicked ref clients page")
time.sleep(secondsToWaitLoadPage) # wait load page
handleOfTabOpenedRef =  driver.window_handles[1] # get handle of new tab where opened reference of page client
driver.switch_to.window(handleOfTabOpenedRef) # open this tab

def createClient(name,phNumIn,clientCode,dateBirth,description):
	#input validation
	if type(name) != type(" "):
		raise Exception("name cannot be not string ("+str(name)+")")      
	if type(phNumIn) != type("0"):
		raise Exception("phone number cannot be not str ("+str(clientCode)+")")				 
	if len(phNumIn) != 10:
		raise Exception("phone number cannot be not 10 lenght ("+str(phNumIn)+")")	 
	if type(clientCode) != type(0):
		raise Exception("clientCode cannot be not integer ("+str(clientCode)+")")		 
	if len(dateBirth) != 4:
		raise Exception("date Birth cannot be not 4 lenght ("+str(dateBirth)+")")	 
	#open form to create client
	xpatchRefClientOpenForm = '/html/body/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[4]/div'
	ClientOpenFormBtn = driver.find_element_by_xpath(xpatchRefClientOpenForm)
	ClientOpenFormBtn.click()
	print("Clicked add client form")
	time.sleep(secondsToWaitLoadelementOnPage) # wait load form
	#typing data
	nameInputXpatch="/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/form/div[1]/div[2]/div/input"
	nameInput = driver.find_element_by_xpath(nameInputXpatch)
	nameInput.send_keys(name)
	phNumInputXpatch="/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div[2]/div/input"
	phNumInput = driver.find_element_by_xpath(phNumInputXpatch)
	phNumInput.send_keys(phNumIn)
	codeClInputXpatch="/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/form/div[3]/div[1]/div/input"
	codeClInput = driver.find_element_by_xpath(codeClInputXpatch)
	codeClInput.clear()
	time.sleep(secondsToWaitLoadelementOnPage) # wait load form
	codeClInput.click()
	codeClInput.send_keys(clientCode)
	time.sleep(secondsToWaitLoadelementOnPage) # wait load form
	dateBirthInputXpatch="/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/form/div[7]/div[3]/div/input"
	dateBirthInput = driver.find_element_by_xpath(dateBirthInputXpatch)
	dateBirthInput.send_keys(dateBirth)
	descXpatch="/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/form/div[4]/div[4]/div/textarea"
	desc = driver.find_element_by_xpath(descXpatch)
	desc.send_keys(description)
	#send form create client
	xpatchRefClientAdd = '/html/body/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[1]'
	ClientAddBtn = driver.find_element_by_xpath(xpatchRefClientAdd)
	ClientAddBtn.click()
	print("Clicked add client")
	time.sleep(secondsToWaitLoadelementOnPage) # wait load form

#create clients
clientCodeNow = startCodeClient
birthNow = birthFirstClient
birthStep = (birthFirstClient - birthLastClient)/countClient
clientsCode = []
phoneNumNow = "0000000000"
phoneNumbers = ["0000000000"]

for clientNum in range(countClient):
	#createClient(name,						phNumIn,		clientCode,		dateBirth,	description)
	createClient("client"+str(clientNum),	phoneNumNow,	clientCodeNow, 	birthNow.strftime("%d%m"),	"Client number"+str(clientNum+1)+".")
	while phoneNumNow in phoneNumbers:
		cut = random.randint(0,9)
		phoneNumNow = phoneNumNow[:cut]+str(random.randint(0,9))+phoneNumNow[cut+1:]
	phoneNumbers.append(phoneNumNow)
	clientsCode.append(clientCodeNow)
	if clientCodeNow != 1:
		clientCodeNow = sum(clientsCode[-2:])
	else:
		clientCodeNow = 2
	birthNow = birthNow + birthStep

print("Sucscess! create: " + str(countClient) +" clients. Last code: "+str(clientsCode[-1]))
time.sleep(120)
driver.quit()