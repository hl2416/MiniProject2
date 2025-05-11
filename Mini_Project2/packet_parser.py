#Work in Progress for bonus
def convert(data):
	payload=""
	data=data.split(" ")
	for item in data:
		try:
			i = bytes.fromhex(item.decode("ascii"))
			payload+=data.decode('utf-8')
		except:
			payload+="."

#format: num, time, source, destination, length, type(reply/response), sequence, ttl, response/reply num, Ethernet, IP, Message
def parse(filename) :
	print('called parse function in packet_parser.py')
	with open(filename) as f:
		full_list=[]
		start=True
		last_line=""
		line=f.readline()
		lis=[]
		line_num="000"
		Ethernet=""
		IP=""
		Message=""

		while line:
			if start:
				line=line.split("  ")
				num,time=line[0].split(" ")
				# print(line)
				line=list(filter(None, line))
				# print(line)
				lis.append(num)
				lis.append(time)
				#src
				lis.append(line[1].strip())
				#dst
				lis.append(line[2].strip())
				#length
				lis.append(line[4].strip())
				tmp=line[6].strip().split(" ")

				#type
				lis.append(line[5].strip().split(" ")[2])
				#sequence
				lis.append(tmp[1].split("=")[1])
				#ttl
				lis.append(tmp[2].split("=")[1])
				#response/reply num
				lis.append(tmp[5].split(")")[0])

				# if len(tmp)>3:
				# 	lis.append(tmp[2])
				# 	lis.append(tmp[5].split("=")[1])
				# 	lis.append(tmp[6].split("=")[1])
				# 	lis.append(tmp[9].split(")")[0])
				# else:
				# 	lis.append(tmp[2])
				# 	tmp=line[10].strip().split(" ")
				# 	lis.append(tmp[1].split("=")[1])
				# 	lis.append(tmp[2].split("=")[1])
				# 	lis.append(tmp[5].split(")")[0])
				# print(lis)
				start=False

			elif line !="\n":
				line_num=line.split("  ")[0]
				line=line.split("  ")[2].strip()

				if line_num == "0000":
					Ethernet+=line[:14]
					IP+=line[14:]
				elif line_num == "0010":
					IP+=line
				elif line_num == "0020":
					IP+=line[:2]
					Message+=line[2:]
				else:
					Message+=line

			elif last_line=="\n" and line == "\n" and start==False:
				payload=[]
				payload.append(Ethernet)
				payload.append(IP)
				payload.append(Message)
				lis.append(payload)
				full_list.append(lis)
				# print(lis)

				lis=[]
				Message=""
				IP=""
				Ethernet=""
				start=True

			last_line=line
			line=f.readline()
	return full_list
