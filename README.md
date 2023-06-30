# Amazon-financial-helper
## Completed 

## TODO: 
- [X] read from an excel sheet and write to an excel sheet
- [ ] create a gui for fetching a source google sheet file locally or through link
- [ ] getting a target google sheet locally or through link.  
- [ ] do for a list of ASIN and measure time taken. 
- [ ] save output to a google sheet.
- [ ] put this up as extension or website

## Installation instructions 
1. clone the directory 
2. install miniconda or conda 
3. run "conda create --name amazonEnv --file requirements.txt" inside directory. 
4. "conda activate amazonEnv"
5. "python amazon-scraper.py"

## Features
1. fetches the column "asin" from any xlsx file in your computer and converts it to list. 
2. fetches each product page from amazon based on asin 
3. gets price and product name 
4. create a new excel file based on new data in following format (asin, product name, product link) 

ENJOY

