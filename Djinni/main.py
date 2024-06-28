import requests
from bs4 import BeautifulSoup
from requests import get
import time
import random
import constant

jobs = []
count = 1

while count < 20:
    url = constant.URL + str(count)
    response = get(url=url)
    html_soup = BeautifulSoup(response.text, 'html')
    main_data = html_soup.find_all(constant.DIV, class_=constant.CLASS_CONTAINER)
    print(main_data)
    if main_data!=[]:
        print(main_data)
        value = random.randint(1, 10)
        time.sleep(value)
    else:
        print('Empty')
        break

    count += 1

# count = 0
# while count < 3:
#     info = jobs[int(count)]
#     print(info)
#     count += 1
#
