#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:37:42 2019

@author: prakash
"""

import os
#import re
#import pyttsx3
import time
#import subprocess
from datetime import datetime
#import dateutil.relativedelta



def logfilecreator(name):
    comb = name+str(nwtime2nmbr())
    pth = os.getcwd()+'/ML Log/'
    combo = pth+comb+'.txt'
    if not  os.path.isfile(combo):
        f = open(combo,'w')
        f.close()
    return combo

def filecreator(name,pth):
    combo = pth+'/'+name+'.txt'
    if not  os.path.isfile(combo):
        f = open(combo,'w')
        f.close()
    return combo


def filecreatorw(name,detail,pth):
    
    #pth = '/Users/prakash/ML Log/'
    combo = pth+'/'+name+'.txt'
    if not  os.path.isfile(combo):
        f = open(combo,'w')
        f.close()
    with open(combo, 'a') as istr:
        ss=str(detail)+" \n"
        istr.writelines(ss)
    return combo

def pathcreator(name):
    nwtm = nwtime2nmbr()
    dt = str(numbr2dt(nwtm)).split()
    #print(type(dt))
    comb = str(int(nwtm))
    pth = os.getcwd()+'/ML Log/'
    combopth = pth+name+'/'+dt[0]+'/'+comb
    try:  
        os.makedirs(combopth)
    except OSError:
        print ("Creation of the directory %s failed" % combopth)
    else:  
        print ("Successfully created the directory %s " % combopth)

    return combopth

def nwtime2nmbr():
    nwdt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    now = time.mktime(time.strptime(nwdt, '%Y-%m-%d %H:%M:%S'))
    return now
    
def write2file(name,address):
    with open(address, 'a') as istr:
        ss=name+" \n"
        istr.writelines(ss)

def numbr2dt(val):
    dt = datetime.fromtimestamp(float(val))
    return dt


#print(logfilecreator('Prakash_'))
#print(pathcreator('LSTM Working'))
