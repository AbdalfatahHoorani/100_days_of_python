import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250816.csv")

data_list = data["Primary Fur Color"].to_list()


gray_count = 0
cinnamon_count = 0
black_count = 0
for color in data_list:

    if color == "Gray":
        gray_count += 1
    elif color == "Black":
        black_count += 1
    elif color == "Cinnamon":
        cinnamon_count += 1


# print(f"there are {gray_count} gray squirrels.")
# print(f"there are {cinnamon_count} gray squirrels.")
# print(f"there are {black_count} black squirrels.")

data_dict = {
    "Fur colour": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count],

}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
