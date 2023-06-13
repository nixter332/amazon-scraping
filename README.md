# Amazon-Scraping
Creating a web scraper and crawler to extract various book details from amazon.com into an external file format like json/csv.

# Webpage

![sample_webpage](https://github.com/nixter332/amazon-scraping/assets/97787214/e1cda256-32bd-4cfc-a917-64accab3e524)

# Installation
1. Create a virtual environment in the directory you want to store the project in.
2. Activate the environment.
3. Install scrapy.
4. Open your IDE of your choice and cd the directory the project is in. (Have used VSC but pycharm etc should work too)
5. Run this command in the terminal - scrapy startproject <project_name> (Scrapy will automatically create the required files for the project)
6. Create a new file in the spiders folder created or just copy in the code which has been uploaded in the code section (spidey.py)
7. Now run the following command to crawl the spider over the website - scrapy crawl <spider_name>
8. To output the data extracted into a json/csv file just add the following command after - scrapy crawl <spider_name> -o <file_name>.csv or .json
9. The desired output should have been created in the respective file format.

# Working

1. Input the starting url into the spider.
2. Define a parse function which will scrape the data of the webpage.
3. The parse function extracts the name, author, price and type of the book using various css selectors.
4. Yield the output using key-value pairs.
5. Now to crawl the website and move onto the next page, we get the split the url into parts and edit the page number using string function and concatonate the string to get the required url.
6. Increment the page_number each time.
7. We keep crawling for 11 pages but this limit can be changed as well.
8. Output the data into the required file format.

# Sample Output

Json File-

![sample_output](https://github.com/nixter332/amazon-scraping/assets/97787214/2ce4cb9e-9653-4638-9cd0-097da2573282)





