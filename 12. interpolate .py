import pandas as pd

dataFrame = pd.read_excel('my discharge water level data.xlsx')
# print(dataFrame)
# print(type(dataFrame.Date[0]))

# interpolate1 = dataFrame.interpolate()
# print(interpolate1)

# interpolate2 = dataFrame.interpolate( method='linear')
# print(interpolate2)



#### interpolate based on time
dataFrame1 = pd.read_excel('my discharge water level data.xlsx', parse_dates=['Date'], index_col= 'Date')

# print(type(dataFrame1.index[0]))

# interpolate3= dataFrame1.interpolate(method='time')
# print(interpolate3) 
# interpolate3= dataFrame1.interpolate(method='index')
# print(interpolate3) 


# Scipy needed to do this
# interpolate4 = dataFrame1.interpolate(method='cubic')
# print(interpolate4) 


