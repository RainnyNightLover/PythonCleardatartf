'''
xihuanyuye
'''
import os
import xlwt

L=[]
for root, dirs, files in os.walk("output/"):
    for file in files:
        if os.path.splitext(file)[1] == '.txt': 
            L.append(os.path.join(file))
#print(L)
i=0
for temp in L:
    i = i+1
    print(temp)
    print(i)