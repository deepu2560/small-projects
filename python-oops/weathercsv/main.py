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
print(data_dict["temp"].to_list())
