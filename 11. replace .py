import pandas as pd

dataFrame = pd.read_excel('./excel file test.xlsx')
# print(dataFrame)

#### Replace
replace1 = dataFrame.replace(to_replace="Yes", value='Y')
# print(replace1)

replace2 = dataFrame.replace("Yes", 'Y')
# print(replace2)

replace3 = dataFrame.replace(10, 15)
# print(replace3)

replace3 = dataFrame.replace({'ID' : 10},22)
# print(replace3)

# total data er moddhy jeikhan a ai value gula pabey, seikhan a 0 bosabey
replace4 = dataFrame.replace([1,2,3,5,6,8,9,10], 0)
# print(replace4)

replace5 = dataFrame.replace([1,2,3,4,5,6,7,8,9,10], [11,12,13,14,15,16,17,18,19,20])
# print(replace5)


replace6 = dataFrame.replace("[A-Za-z]", 0, regex=True)
# print(replace6)

replace7 = dataFrame.replace({'PASS' : "[A-Za-z]"}, 0, regex=True)
print(replace7)


