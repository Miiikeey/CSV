
list_of_temps = []
f_obj = open("climate.csv")
#csv = f_obj.read()
header = f_obj.readline()
for line in f_obj:
    columns = line.split(",")
    if len(columns) >= 4:
        list_of_temps.append(columns[7])
print(list_of_temps)
list_of_numbers = []
for temp in list_of_temps:
    number = float(temp.replace('"', ""))
    list_of_numbers.append(number)

print(list_of_temps)
#print(csv)
#for linein in csv:
