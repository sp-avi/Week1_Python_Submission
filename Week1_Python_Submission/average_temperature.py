num = int(input("How many temperature readings? "))
temps = []

for i in range(num):
    temp = float(input(f"Enter temperature {i+1}: "))
    temps.append(temp)

average = sum(temps) / len(temps)
print(f"Average temperature: {average:.2f}°C")