"# amazon-financial-helper" 


TODO: 
create a gui for fetching a source google sheet file locally or through link
and getting a target google sheet locally or through link. 

TODO: 
do for a list of ASIN and measure time taken. 
save output to a google sheet. 

This project is complete 
#Installation instructions 
1-clone the directory 
2-install miniconda or conda 
3-run "conda create --name amazonEnv --file requirements.txt" inside directory. 
4-"conda activate amazonEnv"
5-"python amazon-scraper.py"

#Features
1-fetches the column "asin" from any xlsx file in your computer and converts it to list. 
2-fetches each product page from amazon based on asin 
3-gets price and product name 
4-create a new excel file based on new data in following format (asin, product name, product link) 

ENJOY

