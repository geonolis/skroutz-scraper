import os
import os.path
import shutil
import re
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class CustomImagesPipeline(ImagesPipeline):

    def make_path(self, path):
        # Create the folders if they don't exist
        if not os.path.exists(path):
            os.makedirs(path)

    def item_completed(self, results, item, info):
        for r in results:
            relative_path = r[1]['path']  # The filename
            IMAGES_STORE = get_project_settings().get("IMAGES_STORE")
            source_path = os.path.join(IMAGES_STORE, relative_path)
            product_name = item['product_name'].replace('/', '-')
            # Replace some special characters
            product_name = re.sub("[\:*?<>|\"]", "", product_name)
            dest_path = os.path.join(IMAGES_STORE, 'full', product_name)
            self.make_path(dest_path)
            # Move the images downloaded for this item in a new dedicated directory
            shutil.move(source_path, dest_path)
        return item
