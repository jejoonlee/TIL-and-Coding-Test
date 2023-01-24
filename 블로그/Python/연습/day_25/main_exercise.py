# with open("weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperature = []

#     for row in data:
#         if not row[1].isalpha():
#             temperature.append(int(row[1]))

#     print(temperature)

# import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }

# pandas.DataFrame(data_dict)

# # 월요일의 데이터들을 가지고 온다
# monday = data[data.day == "Monday"]

# # monday.temp를 통해, 월요일의 기온을 가지고 온다
# fahrenheit = (int(monday.temp) * 9/5) + 32

# print(fahrenheit)

# import pandas

# squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# grey = len(squirrel[squirrel["Primary Fur Color"] == 'Gray'])
# red = len(squirrel[squirrel["Primary Fur Color"] == 'Cinnamon'])
# black = len(squirrel[squirrel["Primary Fur Color"] == 'Black'])

# data_dict = {
#     "Fur Color" : ["grey", "red", "black"],
#     "Count" : [grey, red, black]
# }

# data_csv = pandas.DataFrame(data_dict)
# data_csv.to_csv("squirrel_count.csv")