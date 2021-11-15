#Self assessment Python task
from math import pi

inputFuncCount = 0
outputFuncCount = 0
degList = []
radList = []

#Function 1: takes input for a list
def inputFunc():
	global inputFuncCount
	global degList
	for i in range(0,5):
		degreein = int(input("Enter degrees: "))
		degList.append(degreein)
		inputFuncCount = inputFuncCount + 1
		if inputFuncCount > 4:
			degreeCalc()

#Function 2: takes our input to convert to radians
def degreeCalc():
	global radList
	global outputFuncCount
	print("Your entered degrees: " + str(degList))
	for i in degList:
		convertedEntry = ((pi/180)*i)
		radList.append(convertedEntry)
		outputFuncCount = outputFuncCount + 1
		if outputFuncCount > 4:
			listAssemble()
	
#Function 3: Prints the results all pretty like			
def listAssemble():
		for i, r in enumerate(radList):
			print("Radian " + str(i+1) + ": " + str(r))
		

#Main script
inputFunc()