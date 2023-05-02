# importing libraries
import csv
import googletrans
from googletrans import *

# making the instance og google trnaslator class 
translator = googletrans.Translator()

with open('scrapedData/5-02.csv') as file:
    lines = csv.reader(file, delimiter=',')
    line_length = 0
    for line in lines:

        if line_length == 0:
           line_length += 1
           with open('cleanData/2023-5-02.csv',mode='w') as tfile:
               writer = csv.writer(tfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
               writer.writerow(line)

        # if line_length <= 86:
        #     line_length +=1


        else:

            minprice = translator.translate(line[1], dest='en',src='nepali').text
            maxprice = translator.translate(line[2], dest='en',src='nepali').text
            avgprice = translator.translate(line[3], dest='en',src='nepali').text

            # print(line[0],minprice, maxprice, avgprice)
            # break


            with open('cleanData/2023-5-02.csv',mode='a') as tfile:
                writer = csv.writer(tfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([line[0],minprice,maxprice,avgprice])


            