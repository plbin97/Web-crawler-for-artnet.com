#-----------------------------------------------------------------------------------------------------------------------------
#|	When you use this program please run this file.                                                                           |
#|	This file is made for execution.                                                                                          |
#|	The use of this code follows the Mozilla Public License Version 2.0, for detail: https://www.mozilla.org/en-US/MPL/2.0/   |
#|----------------------------------------------------------------------------------------------------------------------------|
# -*- coding: utf-8 -*-
import engine
import config
import data
import ErrorHandling
from datetime import datetime
from datetime import timedelta
import MySqlIni

start = config.Search_from	#The lot's ID that the loop would started from 
end = config.Search_to + 1	#The last lot's ID that the loop would stop

#----------------------------------------------------------------------------------------------------------------------
#If you have any costomized code(For expamle, environment check) which should be run before the loop start, please put it here: 
#Cheak the MySql connection if the user plan to use MySql Database
if config.UseMySqlDataBase == 1 :
	if MySqlIni.connTest() :
		#If the user plan to create a table, the program would create a table in database, and the detail of the table in config.MySqlTableExisted. 
		if config.MySqlTableExisted == 0 :
			if MySqlIni.createTable() :
				print 'Table Created Successful'
			else :
				print 'There is an error in while the program is creating the table/nFor Detail, please take a look at error log'
				exit()
	else :
		print 'The program cannot connect to the MySql database/nFor Detail, please take a look at error log'
		exit()
		
#-------------------------------------------------------------------------------------------------------------------------		

#Start the loop for Lot's ID
while (start < end) :
	#In the loop, the variable 'start' is the lot's ID. 
	
	#Check if the web(url) is visitable
	web_data = engine.urlReq(0,start)
	#If the web(url) is visitable, the program would start to analysis the data. If not, the program would abandon this Lot's Data and start to analysis the next lot
	#Variable web_data is the result of url request. 
	if web_data == '' :
		ErrorHandling.logFail(start)
		start = start + 1
		continue
	
	#Chect if the lot is existed. There is some lot's id with empty page. If this lot is an empty page, the program would abandon this Lot's Data and start to analysis the next lot. 
	if not engine.isLotExisted(web_data) :
		ErrorHandling.logNotFound(start)
		start = start + 1
		continue
		
	
	#The program would get all the data we need from web_data variable
	ad = engine.getArtestDetail(web_data,start)
	artest_race = ''
	artest_birth = 0
	artest_death = 0
	if not ad[0] == '' :
		artest_race = ad[0]	#Variable artest_race is the artist's nationality, string type
		artest_birth = ad[1]	#Variable artest_birth is the artist's birth year, 4 digit integer type
		artest_death = ad[2]	#Variable artest_death is the artist's death year, 4 digit integer type
	est_low = 0	#The lower bound of estimated price for this lot
	est_upp = 0	#The upper bound of the estimated price for this 
	est = engine.getEst(web_data,start)
	if not est[0] == '' :
		est_low = est[0]
		est_upp = est[1]
	sold_ = 0	#Variable sold_ represent if the lot has already been sold yet, integer type. value is 1 means that this lot has already been sold; however, value 0 means that this lot has not been sold yet. 
	sold_date = datetime(1900,1,1,1,1,1)	#Variable sold_date is the Data that this lot would/will be sold, datetime objective instance
	sold = engine.getSoldDate(web_data,start)
	if not sold[0] == '' :
		sold_ = sold[0]
		sold_date = sold[1]
	artest = engine.getAuthorname(web_data,start)	#Variable artest is the artist's name of this lot, string type
	lot_name = engine.getLotName(web_data,start)	#Variable lot_name is the name/title of this lot, string type
	lot_year = engine.getLotYear(web_data,start)	#Variable lot_year is the creation year of this lot, 4 digit integer type
	lot_info = engine.getLotInfo(web_data,start)	#Variable lot_info is the gerenal introduction of this lot, string type. This variable inclusive of the dimention, size, material of this lot. 
	lot_info_addi = engine.getLotInfoAddi(web_data,start)	#Variable lot_info_addi is the additional introduction about this lot, string type. 
	lot_desc = engine.getLotDesc(web_data,start)	#Variable lot_desc is the description of this lot, string type. 
	lot_prov = engine.getLotProv(web_data,start)	#Variable lot_prov is the Provenance of this lot, string type. 
	deal_price = engine.getDealPrice(web_data,start)	#Variable deal_price is the final price for this lot, integer type. If the lot is still bidding, the deal_price is the price for last bid. 
	bid_num = engine.getBidNum(web_data,start)	#Variable bid_num is the number of bids for this lot, integer type. 
	
	#Put those values we catched into an object
	data_ = data.dataCatched(start,artest,artest_race,artest_birth,artest_death,lot_name,lot_year,lot_info,lot_info_addi,lot_desc,lot_prov,est_low,est_upp,deal_price,bid_num,sold_,sold_date)
	ErrorHandling.logSuccess(start)
	
	#Reminder: For all variables, if the program cannot catch the specific data from 'web_data'(result of url request), the value of the variable would be ''(empty). Also, if the data type is string and the program cannot catch this data, the value would be 0. For datetime objective instance data, the value would be "datetime(1900,1,1,1,1,1)". 
	#-----------------------------------------------------------------------------
	#Here, you can put your own costomized code to handle those data
	#The program would loop the variable 'start' as lot's ID from the begining to the end
	#The variable you need : start, artest, artest_race, artest_birth, artest_death, lot_name, lot_year, lot_info, lot_info_addi, lot_desc, lot_prov, est_low, est_upp, deal_price, bid_num, sold_, sold_date
	#For how to use those variable, please take a look in above comments
	#Also, you can make your own costomized code in data.py
	#-----------------------------------------------------------------------------
	
	#Handle those data in data.py
	if config.DisplayData == 1 :
		data_.displayData()	#Display the data we catched if needed. 
	if config.PrintThemInToFile == 1 :
		data_.printData()	#Print the data we catched in to file if needed. 
	if config.UseMySqlDataBase == 1 :
		MysqlRes = data_.mysqlStoreData()	#Store the data we catched into MySql if needed. 
		if not MysqlRes :
			ErrorHandling.logStorageError(start)	#If there is an exception, print error into file. 
	del data_	#Remove the object
	start = start + 1

ErrorHandling.logDone()
print 'Done'