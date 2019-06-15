import serial
import time

s = serial.Serial('/dev/ttyAMA0', 9600)			# s is the variable for the serial connection
#s = serial.Serial('/dev/ttyAMA0', 115200)
#s.open()	# Already open(?)

#time.sleep(5)

Mode = 0						# Variable for the mode
# 0: No Mode
# 1: Mapping
# 2: Hole Detection
# 3: Speed Test
# 4: Dead End


# Open or create files for the data, then close them until they are used again
DataForMapping = open("DataForMapping.txt", "w")
DataForMapping.close()


while (Mode != 1) and (Mode != 2) and (Mode != 3) and (Mode != 4):
	print("Please select the mode you want to enter:\n1: Mapping\n2: Hole Detection\n3: Speed Test\n4: Dead End")
	ModeInput = raw_input()
	Mode = int(ModeInput)
time.sleep(5)
s.write(str(Mode))

while True:						# Endless loop

	if Mode == 1:					# Mode for cartography
#		s.write("1")				# Write the mode number (1) to the Arduino
		coordinates = s.readline()		# Get back the coordinates
#		print("Coordinates = " + coordinates)

		# Write the coordinates in the text file
		DataForMapping = open("DataForMapping.txt", "a")
		DataForMapping.write(coordinates)
		DataForMapping.close

	if Mode == 2:
#		s.write("2")
		distance = float(s.readline())
		angle = float(s.readline())

		print(distance)
		print(angle)
