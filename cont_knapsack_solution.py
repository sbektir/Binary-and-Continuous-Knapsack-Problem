from matplotlib import pyplot as plt
import pandas as pd
import xlrd

    # The data contains 3 different properties. These are the name of the object,
    # the weight of the object and the profit of the object.
    # Apart from these data, a maximum capacity is determined.

datainexcel=pd.read_excel("basic_and_cont_data.xlsx",header=1,usecols="B:D")
data=[]
for index,rows in datainexcel.iterrows():
    listin=[rows.Name,rows.Profit,rows.Weight]
    data.append(listin)
wb=xlrd.open_workbook("basic_and_cont_data.xlsx")
ws=wb.sheet_by_name("data")
maxcond=ws.cell_value(0,6)

for product in data:
    ratio=product[1]/product[2]
    product.append(ratio)
data.sort(reverse=True,key=lambda product: product[3])
print(data)

lenofdata=len(data)
kmax=maxcond
selectedlist=[]
totalprofit=0
for product in data:
    selectedin=[]
    if product[2]<=kmax:
        kmax=kmax-product[2]
        totalprofit=totalprofit+product[1]
        selectedin.append(product[0])
        selectedin.append(product[2])
    elif product[2]>kmax:
        profit=kmax*product[3]
        totalprofit=totalprofit+profit
        selectedin.append(product[0])
        selectedin.append(kmax)
        kmax = 0
    selectedlist.append(selectedin)

print("selected: "+str(selectedlist))
print(totalprofit)

