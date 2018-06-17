import csv, sys
filename = 'csv_sample.csv'
titles = []
years = []

with open(filename, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # remove header
    try:
        for row in reader:
            title = row[0]
            year = row[1]
            titles.append(title)
            years.append(year)

    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

print("\nTitles: ", titles)
print("\nDates: ", years)

whatMovie = input('\nWhat movie do you wish to know the date of?:')
coldex = years.index(whatMovie)
theMovie = titles[coldex]
print('The date of',whatMovie,'is:',theMovie)

########## Readin as a Dictionary:
print ("\n##################### Records as a Dictionary:\n")
with open("csv_sample.csv") as f:
    reader2 = csv.DictReader(f)
    data = [r for r in reader2]
print(data)
