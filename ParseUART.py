#!/usr/bin/env python3
#TO BE USED WHEN DUMPING FIRMWARE OVER UART
#USE "sudo picocom -b <baud> /dev/ttyUSB0 -g <output file>" TO RECORD UART OUTPUT
#THIS FILE JUST REMOVES SPACES FROM EACH UART LINE, MORE TRIMMING CAN BE ADDED IF NECESSARY
import sys

if len(sys.argv) < 2:
	print("USEAGE: "+sys.argv[0]+" INFILE OUTFILE")
	sys.exit(0)

infile = sys.argv[1]
outfile = sys.argv[2]

f_in = open(infile,'r')
f_out = open(outfile, 'wb')

for line in f_in:
	line = line.strip()
	
        #process data line
	line = line.replace(" ","")
	line = bytes.fromhex(line)
	f_out.write(line)

f_in.close()
f_out.close()
