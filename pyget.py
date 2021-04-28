import requests
import logging
import http.client as http_client

from datetime import datetime
from pathlib import PurePath

import argparse

url='https://pml.nist.gov/cuu/Constants/Table/allascii.txt'
fname=url.split('/')[-1]
p=PurePath(__file__).parent.joinpath(fname)
print(f'Saving file to {p}')

http_client.HTTPConnection.debuglevel=1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
#logging.getLogger().setLevel(logging.ERROR)
requests_log=logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
#requests_log.setLevel(logging.ERROR)
requests_log.propagate=True
#requests_log.propagate=False

data=requests.get(url)
print(f'status code: {data.status_code}') 
open(p, 'wb').write(data.content)
print('DONE')
