import matplotlib.pyplot as plt
import csv
filename = "table.csv"
x = []
y = []
with open(filename, 'r') as csvfile:
   csvreader = csv.reader(csvfile)
   for row in csvreader:
   	x.append(row[0])
   	y.append(row[1])
print(x)
print(y)
plt.plot(x,y)
plt.show()
