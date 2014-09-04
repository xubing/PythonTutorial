#! #! /usr/bin/env Python
#-*- coding:utf-8-*-

#Module Using the module name you can access the functions
#from fibo import *  ＃这样可以倒入除下划线开头的命名。
#import study
import shutil
import os
import glob 
import re
import math
import random
import sys
import urllib
import urllib2
import smtplib
from datetime import date 

#daily file and directory management
#shutil.move(
#shutil.copy(

#glob module provides a function for making file lists from directory wildcard searches
#print glob.glob('*.py')
#print os.system('time 0:20')
#print os.getcwd()
        
# regular expression tools
re.findall(r'\bf[a-z]*','which foot or hand fell fastest')

#math
math.cos(math.pi/4.0)
random.choice(['apple','pear'])
random.sample(range(100),10)
random.randrange(6)

#Internet access
#urllib2 
for line in urllib2.urlopen('http://www.baidu.com'):
    print line
    if 'EST' in line or 'EDT' in line:
        print line

#smtplib
#server = smtplib.SMTP('localhost')
#server.sendmail('soothsayer@example.org', 'kcaesar@example.org',
#        """To: jcaesar@example.org
#        From: soothsayer@example.org
#        Beware the Ides of March.""")
#server.quit()


# Dates and Times
#The datetime module supplies classes for manipulating dates and times in both simple and complex ways

now =date.today()
print now

# Data Compression
#modules including: zlib, gzip, bz2,zipfile, and tarfile.

