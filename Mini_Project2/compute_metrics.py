def compute(filename, ip) :
	print('called compute function in compute_metrics.py')
	
	metrics = []
	requestSent = []
	requestRec = []
	replySent = []
	replyRec = []
	rByteSent = 0
	rByteRec = 0
	rDataSent = 0
	rDataRec = 0
	rttSum = 0
	rpSum = 0
	ttlSum = 0

	#Data Size Metrics
	#appends the echo requests sent/received and echo replies sent/received to a list for easier computing and also gives the numbers for metrics 1-4 when len is used
	for iter in filename :
		if ip == iter[2] :
			if iter[5] == 'request' :
				requestSent.append(iter)
			if iter[5] == 'reply' :
				replySent.append(iter)
		elif ip != iter[2] :
			if iter[5] == 'request' :
				requestRec.append(iter)
			if iter[5] == 'reply' :
				replyRec.append(iter)
	
	#metrics 5-8
	for iter in requestSent :
		rByteSent = rByteSent + float(iter[4])
		rDataSent = rDataSent + float(iter[4]) - 42
	
	for iter in requestRec :
		rByteRec = rByteRec + float(iter[4])
		rDataRec = rDataRec + float(iter[4]) - 42
	
	#Time Based Metrics
	#metric 9
	for iter in requestSent :
		time = float(iter[1])
		seqNum = iter[6]
		for iter in replyRec :
			if iter[6] == seqNum :
				rttSum = rttSum + (float(iter[1]) - time)
	rtt = (rttSum / len(requestSent)) * 1000
	
	#metric 10
	requestTP = (rByteSent / 1000) / rttSum

	#metric 11
	requestGP = (rDataSent / 1000) / rttSum
	
	#metric 12
	for iter in requestRec :
		time = float(iter[1])
		seqNum = iter[6]
		for iter in replySent :
			if iter[6] == seqNum :
				rpSum = rpSum + (float(iter[1]) - time)
	rp = (rpSum / len(requestRec)) * 1000000
	
	#Distance Metric
	#metric 13
	for iter in requestSent :
		ttl = float(iter[7])
		seqNum = iter[6]
		for iter in replyRec :
			if iter[6] == seqNum :
				ttlSum = ttlSum + (ttl - float(iter[7])) + 1
	avgNumHops = ttlSum / len(requestSent)
	
	#appends all the metrics into the metrics list to be returned and hardcoded into output file in packet_analyzer.py
	metrics.append(str(len(requestSent)))
	metrics.append(str(len(requestRec)))
	metrics.append(str(len(replySent)))
	metrics.append(str(len(replyRec)))
	metrics.append(str(int(rByteSent)))
	metrics.append(str(int(rByteRec)))
	metrics.append(str(int(rDataSent)))
	metrics.append(str(int(rDataRec)))
	metrics.append(str("%.2f" % rtt))
	metrics.append(str("%.1f" % requestTP))
	metrics.append(str("%.1f" % requestGP))
	metrics.append(str("%.2f" % rp))
	metrics.append(str("%.2f" % avgNumHops))
	
	return metrics
