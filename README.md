# Kalimati Scraping

This repository contains the code to scrape the [kalimati] which has daily prices of different vegetables and fruits in Nepal's one of the biggest market. First simple price list was scrpaed from the website. The obtained data was then stored in the csv file. Scraping was done with the help of [Scrapy] which is the python library for web scraping. Scraped data has item like product name (in nepali), minimum price, maximum price and average price. Then the price was converted in english value since it was originally in nepali.

[kalimati]:https://kalimatimarket.gov.np/
[Scrapy]: https://scrapy.org/
