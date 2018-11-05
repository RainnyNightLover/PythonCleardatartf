'''
xihuanyuye
'''
import re
import xlwt
import os

L=[]
for root, dirs, files in os.walk("input/"):
    for file in files:
        if os.path.splitext(file)[1] == '.txt': 
            L.append(os.path.join(root,file))
for index,temp in enumerate(L):
    f = open(temp)
    line = f.readline()
    i=0
    excle = xlwt.Workbook()
    sheet1 = excle.add_sheet(u'sheet1',cell_overwrite_ok=True)
    
    while line:
        if line == '\n':
            line = f.readline()
            continue
        #print(line,end="")
        rightline = re.findall("^From[\s\S]*, Language:[\s\S]*, Database: CAPLUS$",line)
        if rightline:
            i=i+1
            #print(i,end=' ')
            #print(rightline[0])
            text1 = rightline[0][5:]
            text2 = re.split(",",text1)
            #print(text2[0])
            #print(text2[1][1:-11])
            #print(text2[1][-11:])
            for j in range(0,2):
                sheet1.write(i,0,text2[0])
                sheet1.write(i,1,text2[1][1:-11])
                sheet1.write(i,2,text2[1][-11:])
        line = f.readline()
    filename = "output/"+temp[6:-3]+"xlsx"
    excle.save(filename)
    print("###############  完成",round(index/L.__len__(),2)*100,"%  ################")
