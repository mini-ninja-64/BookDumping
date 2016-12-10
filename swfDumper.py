import os
import time
import sys
import shutil

dir = input("Enter directory to dump to: ")
width = int(input("Enter the width to render at: "))
(columns,lines) = shutil.get_terminal_size((80, 20))

numOfFiles = 0
numOfFilesProcessed = 0

for file in os.listdir(os.getcwd()):
	if file.endswith(".swf"):
		numOfFiles += 1

for file in os.listdir(os.getcwd()):
	if file.endswith(".swf"):
		command = "swfrender " + os.path.abspath(file) + " -X " + str(width) + " -o " + dir + "/" + os.path.splitext(file)[0] + ".png"
		os.system(command)
		#time.sleep(0.25)

		#recheck size
		(columns,lines) = shutil.get_terminal_size((80, 20))
		percent = numOfFilesProcessed/numOfFiles

		loadingBar = ''
		for i in range(0,int((columns+1)*percent)):
			loadingBar += '#'

		#Clear and write
		sys.stdout.write("\033[K") #clear line
		print(loadingBar)
		sys.stdout.write("\033[F") #back to previous line

		numOfFilesProcessed += 1

print()
print("Dump Completed!")
