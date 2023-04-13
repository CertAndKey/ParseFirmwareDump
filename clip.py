import sys

input_file = open(sys.argv[1], 'rb')
output_file = open("parsed.bin", "wb")
junk_file = open("junk.bin", "wb")

i=0
while(i < 131072):
    try:
        output_file.write(input_file.read(2048))
        junk_file.write(input_file.read(128))
        i += 1
    except:
        output_file.close()
        input_file.close()
        junk_file.close()
        print("DONE!")
