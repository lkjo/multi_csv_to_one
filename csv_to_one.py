# import pandas as PD
import xlsxwriter
import os
path = "."
data = []
xlNameList = [i for i in os.listdir(path) if i.endswith(".csv")]
result = xlsxwriter.Workbook("result2.xlsx")
for i in range(len(xlNameList)):
    temp = path+"/"+xlNameList[i]
    file = open(temp,'r',encoding='utf-8')
    content = file.readlines()
    if i ==0:
        data.append(content[0].replace('"',"").split(","))
    for j in range(1,len(content)):
        content[j] = content[j].replace('"',"")
        data.append(content[j].split(","))
# print(*data,sep="\n")
temp = [result.add_worksheet()]
font = result.add_format({"font_size":12})
for i in range(len(data)):
    for j in range(len(data[i])):
        # print(data[i][j])
        temp[0].write(i,j,data[i][j],font)
# result.save("result.xlsx")
result.close()