#--coding=utf-8
import re
import sys
import os

a='aasdfa12334d'
result = re.search(r"(\d)+",a)
if result !=None:
    print result
    print result.group(0)


