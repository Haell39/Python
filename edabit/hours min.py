def convert(hours, minutes):
	secoundsH = hours * 3600
	secoundsM = minutes * 60
	sum = secoundsH + secoundsM
	return sum



a = int(input("Type an hour: "))
b = int(input("Type minutes: "))

print(convert(a, b))
	