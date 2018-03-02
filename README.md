
# Spiders
* The categories Spider searches for the urls of all the categories.  
* The pic Spider downloads all the product images of a particular category (starting from the urls  
listed in the start_urls attribute).  

# Pipelines
CustomImagesPipeline overrides the default ImagesPipeline functionality. It stores the images in  
dedicated folders for every item (product) after the download process has been completed.

# Disclaimer
Always respect the policy of the website and the restrictions of robots.txt.  
Change the USER_AGENT variable in settings.py to identify yourself (and your website). 