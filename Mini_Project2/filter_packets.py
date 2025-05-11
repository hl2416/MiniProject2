def filter(filename, node) :
	print('called filter function in filter_packets.py')
	
	#open files 
	newfile = "Node"+ str(node) +"_filtered.txt"
	infile = open(filename, 'r')
	outfile = open(newfile, 'w')

	#skip over first line to get past headings
	line = infile.readline()
	line = infile.readline()
	
	while line :
		line = line.strip()
		if 'Echo (ping)' in line:
			#write the line we just checked
			line = line.strip()
			line = line + "\n"
			outfile.write(line)
			line = infile.readline()
			#write everything else in this packet
			while 'Destination' not in line :
				line = line.strip()
				line = line + "\n"
				outfile.write(line)
				line = infile.readline()
			#space to separate packets
			outfile.write("\n")


		line = infile.readline() #read next line
        
	infile.close()
	outfile.close()
