#!/usr/bin/env python

#the above is a shebang
#good practive to do so

import requests

print(requests.__version__)


e = requests.get("https://www.google.com")
# change url to file getting raw conent of script

print(dir(e))

print(e.text)

print(e.status_code)




