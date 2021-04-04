import math
import csv
with open("sd.csv", newline='') as f:
    reader= csv.reader(f) 
    file_data= list(reader)
data = file_data[0]
# find mean
def mean(data):
    n = len(data)
    total= 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean
# squaring the values
squared_list = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)
sum = 0
for i in squared_list:
    sum = sum + i
result = sum/(len(data)-1)
print('length is '+ str(len(data)))
standard_deviation = math.sqrt(result)
print (standard_deviation)