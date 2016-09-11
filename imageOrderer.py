import os
import time
import sys
import shutil

numOfFront = 0
numOfPage = 0
numOfPrelim = 0

currFrontI = 0
currPrelimI = 0
currPageI = 0

for file in os.listdir(os.getcwd()):
	fileName = os.path.splitext(file)[0];
	if ("front" in fileName):
		numOfFront+=1
	elif ("prelim" in fileName):
		numOfPrelim+=1
	elif ("page" in fileName):
		numOfPage+=1

for file in os.listdir(os.getcwd()):
	fileName = os.path.splitext(file)[0];
	if ("front" in fileName):
			#print ("front")
			os.rename(file, format(currFrontI, '05') + '.png')
			currFrontI+=1
	elif ("prelim" in fileName):
			#print ("prelim")
			os.rename(file, format(currPrelimI+numOfFront, '05') + '.png')
			currPrelimI+=1
	elif ("page" in fileName):
			#print ("page")
			os.rename(file, format(currPageI+numOfFront+numOfPrelim, '05') + '.png')
			currPageI+=1