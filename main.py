import sys
import datetime

def productfile(path, factor):
	sum = factor
	for line in open(path):
		sum *= int(line)
	return sum

def sumfile(path):
	sum = 0
	for line in open(path):
		sum += int(line)
	return sum

a = sumfile("C:/Users/Michiana Archery/Documents/Aidan/Python/01/test.txt")
b = productfile("C:/Users/Michiana Archery/Documents/Aidan/Python/01/test.txt", 2)

function = sys.argv[1]
parts = function.split(" ")
if parts[1] == "*":
	print( int(parts[0]) * int(parts[2]) )
c = 1

print(a + b + c)

def isChristmasDay():
	return datetime.date.month == 12 and datetime.date.day == 20

if isChristmasDay():
	print("YES")
else:
	print("No")

a = 1
if a == 1:
	print("1")
elif a == 2:
	print("2")
else:
	print("other")