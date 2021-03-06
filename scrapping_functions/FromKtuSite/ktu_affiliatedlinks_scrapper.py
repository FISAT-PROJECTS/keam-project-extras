from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from affiliated_links import affiliated_links
import time as t
from ktu_scrapper import select_combobox_x

year={
        '-Select-': 0 ,
        2021: 0 ,
        2020: 1 ,
        2019: 2 ,
        2018: 3 ,
        2017: 4 ,
        2016: 5 ,
        2015: 6 ,
}

csv_files = [
	'2020.csv',
	'2019.csv', 
	'2018.csv', 
	'2017.csv', 
	'2016.csv', 
	'2015.csv', 
] 


def clear_csv(file):
	with open(file,'w') as f:
		f.write('')


def write_to_csv(data,file):
	with open(file,'a') as f:
		for i in data:
			f.write(",".join(i))
			f.write("\n")


# scrape a single affiliated link
def automated_choose(driver):	
	table_rowdata, rows, row = [], [], []

	#1
	collage_name = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/table/tbody/tr/td/span[1]/h4")[0].text
	print(' - select complete')

	#3
	table_data = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/form/h4/select")
	print(' - select complete')
	select_combobox_x(table_data,year[int(csv[:4])])

	#4
	table_data = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/table/tbody/tr/td")
	print(' - select complete')
	for i in table_data:
		if type(i) != list:
			table_rowdata.append(i.text)
	for i,r in enumerate(table_rowdata):
		row.append(r)
		if i%8==7:
			row.append(collage_name)
			rows.append(row)
			row=[]
	# print(rows)
	write_to_csv(rows,csv)


# main
def ktu_affiliated(csv):
	print('run this file only after running ktu scrapper')
	try:
		driver =  webdriver.Edge("msedgedriver.exe")

		#2
		headings = ['Program Category', 'Program Name', 'Degree', 'Program Type', 'Sanctioned Intake', 'Actual Intake', 'NRI', 'PIO', 'clg_name']
		# for i in csv_files:
		with open(csv,'w') as f:
			f.write(",".join(headings))
			f.write("\n")

		for i in affiliated_links:
			driver.get(i)

			automated_choose(driver)
		
		driver.implicitly_wait(5)

	except Exception as e:
		print("\n\terr: \n",e)
	finally:
		driver.close()

for csv in csv_files:
	print(csv)
	ktu_affiliated(csv)


# to query headings
	#2
	# table_heading = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/th")
	# print(' - select complete')
	# for i in table_heading:
	# 	if type(i) != list:
	# 		headings.append(i.text)
	# 	print()
	# print(headings)