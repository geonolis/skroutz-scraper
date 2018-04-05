
## Spiders
* The categories Spider searches for all the categories and saves the URLs in a .txt file.
* The pic Spider downloads all the product images of a particular category (starting from the urls  
listed in the start_urls attribute). You can modify start_urls attribute in pic.py to process 
more categories and the IMAGES_STORES attribute in settings.py to change the download location.

## Pipelines
CustomImagesPipeline overrides the default ImagesPipeline functionality. It stores the images in  
dedicated directories for every item (product) after the download process has been completed.

## Requirements
Skroutz-scraper requires Scrapy and Pillow in order to work.

## Disclaimer
Always respect the policy of the website and the restrictions of robots.txt.  
Change the USER_AGENT variable in settings.py to identify yourself (and your website).