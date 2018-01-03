#-----------------------------------------------------------------------------------------------------------------------------
#|	When you use this program please run run.py file.                                                                         |
#|	This file is used for handling the data catched by engine.py                                                              |
#|	Also, this file support the storage of data into file or into database                                                    |
#|	The use of this code follows the Mozilla Public License Version 2.0, for detail: https://www.mozilla.org/en-US/MPL/2.0/   |
#|----------------------------------------------------------------------------------------------------------------------------|
# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
import config
import ErrorHandling
if config.UseMySqlDataBase == 1 :
	import MySQLdb


class dataCatched :
	#------------------------------------------------------------------------------------
	#For the use of this class dataCatched, each lot is one object based on this class. 
	#This class inclusive of the method of storage and display
	#Now, we only support to store the data to a file and MySql database
	#You can add your own customized code below. 
	#After you create the object, remember to delete the object after you use in order to release the memory
	#------------------------------------------------------------------------------------

	def __init__(self,lot_id,artest,artest_race,artest_birth,artest_death,lot_name,lot_year,lot_info,lot_info_2,lot_desc,lot_provenance,est_low,est_up,bid_price,bid_number,lot_sold,lot_sell_date) :
		#Method for initialization of object
		#For each variable, I introduce them below. 
		#For initialization, please be careful with the data type: 
		self.lot_id = lot_id	#integer, lot's ID number
		self.artest = artest	#String, Artist's name
		self.artest_race = artest_race	#String, Artist's Nationality
		self.artest_birth = artest_birth	#integer, Artist's birth year
		self.artest_death = artest_death	#integer, Artist's death year
		self.lot_name = lot_name	#String, Lot's Title/Name
		self.lot_year = lot_year	#integer, Lot's creation year
		self.lot_info = lot_info	#String, Lot's general information
		self.lot_info_2 = lot_info_2	#String, Lot's additional information
		self.lot_desc = lot_desc	#String, Lot's artistic description
		self.lot_provenance = lot_provenance	#String, Lot's provenance
		self.est_low = est_low	#integer, lower bound for Lot's estimated price 
		self.est_up = est_up	#integer, upper bound for Lat's estimated price
		self.bid_price = bid_price	#integer, Lot's Final price (The price for last bid)
		self.bid_number = bid_number	#integer, Lot's bid number
		self.lot_sold = lot_sold	#integer, value 1 means that the lot has already been sold, 0 means that lot has not been sold yet
		self.lot_sell_date = lot_sell_date	#datetime Object, the date that lot would/will be sold

	
	def displayData(self) :	
		#Method for display the data
		#When the method is called, the program would print all the lot's information in console
		print '---------------------------------------------------------- \n'
		print 'Lot\' ID : ' + str(self.lot_id) + '\n'
		print 'Artest : ' + self.artest.encode('utf-8') + '\n'
		print 'Artest\'s Nation : ' + self.artest_race.encode('utf-8') + '\ln'
		if self.artest_birth != 0 :
			if self.artest_death == 0 :
				print 'Artest borned in ' + str(self.artest_birth) + ' , and still alived\n'
			else :
				print 'Artest borned in ' + str(self.artest_birth) + ' and died in ' + str(self.artest_death) + '\n'
		print 'The name of the lot is : ' + self.lot_name.encode('utf-8') + '\n'
		print 'The lot was created in ' + str(self.lot_year) + '\n'
		print 'The general information for this lot is : ' + self.lot_info.encode('utf-8') + '\n'
		if self.lot_info_2 != '' :
			print 'Additional Information about this lot : ' + self.lot_info_2.encode('utf-8') + '\n'
		print 'Description of this lot: ' + self.lot_desc.encode('utf-8') + '\n'
		if self.lot_provenance != '' :
			print 'The provenance of this lot : ' + self.lot_provenance.encode('utf-8')
		print 'The estimated price for this lot is : ' + str(self.est_low) + ' to ' + str(self.est_up) + '\n'
		print 'The final price of Bidding is/was : ' + str(self.bid_price) + '\n'
		print 'This lot was bided for ' + str(self.bid_number) + ' times\n'
		if self.lot_sold == 0 :
			print 'This lot has not been sold yet\n'
		else :
			print 'This lot has already been sold\n'
		print 'This lot was sold/will be sold at ' + self.lot_sell_date.strftime('%Y-%m-%d') + '\n'
		print '---------------------------------------------------------- \n'
	
	def printData (self) :
		#Method for print the data into file
		#You can set the file path in config.py : FilePath = '<the path you for your ourput date>'
		#The method would print a beautiful format which easy for you to read. 
		fil = open(config.FilePath, "a")
		print >> fil, '---------------------------------------------------------- \n'
		print >> fil, 'Lot\' ID : ' + str(self.lot_id) + '\n'
		print >> fil, 'Artest : ' + self.artest.encode('utf-8') + '\n'
		print >> fil, 'Artest\'s Nation : ' + self.artest_race.encode('utf-8') + '\ln'
		if self.artest_birth != 0 :
			if self.artest_death == 0 :
				print >> fil, 'Artest borned in ' + str(self.artest_birth) + ' , and still alived\n'
			else :
				print >> fil, 'Artest borned in ' + str(self.artest_birth) + ' and died in ' + str(self.artest_death) + '\n'
		print >> fil, 'The name of the lot is : ' + self.lot_name.encode('utf-8') + '\n'
		print >> fil, 'The lot was created in ' + str(self.lot_year) + '\n'
		print >> fil, 'The general information for this lot is : ' + self.lot_info.encode('utf-8') + '\n'
		if self.lot_info_2 != '' :
			print >> fil, 'Additional Information about this lot : ' + self.lot_info_2.encode('utf-8') + '\n'
		print >> fil, 'Description of this lot: ' + self.lot_desc.encode('utf-8') + '\n'
		if self.lot_provenance != '' :
			print >> fil, 'The provenance of this lot : ' + self.lot_provenance.encode('utf-8')
		print >> fil, 'The estimated price for this lot is : ' + str(self.est_low) + ' to ' + str(self.est_up) + '\n'
		print >> fil, 'The final price of Bidding is/was : ' + str(self.bid_price) + '\n'
		print >> fil, 'This lot was bided for ' + str(self.bid_number) + ' times\n'
		if self.lot_sold == 0 :
			print >> fil, 'This lot has not been sold yet\n'
		else :
			print >> fil, 'This lot has already been sold\n'
		print >> fil, 'This lot was sold/will be sold at ' + self.lot_sell_date.strftime('%Y-%m-%d') + '\n'
		print >> fil, '---------------------------------------------------------- \n'
		fil.close()
	
	def mysqlStoreData (self) : 
	#Method for storing the data into MySql database
	#The method would check if you want to store the data into MySql database in your setting in config.py file
	#Before calling this method, please ensure that you have already create a table in database in appropriate format. 
	#If you don't know what is appropriate format is, please take a look at MySqlIni.py. There is a method createTable(), and it would help you. 
	#Actually, the users do not required to create a table first. You can edit config.py file, and set: MySqlTableExisted = 0. Then the program would automatically create a table before catch the data. 
	#This method has return value. 
	#If there is no error and storage successful, the method would return 1
	#If there is an error happened, the method would tried to repeat the storage for at maxitum 3 times til storage successful, and return 1.
	#If it has error happened for three tims and storage failure, the method would return 0
		if config.UseMySqlDataBase == 1 :
			flag = 0
			while flag < 3 :
				try :
					#---------------------------------------------------------------------------------------------------
					#Mysql Database operation
					db = MySQLdb.connect(config.MySqlHost,config.MySqlUser,config.MySqlPassword,config.MySqlDatabase)
					cursor = db.cursor()
					cursor.execute("INSERT INTO " + config.MysqlTableName + "(lot_id, author_name, author_birth, author_death, author_race, lot_name, lot_year, lot_info, lot_info_addi, lot_desc, lot_provenance, est_upp, est_low, biding_price, biding_number, lot_status, ending_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (self.lot_id, self.artest.encode('utf-8'), self.artest_birth, self.artest_death, self.artest_race.encode('utf-8'), self.lot_name.encode('utf-8'), self.lot_year, self.lot_info.encode('utf-8'), self.lot_info_2.encode('utf-8'), self.lot_desc.encode('utf-8'), self.lot_provenance.encode('utf-8'), self.est_up, self.est_low, self.bid_price, self.bid_number, self.lot_sold, self.lot_sell_date.strftime('%Y-%m-%d 0:0:0')))
					db.commit()
					db.close()
					#-----------------------------------------------------------------------------------------------------
					return 1
				except MySQLdb.Error, e:
					#If there is error happened: 
					if flag < 2 : 
						ErrorHandling.errorOutput(self.lot_id,'DataBase Error',repr(e),1)
						flag = flag + 1
						continue
					else :
						ErrorHandling.errorOutput(self.lot_id,'DataBase Error',repr(e),2)
						return 0


						
	#--------------------------------------------------------------------
	#Here, you can add your own customized method code for handling the data. 
	#For example: 
	#------------------------------
	#def example(self) :
		#We have those variables for you to use, and those variable has already introduce in aboved comment. 
		#If you do not understand those variables, please take a look at __init__()
		#You have permission to get the value from variables and change the value in variables. 
		#But you have to be careful with the data type. Also, be careful with charset
		#Variables: 
		# self.lot_id
		# self.artest
		# self.artest_race
		# self.artest_birth
		# self.artest_death
		# self.lot_name
		# self.lot_year
		# self.lot_info
		# self.lot_info_2
		# self.lot_desc
		# self.lot_provenance
		# self.est_low
		# self.est_up
		# self.bid_price
		# self.bid_number
		# self.lot_sold
		# self.lot_sell_date
	#------------------------------
	#After you create methods here, you can call the method in run.py
	#I'm happy for you to add more method
	#----------------------------------------------------------------------
	