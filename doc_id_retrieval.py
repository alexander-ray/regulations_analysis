from urllib.request import urlopen
from urllib.error import HTTPError
import json
import pandas as pd

tmp_url = 'https://www.regulations.gov/exportdocket?docketId=BIS-2018-0006'

try:
    response = urlopen(tmp_url)
    content = response.read()
except HTTPError as e:
    if e.getcode() == 500:
        content = e.read()
        print(content)
    else:
        raise
