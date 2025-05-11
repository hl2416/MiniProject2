from filter_packets import *
from packet_parser import *
from compute_metrics import *
import csv

filename = 'Node1.txt'
filter(filename, 1)

filename = 'Node2.txt'
filter(filename, 2)

filename = 'Node3.txt'
filter(filename, 3)

filename = 'Node4.txt'
filter(filename, 4)

#Calls to parse function in packet_parser.py, made by Devon
filename="Node1_filtered.txt"
n1=parse(filename)

filename="Node2_filtered.txt"
n2=parse(filename)

filename="Node3_filtered.txt"
n3=parse(filename)

filename="Node4_filtered.txt"
n4=parse(filename)


#Calls to compute function in compute_metrics.py, made by Hai Jie
metrics1 = compute(n1, "192.168.100.1")
metrics2 = compute(n2, "192.168.100.2")
metrics3 = compute(n3, "192.168.200.1")
metrics4 = compute(n4, "192.168.200.2")

#Writes the output from compute_metrics into a csv file called output.csv
with open("output.csv", "w") as output :
	metricsWriter = csv.writer(output, delimiter=",")
	
	#Hardcoded Node 1 Write
	metricsWriter.writerow(["Node 1"])
	metricsWriter.writerow(["\n"])
	metricsWriter.writerow(["Echo Requests Sent","Echo Requests Received","Echo Replies Sent","Echo Replies Received"])
	metricsWriter.writerow([metrics1[0],metrics1[1],metrics1[2],metrics1[3]])
	metricsWriter.writerow(["Echo Request Bytes Sent (bytes)","Echo Request Data Sent (bytes)"])
	metricsWriter.writerow([metrics1[4],metrics1[6]])
	metricsWriter.writerow(["Echo Request Bytes Received (bytes)","Echo Request Data Received (bytes)"])
	metricsWriter.writerow([metrics1[5],metrics1[7]])
	metricsWriter.writerow(["\n"])
	metricsWriter.writerow(["Average RTT (milliseconds)",metrics1[8]])
	metricsWriter.writerow(["Echo Request Throughput (kB/sec)",metrics1[9]])
	metricsWriter.writerow(["Echo Request Goodput (kB/sec)",metrics1[10]])
	metricsWriter.writerow(["Average Reply Delay (microseconds)",metrics1[11]])
	metricsWriter.writerow(["Average Echo Request Hop Count",metrics1[12]])
	metricsWriter.writerow(["\n"])
	
	#Hardcoded Node 2 Write
	metricsWriter.writerow(["Node 2"])
	metricsWriter.writerow(["\n"])
	metricsWriter.writerow(["Echo Requests Sent","Echo Requests Received","Echo Replies Sent","Echo Replies Received"])
	metricsWriter.writerow([metrics2[0],metrics2[1],metrics2[2],metrics2[3]])
	metricsWriter.writerow(["Echo Request Bytes Sent (bytes)","Echo Request Data Sent (bytes)"])
	metricsWriter.writerow([metrics2[4],metrics2[6]])
	metricsWriter.writerow(["Echo Request Bytes Received (bytes)","Echo Request Data Received (bytes)"])
	metricsWriter.writerow([metrics2[5],metrics2[7]])
	metricsWriter.writerow(["\n"])
	metricsWriter.writerow(["Average RTT (milliseconds)",metrics2[8]])
	metricsWriter.writerow(["Echo Request Throughput (kB/sec)",metrics2[9]])
	metricsWriter.writerow(["Echo Request Goodput (kB/sec)",metrics2[10]])
	metricsWriter.writerow(["Average Reply Delay (microseconds)",metrics2[11]])
	metricsWriter.writerow(["Average Echo Request Hop Count",metrics2[12]])
	metricsWriter.writerow(["\n"])
	
	#Hardcoded Node 3 Write
	metricsWriter.writerow(["Node 3"])
	metricsWriter.writerow(["\n"])
	metricsWriter.writerow(["Echo Requests Sent","Echo Requests Received","Echo Replies Sent","Echo Replies Received"])
	metricsWriter.writerow([metrics3[0],metrics3[1],metrics3[2],metrics3[3]])
	metricsWriter.writerow(["Echo Request Bytes Sent (bytes)","Echo Request Data Sent (bytes)"])
	metricsWriter.writerow([metrics3[4],metrics3[6]])
	metricsWriter.writerow(["Echo Request Bytes Received (bytes)","Echo Request Data Received (bytes)"])
	metricsWriter.writerow([metrics3[5],metrics3[7]])
	metricsWriter.writerow(["\n"])
	metricsWriter.writerow(["Average RTT (milliseconds)",metrics3[8]])
	metricsWriter.writerow(["Echo Request Throughput (kB/sec)",metrics3[9]])
	metricsWriter.writerow(["Echo Request Goodput (kB/sec)",metrics3[10]])
	metricsWriter.writerow(["Average Reply Delay (microseconds)",metrics3[11]])
	metricsWriter.writerow(["Average Echo Request Hop Count",metrics3[12]])
	metricsWriter.writerow(["\n"])
	
	#Hardcoded Node 4 Write
	metricsWriter.writerow(["Node 4"])
	metricsWriter.writerow(["\n"])
	metricsWriter.writerow(["Echo Requests Sent","Echo Requests Received","Echo Replies Sent","Echo Replies Received"])
	metricsWriter.writerow([metrics4[0],metrics4[1],metrics4[2],metrics4[3]])
	metricsWriter.writerow(["Echo Request Bytes Sent (bytes)","Echo Request Data Sent (bytes)"])
	metricsWriter.writerow([metrics4[4],metrics4[6]])
	metricsWriter.writerow(["Echo Request Bytes Received (bytes)","Echo Request Data Received (bytes)"])
	metricsWriter.writerow([metrics4[5],metrics4[7]])
	metricsWriter.writerow(["\n"])
	metricsWriter.writerow(["Average RTT (milliseconds)",metrics4[8]])
	metricsWriter.writerow(["Echo Request Throughput (kB/sec)",metrics4[9]])
	metricsWriter.writerow(["Echo Request Goodput (kB/sec)",metrics4[10]])
	metricsWriter.writerow(["Average Reply Delay (microseconds)",metrics4[11]])
	metricsWriter.writerow(["Average Echo Request Hop Count",metrics4[12]])
