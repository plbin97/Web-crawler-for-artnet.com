#-----------------------------------------------------------------------------------------------------------------------------
#|	When you use this program please run run.py file. 																		  |
#|	This is the configuration file for this program. 			  															  |
#|	Please do not delete any variable here, but you can change its values													  |
#|	The use of this code follows the Mozilla Public License Version 2.0, for detail: https://www.mozilla.org/en-US/MPL/2.0/   |
#|----------------------------------------------------------------------------------------------------------------------------|
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
#Important: please Do not delete any statement here, even those are not useful. 
#-------------------------------------------------------------------------------


#	Search_from is the First lot's ID that the program would going to catch
Search_from = 1
#	The program would catch the data from lot's ID in "Search_from" to lot's ID in 'Search_to'
#	Now, the latest lot's ID I get is: 123783. 
#	You can put any number which larger than latest lot's ID
Search_to = 140000

#--------------------------------------------------------------------------------
# Those configuration is used for MySql Database storage. 
# If you do not want to use MySql Database to store the data, just ignore this area
# If you wana to use MySql to store your data, please take a look here: 
#
#
#If you want to storage the data in MySql database, 
#please change the value for variable UseMySqlDataBase = 1
UseMySqlDataBase = 0
#
#
#Before you use MySql Database to store your data, please create a Database in MySql first. 
#
#This program required a certain format of database table. 
#If you already have that table, please set the value: MySqlTableExisted = 1
#If you do not have that table, please set the value: MySqlTableExisted = 0, and we can create for you
MySqlTableExisted = 0
#
#
#Following are the MySql connection Configuration: 
MySqlHost = 'localhost'	#Put your MySql Host here
MySqlUser = 'root'	#Put your MySql User here
MySqlPassword = 'your_password'	#Put your MySql Password Here 
MySqlDatabase = 'database_name'	#Put your MySql Database Name here
MysqlTableName = 'table_name'	#Put the MySql table name which you are going to create or you are going to use here

#--------------------------------------------------------------------------------
#Do you want to print the data you catched in to Consolo? 
# If you want to do that, please set value: DisplayData = 1
# If you don't want to do that, please set value: DisplayData = 0
DisplayData = 0

#--------------------------------------------------------------------------------
#Do you want to store the data you catched into a file? 
# If you want to do that, please set value: PrintThemInToFile = 1
# If you don't want to do that, please set value: PrintThemInToFile = 0
PrintThemInToFile = 0
#
#
#If you are going to store the data you catched into a file, please put your file path: 
#The format should be: FilePath = 'example_path/example_output.txt'
FilePath = 'output.txt'
#If you do not want to store the data into file, just ignore above items. 

#--------------------------------------------------------------------------------
#The program would have a log output system, and there is two kinds of log. 
#
#The first kind of log is only for the error and the exception. 
#Here, you have to set the error log path
#The format would be: ErrorPath = 'example_path/error_output.log'	
ErrorPath = 'error.log'	
#During the program is running, you can see if there is any error happened through that file
#
#
#The second kind of log would notice all the thing happened in this program. 
#You can trace Which lot does the program is catching now, and you can see the statue of this program. 
#Here, you have to set the general log path. 
#The format would be: LogPath = 'example_path/log_output.log'
LogPath = 'statue.log'

#----------------------------------------------------------------------------------
#You have already set them all? 
#Good, you can start to execute run.py now. 