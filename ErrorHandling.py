#-----------------------------------------------------------------------------------------------------------------------------
#|	 When you use this program please run run.py file. 																		  |
#|	This file is made for handling the error happened in program, because we are not sure that the program is perfect.		  |
#|	 We would print the log and error into file. After user run the program, they should take a look at the log and see what  |
#|	data has not been captured yet.																							  |
#|	 The use of this code follows the Mozilla Public License Version 2.0, for detail: https://www.mozilla.org/en-US/MPL/2.0/  |
#|----------------------------------------------------------------------------------------------------------------------------|
# -*- coding: utf-8 -*-
import config

#------------------------------------------------------------------------------------------------------------------
#First, you have to under stand that we have two file. One is the "log file", which store the general log: successful and failure. Another one is the "error file", which store the error information when the error is happened when program is running. 
#------------------------------------------------------------------------------------------------------------------


def errorOutput(lot_id,errorType,errorInfo,statue) :
	#Method errorOurput is made for storing the error into error file, when the users execute the program, they can see the error happened in program
	#There is four parameter
	#First parameter is the lot's id where the error happened, integer type
	#Second parameter is the error type, for example 'Database Error', string type
	#Third parameter is the error information, about the detail of error, string type
	#Last parameter is the statue of the program, integer type. For detail of this parameter, please take a look at at following code. I believe that you will under stand without comments
	fil = open(config.ErrorPath, "a")
	print >> fil, '---------------------------------------------------------- \n'
	if lot_id != 0 :
		print >> fil, 'Problem lot\' ID : ' + str(lot_id) + '\n'
	print >> fil, 'Type of error : ' + errorType + '\n'
	print >> fil, 'Error detail : ' + errorInfo + '\n'
	#The last parameter: 
	if statue == 1 :
		print >> fil, 'The program is tring to repeat the action\n'
	if statue == 2 :
		print >> fil, 'The program cannot handles this error and abandons the capture of this lot\n'
	if statue == 3 :
		print >> fil, 'The program cannot catchs specific data and abandons this data\n'
	if statue == 4 :
		print >> fil, 'The error is fatal, and the program stoped. Sorry!!\n'
	print >> fil, '---------------------------------------------------------- \n'
	fil.close()


def logSuccess(lot_id) :
	#Method logSuccess is made for printing the 'successful' notification into log file
	#Only one parameter, and that is lot's ID. 
	fil = open(config.LogPath,'a')
	print >> fil, '---------------------------------------------------------- \n'
	print >> fil, 'Catch ' + str(lot_id) + ' successful\n'
	print >> fil, '---------------------------------------------------------- \n'
	fil.close()


def logDone() :
	#Method logDone is made for printing the notification 'Done' into log file
	fil = open(config.LogPath,'a')
	print >> fil, '---------------------------------------------------------- \n'
	print >> fil, 'Done\n'
	print >> fil, '---------------------------------------------------------- \n'
	fil.close()


def logNotFound(lot_id) :
	#Method logNotFound would be used if the program detect that there is no data on that lot. It would print into log file
	fil = open(config.LogPath,'a')
	print >> fil, '---------------------------------------------------------- \n'
	print >> fil, 'There is no data in ' + str(lot_id) + '\n'
	print >> fil, '---------------------------------------------------------- \n'
	fil.close()


def logStorageError(lot_id) :
	#Method logStorageError would be used if there is an storage error happened, usually in MySql database error. It would print into log file. 
	fil = open(config.LogPath,'a')
	print >> fil, '---------------------------------------------------------- \n'
	print >> fil, 'The lot ' + str(lot_id) + ' cannot be handle\n'
	print >> fil, '---------------------------------------------------------- \n'
	fil.close()
	
 
def logFail(lot_id) :
	#Method logFail would be used if the program cannot get the response of url request to the lot's page. It would print into log file.
	fil = open(config.LogPath,'a')
	print >> fil, '---------------------------------------------------------- \n'
	print >> fil, 'Catch ' + str(lot_id) + ' failed. \n'
	print >> fil, '---------------------------------------------------------- \n'
	fil.close()