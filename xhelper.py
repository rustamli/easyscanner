import re

def findSecondPartCityName(city, query, cities, ERROR, TO):
	for outerKeys in query:
		for secondKey in query[outerKeys]:
			if query[outerKeys][secondKey] == city:
				cityName = city + " " + secondKey
				if cityName in cities:
					city = cityName
					break
				else:
					if containsCity(secondKey, cities) == 'NULL':
						ERROR = True;
						break
					else:
						city = containsCity(secondKey, cities)
						break
				break
	return city, ERROR


def containsCity(string, table):
	result = "NULL"
	if len(string) > 3:
		for c in table:
			if string in c: 
				result = c
				break
	return result


def findFlights(sourceCity, destinationCity, depDate, table):
	FLAG = False
	NO_DATE = False

	flights = []
	if sourceCity == "":
		sourceCity = "edinburgh"
	if destinationCity == "":
		FLAG = True
	if depDate == "":
		NO_DATE = True
	for rows in table:
		if FLAG:
			if rows[0] == sourceCity:
				if NO_DATE:
					flights.append(rows)
				else:
					date = re.split('[\\s]+', rows[2])
					date = date[0].split('-')
					if depDate == date[1]:
						flights.append(rows)
		else:
			if rows[0] == sourceCity and rows[1] == destinationCity:
				if NO_DATE:
					flights.append(rows)
				else:
					date = re.split('[\\s]+', rows[2])
					date = date[0].split('-')
					if depDate == date[1]:
						flights.append(rows)

	flights.sort(key=lambda x: float(x[3]))
	return flights


def creatTable(FILE_DATASET):
	content = readFile(FILE_DATASET)
	lines = content.splitlines()

	table = [None] * (len(lines))

	for j in range(len(lines)):
		table[j] = [None] * (5)

	i = 0
	for line in lines:
		tokens = line.split(',')
		table[i] = tokens
		i += 1;
	return table

def readFile(filename):
	f = open(filename, 'r')
	try:
	    content = f.read()
	finally:
	    f.close()
	return content


