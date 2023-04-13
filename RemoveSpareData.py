#ARGUMENT IS .BIN FILE TO BE PARSED
#PRINTS GOOD DATA INTO PARSED.BIN
#PRINTS BAD DATA INTO JUNK.BIN 
import sys

input_file = open(sys.argv[1], 'rb')
output_file = open("parsed.bin", "wb")
junk_file = open("junk.bin", "wb")

i=0
while(i < <number_of_pages>):
    try:
        output_file.write(input_file.read(<data_size>))
        junk_file.write(input_file.read(<spare_data_size>))
        i += 1
    except:
        output_file.close()
        input_file.close()
        junk_file.close()
        print("DONE!")
