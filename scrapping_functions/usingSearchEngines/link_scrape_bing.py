from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t
from pprint import pprint as pp
import pandas as pd

bing = "https://www.bing.com"

def search_bing(text,driver):
	input_bing_main = driver.find_elements(By.XPATH,"/html/body/header/form/div/input[1]")
	print("--select complect")
	input_bing_main[0].clear()
	input_bing_main[0].send_keys(text)
	input_bing_main[0].send_keys(Keys.RETURN)
	link = driver.find_elements(By.XPATH,"//li[@class='b_algo']/h2/a")#.text
	print("--select")
	with open("output.csv",'a') as f:
		# print(link,type(link))
		if len(link)>0:
			f.write(link[0].get_attribute("href"))
			f.write('\n')
		else:
			f.write('\n')


# main
def link_scrap_bing(csv="final_data.csv"):
	try:
		driver =  webdriver.Edge("msedgedriver.exe")
		with open("output.csv",'w') as f:
			f.write('\n')

		df = pd.read_csv(csv)
		college_names = list(df['Institution Name'])
		# driver.get("https://www.bing.com/search?q=input+a+text+usnig+selenium+in+python+w3c&qs=n&form=QBRE&sp=-1&pq=input+a+text+usnig+selenium+in+p+w3c&sc=0-36&sk=&cvid=3D693DD342DE4396BFA6399B4A0F95AD")
		driver.get(bing)
		input_bing_main = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/form/input[1]")
		print("--select complect")
		# print(input_bing_main,input_bing_main[0],type(input_bing_main[0]))
		input_bing_main[0].send_keys("text")
		input_bing_main[0].send_keys(Keys.RETURN)

		for i in college_names:
			search_bing(i[1:-2]+" website",driver)
		
		driver.implicitly_wait(5)

	except Exception as e:
		print("\n\terr: \n",e)
	finally:
		driver.close()

link_scrap_bing()
