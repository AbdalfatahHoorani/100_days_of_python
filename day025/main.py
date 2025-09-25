# # with open("./weather_data - Sheet1.csv") as data_file:
# #     raw_data = data_file.readlines()
# #
# # print(raw_data)
#
# import csv
#
# with open("./weather_data - Sheet1.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     i = 0
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#
#     # for temp in range(1,8):
#     #     number = int(list[temp][1])
#     #     temperatures.append(number)
#
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data - Sheet1.csv")
# type(data)


data_dic = data.to_dict()

# print(data_dic)

temp_list = data["temp"].to_list()

# total = 0
# t = 0
# for temp in temp_list:
#     total += temp
#     t += 1
#
# print(total/t)

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp  == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday["temp"] * 1.8 + 32)



