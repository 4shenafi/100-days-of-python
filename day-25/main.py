import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240904.csv")
# print(f'Average Temp: {data["Temperature (°C)"].mean()}')
# print(f'Max Temperature: {data["Temperature (°C)"].max()}')
# print(f'Min Temperature: {data["Temperature (°C)"].min()}')
# print(f'Median Temperature: {data["Temperature (°C)"].median()}')
# print(data[data.Temperature == data.Temperature.max()])
# print(data[data.Temperature == data.Temperature.max()].Day)

black_count = len(data[data["Primary Fur Color"] == "Black"])
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])


# print(f'Total colors are: Black: {black_count}, Gray: {gray_count}, Cinnamon: {cinnamon_count}')
Primary_Fur_Color = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [black_count, gray_count, cinnamon_count]
}

df = pandas.DataFrame(Primary_Fur_Color)
print(df)
df.to_csv("output.csv", index=True)
