# coding: utf - 8
import csv

# with open('/Users/sarahyang/Desktop/word1.csv') as f:
#     reader = csv.reader(f)
#     row1 = next(reader)  # gets the first line
# now do something here
# if first row is the header, then you can do one more next() to get the next row:
# row2 = next(f)
# print(row1)
if __name__ == '__main__':

    # with open('/Users/sarahyang/Desktop/word1.csv', 'r', encoding="utf-16") as csvfile:
    #     spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    try:
        f = open("/Users/sarahyang/Desktop/word1.csv", "r")
        data = f.read()
        array = data.split('\n')
        for arr in array:
            print(arr)
        f.close()
    except IOError as err:
        print(err)
