from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

duck = "https://duckduckgo.com/"

dis ={
	'THIRUVANANTHAPURAM',
	'KOLLAM' 			,
	'PATHANAMTHITTA' 	,
	'ALAPPUZHA' 		,
	'KOTTAYAM' 			,
	'IDUKKI' 			,
	'ERNAKULAM' 		,
	'THRISSUR' 			,
	'PALAKKAD' 			,
	'MALAPPURAM' 		,
	'KOZHIKODE' 		,
	'WAYANAD' 			,
	'KANNUR' 			,
	'KASARAGOD' 		,
}


def search_duck(text,driver,n):
	input_duck_main = driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[1]/div/form/input[1]")
	print("--select complect")
	input_duck_main[0].clear()
	input_duck_main[0].send_keys(f'{text} district in kerala')
	input_duck_main[0].send_keys(Keys.RETURN)
	
	label = driver.find_elements(By.XPATH,"//span[@class='about-info-box__info-label']");
	value = driver.find_elements(By.XPATH,"//span[@class='about-info-box__info-value']");
	flag=0;
	district=''
	for i in range(len(label)):
		if label[i].text.strip() == 'District:':
			flag=1;
			district = value[i].text.strip()
			print(district)

	print("--select")
	with open("output.csv",'a') as f:
		if flag==1:
			f.write(f'{district},{n}')
			f.write('\n')
		else:
			f.write('\n')


# main
def link_scrap_duck(csv="final_data.csv"):
	try:
		driver =  webdriver.Edge("msedgedriver.exe")
		driver.maximize_window()
		with open("output.csv",'w') as f:
			f.write('\n')

		driver.get(duck)
		input_duck_main = driver.find_elements(By.XPATH,"/html/body/div/div[2]/div/div[1]/div[2]/form/input[1]")
		print("--select complect")
		# print(input_duck_main,input_duck_main[0],type(input_duck_main[0]))
		input_duck_main[0].send_keys("text")
		input_duck_main[0].send_keys(Keys.RETURN)

		df = pd.read_csv("final_data.csv")
		colleges = list(df['Institution Name'])
		places = []
		for i in range(len(colleges)):
			places.append(colleges[i].split(',')[-1].strip().strip('.'))


		for i in range(len(places)):
			print(places[i])
			if places[i]=='':
				with open("output.csv",'a') as f:
					f.write('\n')

			elif places[i].upper() in dis:
				with open("output.csv",'a') as f:
					f.write(places[i]+','+str(i))
					f.write('\n')
					
			else:
				search_duck(places[i],driver,i)

		driver.implicitly_wait(5)

	except Exception as e:
		print("\n\terr: \n",e)
	finally:
		driver.close()

link_scrap_duck()
