import os
from bs4 import BeautifulSoup

execution_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(execution_dir, 'mphg.htm')


soup = BeautifulSoup(open(file_path))

# print soup.get_text()
print soup.prettify()