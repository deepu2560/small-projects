# with open("./weather_data.csv") as weatherData:
#     data = weatherData.readlines()

# import csv
#
# with open("weather_data.csv") as weatherData:
#     data = csv.reader(weatherData)
#     temperature = []
#     for x in data:
#         if x[1] != "temp":
#             temperature.append(int(x[1]))
#
#     print(temperature)

import pandas

weatherData = pandas.read_csv("weather_data.csv")
# print(weatherData["temp"])

data_dict = weatherData.to_dict()
# print(data_dict)

temp_list = weatherData["temp"].to_list()
# print(temp_list)

average_weather = sum(temp_list)/len(temp_list)
# print(round(average_weather))

mean_weather = weatherData["temp"].mean()
# print(mean_weather)

max_weather = weatherData["temp"].max()
# print(max_weather)

# print(weatherData["condition"])
# print(weatherData.condition)

# getting rows
# print(weatherData[weatherData.day == "Monday"])
# print(weatherData[weatherData.temp == weatherData["temp"].max()])

