import os

path = os.path.dirname(__file__).replace('\\', '/')
print(type(path), path)
# jupyter notebook 에서는 __file__

crawled_folder = path + '/crawled_data/test_data'
os.makedirs(crawled_folder, exist_ok=True)
