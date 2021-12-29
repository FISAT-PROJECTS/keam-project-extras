from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t
from pprint import pprint as pp

# number as per the dropdown in the site
district = {
	'All' 					: 0 ,
	'THIRUVANANTHAPURAM'	: 1 ,
	'KOLLAM' 				: 2 ,
	'PATHANAMTHITTA' 		: 3 ,
	'ALAPPUZHA' 			: 4 ,
	'KOTTAYAM' 				: 5 ,
	'IDUKKI' 				: 6 ,
	'ERNAKULAM' 			: 7 ,
	'THRISSUR' 				: 8 ,
	'PALAKKAD' 				: 9 ,
	'MALAPPURAM' 			: 10 ,
	'KOZHIKODE' 			: 11 ,
	'WAYANAD' 				: 12 ,
	'KANNUR' 				: 13 ,
	'KASARAGOD' 			: 14 ,
	'Other' 				: 15 ,
}

year = {
	2021: 0,
	2020: 1,
	2019: 2,
	2018: 3,
	2017: 4,
	2016: 5,
	2015: 6
}

degree = {
	'UG' : 1,
	'PG' : 2,
}

program = {
	'All' 			: 0 ,
	'B.Tech' 		: 1 ,
	'B.Arch' 		: 2 ,
	'Hotel' 		: 3 ,
	'Management' 	: 4 ,
	'and' 			: 5 ,
	'Catering' 		: 6 ,
	'Technology' 	: 7 ,
	'B.Des' 		: 8 ,
}

files = [
	 'THIRUVANANTHAPURAM.csv',
	 'KOLLAM.csv',
	 'PATHANAMTHITTA.csv',
	 'ALAPPUZHA.csv',
	 'KOTTAYAM.csv',
	 'IDUKKI.csv',
	 'ERNAKULAM.csv',
	 'THRISSUR.csv',
	 'PALAKKAD.csv',
	 'MALAPPURAM.csv',
	 'KOZHIKODE.csv',
	 'WAYANAD.csv',
	 'KANNUR.csv',
	 'KASARAGOD.csv',
 ]


# to select the item in the dropdown (in site)
def select_combobox_x(driver,dropdown_val):
	driver[0].click()
	driver[0].send_keys(Keys.ARROW_DOWN*dropdown_val)
	driver[0].send_keys(Keys.RETURN)
	# t.sleep(5)

def automated_choose(driver,csv):	
	#1
	select_yr = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/form/div/div[1]/span[1]/select")
	print(' - select complete')
	checklist(select_yr)
	select_combobox_x(select_yr, year[2020])

	#2
	select_dis = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/form/div/div[1]/span[2]/select")
	print(' - select complete')
	checklist(select_dis)
	# select_combobox_x(select_dis, district['ERNAKULAM'])
	select_combobox_x(select_dis, district[csv[:-4]])

	#3
	select_deg = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/form/div/div[2]/span[1]/select")
	print(' - select complete')
	checklist(select_deg)
	select_combobox_x(select_deg, degree['UG'])

	# #4
	# select_prog = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/form/div/div[2]/span[2]/select")
	# print(' - select complete')
	# checklist(select_prog)
	# select_combobox_x(select_prog, program['B.Tech'])



# to iterate the selenium_scraped_element 
def checklist_x(driver):
	if type(driver) == list:
		for i in driver:
			if type(i) != list:
				print(i.text.split('\n'))
			print()
			
# to get affiliated links for further scrapping
def get_affiliated_links(driver,csv):
	print(csv)


	tr = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/table/tbody/tr")
	print(' - select complete')
	collage_details = []
	if type(tr) == list:
		for i in tr[1:]:
			detail = i.text.split('\n')				#removing text=affiliated links
			collage_details.append(detail[:3]+detail[4:])

	# a = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/table/tbody/tr/td[1]/span/a")
	# print(' - select complete')
	# affiliated_links =[]
	# if type(a) == list:
	# 	for i in a:
	# 		affiliated_links.append(i.get_attribute("href"))

	with open(csv,'a') as f:
		for i in collage_details:
			f.write(";".join(i))
			f.write("\n")

	# pp(collage_details)

# main
def ktu_scrapper(csv):
	try:
		driver =  webdriver.Edge("msedgedriver.exe")
		driver.get('https://ktu.edu.in/eu/afn/affiliationInstitutes.htm')
		
		automated_choose(driver,csv)

		get_affiliated_links(driver,csv)
		driver.implicitly_wait(5)

	except Exception as e:
		print("\n\terr: \n",e)
	finally:
		driver.close()

for csv in files:
	headings = ['Collage_name', 'AICTE ID', 'Type', 'Postal Address', 'mail id', 'site']
	with open(csv,'w') as f:
		f.write(';'.join(headings))
		f.write('\n')
	ktu_scrapper(csv)

# from affiliated_links import affiliated_links
# print(affiliated_links)	