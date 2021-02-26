import itertools
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

    # Determining the number of products in the data. Binary production of all combinations
    # according to the specified number of products.

lenofdata=len(data)
combinations=list(itertools.product([0,1],repeat=lenofdata))

    # Creation of the combination list containing the total weight and profits of the combinations.

undermaxlist=[]
for combination in combinations:
    count=0
    sumprofcont=0
    sumkgcont=0
    listin=[]
    listinn=[]
    for combel in combination:
        if combel==1:
            sumprofcont=sumprofcont+data[count][1]
            sumkgcont=sumkgcont+data[count][2]
            listin.append(data[count][0])
        count=count+1
    listinn.append(listin)
    listinn.append(sumprofcont)
    listinn.append(sumkgcont)
    if sumkgcont<=maxcond:
        undermaxlist.append(listinn)

    # Determining the highest profit value from the combinations created

maxp=undermaxlist[0][1]
for undermax in undermaxlist:
    if maxp<=undermax[1]:
        maxp=undermax[1]

    # Determining the combinations with the highest profit

maxlist=[]
maxlistkg=[]
for undermax in undermaxlist:
    if maxp==undermax[1]:
        maxlist.append(undermax[0])
        maxlistkg.append(undermax[2])

    # Output of selected combinations and maximum profit

print("selected: "+str(maxlist))
print("profit: "+str(maxp))

kglist=[]
plist=[]
for undermax in undermaxlist:
    kglist.append(undermax[2])
    plist.append(undermax[1])
plt.scatter(kglist,plist,color="red")
for maxpkg in maxlistkg:
    plt.scatter(maxpkg,maxp,color="blue")
plt.ylabel("total profit ($)")
plt.xlabel("total weight (kilogramme)")
plt.title("Combination's Revenue and Profit Results for Basic Knapsack Problem")
plt.show()