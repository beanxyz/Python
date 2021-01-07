# with open("weather_data.csv",'r') as file:
#     content = file.readlines()
#     for each in content:
#         print(each)
#
#
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     print(data)
#     temp=[]
#     for row in data:
#         if row[1] == 'temp':continue
#         # print(row)
#         temp1=row[1]
#         print(temp1)
#         temp.append(int(temp1))
#
#     print(temp)

import pandas, math

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data.columns)

gray = data[data['Primary Fur Color'] == 'Gray']
cinnamon = data[data['Primary Fur Color'] == 'Cinnamon']
black = data[data['Primary Fur Color'] == 'Black']

print(f"gray:{len(gray)},cinnomon:{len(cinnamon)},black:{len(black)}")

result={
    "Fur Color":["gray","cinnomon","black"],
    "Count":[len(gray),len(cinnamon),len(black)]

}

data=pandas.DataFrame(result)
data.to_csv('squirrel_count.csv')





# print(data)
# print(data["condition"][1])

# data_dict= data.to_dict()
# print(data_dict)

#
# temp_list = data["temp"].to_list()
#
# print(sum(temp_list)/len(temp_list))
#
# print(data.condition)
#
# print(data[data.day == 'Monday'])
#
# # temp_list = data.temp.to_list()
# # max_temp = max(temp_list)
# print(data[data.temp == data.temp.max()])

#
# monday = data[data.day == 'Monday']
# print( monday.condition)

#
# data_dict={
#     "student":["Amy","James","Kein"],
#     "score": [23,45,33]
#
#
# }
#
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")



