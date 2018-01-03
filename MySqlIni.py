#-----------------------------------------------------------------------------------------------------------------------------
#|	When you use this program please run run.py file.                                                                         |
#|	This file is made for MySql connection test, and create a database table for store the data.                              |
#|	The use of this code follows the Mozilla Public License Version 2.0, for detail: https://www.mozilla.org/en-US/MPL/2.0/   |
#|----------------------------------------------------------------------------------------------------------------------------|
# -*- coding: utf-8 -*-
import MySQLdb
import config


def connTest() :
	#Method connTest is made for MySql connection test. 
	#Return 1 means connect successful
	#Return 0 means connect fail
	try :
		dbTest = MySQLdb.connect(config.MySqlHost,config.MySqlUser,config.MySqlPassword,config.MySqlDatabase )
		cursorTest = dbTest.cursor()
		cursorTest.execute("SELECT VERSION()")
		dataTest = cursorTest.fetchone()
		dbTest.close()
		return 1
	except MySQLdb.Error, e: 
		ErrorHandling.errorOutput(0,"Cannot connect to the Database",repr(e),4)	#If there is an error, ErrorHandling.py would handle the error. 
		return 0
		
		
def createTable() :
	#Method createTable is made for creation of MySql database table, and the program would store the data catched into this table
	#Return 1 means that creation completed
	#Return 0 means that creation failed
	try :
		db = MySQLdb.connect(config.MySqlHost,config.MySqlUser,config.MySqlPassword,config.MySqlDatabase )
		cursor = db.cursor()
		#Variable sql is the SQL statement for the creation of table. 
		sql = """CREATE TABLE `""" + config.MySqlDatabase + """`.`""" + config.MysqlTableName + """` ( `lot_id` INT(6) NOT NULL COMMENT 'The lot ID number' , `author_name` VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'The artist name' , `author_birth` INT(4) NOT NULL COMMENT 'The artist Birth year (0 means that there is no birth information for this artist)' , `author_death` INT(4) NOT NULL COMMENT 'The artist Death year (0 means that the artist has not dead yet, or there is no information about the author death year)' , `author_race` VARCHAR(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'The artist nationality' , `lot_name` VARCHAR(1024) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'The name of this lot' , `lot_year` INT(4) NOT NULL COMMENT 'The year of the creation' , `lot_info` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'Some general information about this lot (Such as size)' , `lot_info_addi` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'Some additional information about this lot' , `lot_desc` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'The description about this lot' , `lot_provenance` TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'The provenance of this lot' , `est_upp` INT(16) NOT NULL COMMENT 'The estimate price for this lot in upper bound' , `est_low` INT(16) NOT NULL COMMENT 'The estimate price for this lot in lower bound' , `biding_price` INT(16) NOT NULL COMMENT 'The current bidding price if the lot has not been sold yet, or the deal price of this lot if the lot has already been sold ' , `biding_number` INT(4) NOT NULL COMMENT 'How many bidder place bid on this lot' , `lot_status` INT(2) NOT NULL COMMENT '1 means that the lot has already been sold, and 0 means that the lot has not been sold yet' , `ending_date` DATE NOT NULL COMMENT 'The date of the lot would be sold' ) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_general_ci;"""
		cursor.execute(sql)
		db.close()
		return 1
	except MySQLdb.Error, e: 
		ErrorHandling.errorOutput(0,"Cannot create Table in Database",repr(e),4)	#If there is an error, ErrorHandling.py would handle the error. 
		return 0