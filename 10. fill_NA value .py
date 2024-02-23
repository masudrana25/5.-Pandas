import pandas as pd
file = pd.read_excel("excel file test.xlsx")
# print(file)

fillWIthZero = file.fillna(0)
# print(fillWIthZero)

fillWithDifferentValues =  file.fillna({'NAME' : 'None', "MARKS":0, 'GRADE' : 'None', 'PASS' : 'No', 'FAIL' : 'Yes'})
# print(fillWithDifferentValues)


# ffill = foreward fill = ager value diye fill
# forewardFill = file.fillna(method='ffill')
forewardFill = file.fillna(method='pad')
# print(forewardFill)

# fill with previous rows value
fill = file.fillna(method = 'ffill', axis = 0) 
# print(fill)

# fill with previous column value
fill = file.fillna(method = 'ffill', axis = 1) 
print(fill)


#### Back Fill

# bfill = backward fill = porer value diye fill
backFill = file.fillna(method='bfill')
# print(backFill)

# fill with next rows value
fill = file.fillna(method = 'bfill', axis = 0) 
# print(fill)

# fill with next column value
fill = file.fillna(method = 'bfill', axis = 1) 
# print(fill)



#### limit
# fill limited null values
fill2 = file.fillna(method = 'bfill', axis = 1, limit =1) 
# print(fill2)


#### inplace = jei place a value nai, seikhan a true , value thakley false
# original file a e change korbey
fill3 = file
fill3.fillna(5555, inplace=True)
# print(fill3) 







