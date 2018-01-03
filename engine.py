#-----------------------------------------------------------------------------------------------------------------------------
#|	When you use this program please run run.py file. 																		  |
#|	This is the core of this program, so I name it 'engine'. 																  |
#|	All data catch, url request, and data analysis have been achieved in this python file.									  |
#|	The use of this code follows the Mozilla Public License Version 2.0, for detail: https://www.mozilla.org/en-US/MPL/2.0/   |
#|----------------------------------------------------------------------------------------------------------------------------|
# -*- coding: utf-8 -*-
import config
import ErrorHandling
import requests
import re
from datetime import datetime
from datetime import timedelta

def urlReq(flag,lot_id) :
	#Method urlReq: 
	#Usage: Get response from URL request, if the artnet.com is not accessiable, the program would try at maxium four times until the artnet.com response to the URL request. 
	#Return ''(empty) if artnet.com is not accessiable for three times
	#Normally, the method would return the certain lot's html source page, and the method has already delete all the wrap and the space between all the html lable. 
	#For the first parameter, please put 0. 
	#For the second parameter, please input the lot's ID. 
	if flag > 3 :
		ErrorHandling.errorOutput(lot_id,'Network Connection Error','Cannot Connect to artnet.com',2)
		return ''
	else :
		try :
			web = requests.get("https://www.artnet.com/auctions/Pages/Lots/" + str(lot_id) + ".aspx").text
			web_data = re.sub(r'[\r]+[\n]+[\s]+','',web)
			web_data = web_data.replace('\r','').replace('\n','').replace('\t','')
			return web_data
		except requests.exceptions.ConnectionError :
			ErrorHandling.errorOutput(lot_id,'Network Connection Error','Cannot Connect to artnet.com',1)
			return urlReq(flag + 1,lot_id)

def isLotExisted (web_data) :
	#Method isLotExisted: 
	#Usage: Chect if there is a lot's information existed in a certain lot's ID
	#Only one parameter required, and this parameter is the lot's html source page, which you can get it from method urlReq()
	#Return 1 means that there is a lot's information existed in this page. 
	#Return 0 means there is no a lot's information in this page. 
	if re.search('serverViewData.LotBiddingInfo',web_data) :
		return 1
	else :
		return 0
			

#----------------------------------------------------------------------------------------------
#Before you call all the following method, please call the method aboved (urlReq and isLotExisted), because you have to get the lot's html source page and chect if a lot's information existed before extract the data from the page. 
#All the data analysis and data extractions from lot's html source page are achieved by regular expression
#----------------------------------------------------------------------------------------------
			
def getAuthorname (web_data,lot_id) :
	#Method getAuthorname:
	#Usage: Get the artist's Name for this lot. 
	#Two parameter, the first parameter is the lot's html source page
	#The second parameter is the lot's ID (Why it needs that? Because if there is an error happened, the lot's ID would print into the error log file). 
	#Normally, the method would return the artist's name in string type
	#If there is an error happened, it would return ''(empty). 
	try :
		return re.findall('serverViewData\.ArtistFullName = \"(.*?)\"',web_data)[0]
	except Exception,e :
		ErrorHandling.errorOutput(lot_id,'Catch Artest\' Name Failed',repr(e),3)
		return ''
	
def getArtestDetail (web_data,lot_id) :
	#Method getArtestDetail: 
	#Usage: Get artist's nationality, artist's birth year, and artist's death year from lot's html source page. 
	#Two parameter, the first parameter is the lot's html source page
	#The second parameter is the lot's ID (Why it needs that? Because if there is an error happened, the lot's ID would print into the error log file). 
	#Normally, the method would return a list with three element. 
	#The first element is the artist's nationality with string type. 
	#The second element is the artist's birth year with integer type. 
	#The third element is the artist's death year with integer type. 
	#If the method cannot found the artist's nation in html source page, the first element would be 'Unknown'
	#If the method cannot found the artist's birth or death year, the second or the third element would be 0. 
	#If there is an error happened in this method, it would return ['']. 
	try :
		artest_detail = re.findall('<div class=\"artist-details\">(.*?)</div>',web_data)[0]
		artest_race = 'Unknown'
		artest_birth = 0
		artest_death = 0
		if re.search(',', artest_detail) :
			artest_detail_ = artest_detail.split(',')
			artest_race = artest_detail_[0]
			if re.search('b.', artest_detail_[1]) :
				artest_birth = int(re.findall('.*?([0-9]{4})',artest_detail_[1])[0])
			else : 
				artest_date = re.findall('([0-9]{4}).*?([0-9]{4})',artest_detail_[1])[0]
				artest_birth = int(artest_date[0])
				artest_death = int(artest_date[1])
		else :
			if re.search('[0-9]',artest_detail) :
				if re.search('b.', artest_detail) :
					artest_birth = int(re.findall('.*?([0-9]{4})',artest_detail)[0])
				else : 
					artest_date = re.findall('([0-9]{4}).*?([0-9]{4})',artest_detail)[0]
					artest_birth = int(artest_date[0])
					artest_death = int(artest_date[1])
			else :
				artest_race = artest_detail
		return [artest_race,artest_birth,artest_death]
	except Exception,e :
		ErrorHandling.errorOutput(lot_id,'Catch Artest\' Detail Failed',repr(e),3)
		return ['']

def getLotName(web_data,lot_id) :
	#Method getLotName:
	#Usage: Get the lot's name/title. 
	#Two parameter, the first parameter is the lot's html source page
	#The second parameter is the lot's ID (Why it needs that? Because if there is an error happened, the lot's ID would print into the error log file). 
	#Normally, the method would return the lot's name/title in string type
	#If there is an error happened, it would return ''(empty). 
	try :
		return re.findall('<h3 class=\"lot-name\"><i>(.*?)</i>',web_data)[0]
	except Exception,e :
		ErrorHandling.errorOutput(lot_id,'Catch Lot\' Name Failed',repr(e),3)
		return ''
		
def getLotYear(web_data,lot_id) :
	#Method getLotYear:
	#Usage: Get the lot's creation year. 
	#Two parameter, the first parameter is the lot's html source page
	#The second parameter is the lot's ID (Why it needs that? Because if there is an error happened, the lot's ID would print into the error log file). 
	#Normally, the method would return the lot's creation year in integer type
	#If there is an error happened, it would return 0. 
	try :
		lot_year_place = re.findall('<h3 class=\"lot-name\"><i>.*?</i>(.*?)</h3>',web_data)[0]
		lot_year = 0
		if re.search('[0-9]',lot_year_place) :
			lot_year = int(re.findall('([0-9]{4})',lot_year_place)[0])
		return lot_year
	except Exception,e :
		ErrorHandling.errorOutput(lot_id,'Catch the year of creation Failed',repr(e),3)
		return 0
		
def getLotInfo(web_data,lot_id) :
	#Method getLotInfo:
	#Usage: Get the lot's general information, such as the dimention, color, size, and texture. 
	#Two parameter, the first parameter is the lot's html source page
	#The second parameter is the lot's ID (Why it needs that? Because if there is an error happened, the lot's ID would print into the error log file). 
	#Normally, the method would return the lot's general information in string type
	#If there is an error happened, it would return ''(empty). 
	try :
		return re.findall('<div class=\"lot-info\"><p class=\"description\">(.*?)</p>',web_data)[0]
	except Exception,e :
		ErrorHandling.errorOutput(lot_id,'Catch Lot\' information Failed',repr(e),3)
		return ''
		
def getLotInfoAddi(web_data,lot_id) :
	#Method getLotInfoAddi:
	#Usage: Get the lot's additional information, the extention of lot's general information for this lot. 
	#Two parameter, the first parameter is the lot's html source page
	#The second parameter is the lot's ID (Why it needs that? Because if there is an error happened, the lot's ID would print into the error log file). 
	#Normally, the method would return the lot's additional information in string type
	#If there is an error happened, it would return ''(empty). 
	try :
		return re.findall('<p>(.*?)</p><div class=\"lot-id\">',web_data)[0]
	except Exception,e :
		ErrorHandling.errorOutput(lot_id,'Catch Lot\' additional information Failed',repr(e),3)
		return ''
		
def getLotDesc(web_data,lot_id) :
	#Method getLotDesc:
	#Usage: Get the lot's artistic description. 
	#Two parameter, the first parameter is the lot's html source page
	#The second parameter is the lot's ID (Why it needs that? Because if there is an error happened, the lot's ID would print into the error log file). 
	#Normally, the method would return the lot's artistic description in string type
	#If there is an error happened, it would return ''(empty). 
	try :
		return re.findall('<div id=\"lotDescriptionWraper\"><p>(.*?)</p></div>',web_data)[0]
	except Exception,e :
		ErrorHandling.errorOutput(lot_id,'Catch Lot\' description Failed',repr(e),3)
		return ''
		
def getLotProv(web_data,lot_id) :
	#Method getLotProv:
	#Usage: Get the lot's provenance. 
	#Two parameter, the first parameter is the lot's html source page
	#The second parameter is the lot's ID (Why it needs that? Because if there is an error happened, the lot's ID would print into the error log file). 
	#Normally, the method would return the lot's provenance information in string type
	#If there is an error happened or there is no provenance information, it would return ''(empty). 
	try :
		lot_provenance = '';
		if re.search('lot-history-text',web_data) :
			lot_provenance = re.findall('<ul class=\"lot-history-text\">(.*?)</ul>',web_data)[0]
			lot_provenance = re.sub('</li>','<br>',lot_provenance)
			lot_provenance = re.sub('<li>','',lot_provenance)
		return lot_provenance
	except Exception,e :
		ErrorHandling.errorOutput(lot_id,'Catch Lot\' provenance Failed',repr(e),3)
		return ''

def getEst(web_data,lot_id) :
	#Method getEst: 
	#Usage: Get lot's estimated price from lot's html source page. 
	#Two parameter, the first parameter is the lot's html source page
	#The second parameter is the lot's ID (Why it needs that? Because if there is an error happened, the lot's ID would print into the error log file). 
	#Normally, the method would return a list with two element. There is a lower bound of estimation and upper bound of estimation. 
	#The first element is the lower bound of the estimation price with integer type. 
	#The second element is the upper bound of the estimation price with integer type. 
	#If there is an error happened in this method, it would return ['']. 
	try :
		est = re.findall('\"Estimate\":\"(.*?) USD\"',web_data)[0]
		est = est.replace(',','')
		est_low = int(re.findall('([0-9]+).*?[0-9]+',est)[0])
		est_up = int(re.findall('[0-9]+.*?([0-9]+)',est)[0])
		return [est_low,est_up]
	except Exception,e :
		ErrorHandling.errorOutput(lot_id,'Catch Lot\' estimate values Failed',repr(e),3)
		return ['']

def getBidNum(web_data,lot_id) :
	#Method getBidNum:
	#Usage: Get the lot's bid number (how many bid for this lot). 
	#Two parameter, the first parameter is the lot's html source page
	#The second parameter is the lot's ID (Why it needs that? Because if there is an error happened, the lot's ID would print into the error log file). 
	#Normally, the method would return the lot's bid number in integer type
	#If there is an error happened, it would return 0. 
	try :
		return int(re.findall('\"NumberOfBids\":([0-9]+),',web_data)[0])
	except Exception,e :
		ErrorHandling.errorOutput(lot_id,'Catch Bidding Number Failed',repr(e),3)
		return 0
		
def getDealPrice(web_data,lot_id) :
	#Method getDealPrice:
	#Usage: Get the lot's final price (if the bidding is not complete, this method would get the last bid price). 
	#Two parameter, the first parameter is the lot's html source page
	#The second parameter is the lot's ID (Why it needs that? Because if there is an error happened, the lot's ID would print into the error log file). 
	#Normally, the method would return the lot's final price (for last bid) in integer type
	#If there is an error happened, it would return 0. 
	try :
		return int(re.findall('\"CurrentPrice\":([0-9]+).*?,',web_data)[0])
	except Exception,e :
		ErrorHandling.errorOutput(lot_id,'Catch deal price Failed',repr(e),3)
		return 0

def getSoldDate(web_data,lot_id) :
	#Method getSoldDate: 
	#Usage: Get lot's sell/sold date from lot's html source page, also it can get the information about the lot has been sold or still biding. 
	#Two parameter, the first parameter is the lot's html source page
	#The second parameter is the lot's ID (Why it needs that? Because if there is an error happened, the lot's ID would print into the error log file). 
	#Normally, the method would return a list with two element. 
	#The first element is index about the item has been sold or not with integer type. 
	#If the first element equals 0, means that the item has not been sold yet. 
	#If the first element equals 1, means that the item has already been sold. 
	#The second element is the date that the item would/will be sold, and the data type is datetime object.  
	#The timezone is your local time zone. 
	#If there is an error happened in this method, it would return ['']. 
	try :
		bid_day_remain = re.findall('\"Days\":(.*?),',web_data)[0]
		days_num = 0
		lot_sold = 0
		lot_sell_date = datetime.now()
		if re.match('-',bid_day_remain) :
			lot_sold = 1
			days_num = int(re.findall('.*?([0-9]+)',bid_day_remain)[0])
			lot_sell_date = lot_sell_date - timedelta( days = days_num )
		else : 
			days_num = int(bid_day_remain)
			lot_sell_date = lot_sell_date + timedelta( days = days_num)	
		return [lot_sold,lot_sell_date]
	except Exception,e :
		ErrorHandling.errorOutput(lot_id,'Catch sold date Failed',repr(e),3)
		return ['']

