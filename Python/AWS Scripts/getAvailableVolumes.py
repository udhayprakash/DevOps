#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Purpose: To query the list of all volumes whose 'State' is 'Available', 
         and represent the volumes and their information in a csv file
"""


from boto3 import Session
from csv import DictWriter

session = Session(region_name = 'us-east-1')

def getAvailableVolumes():
    response = session.client('ec2').describe_volumes()

    AvailableVolumes = []
    for vol in response['Volumes']:
        if vol['State'] == 'available':
            AvailableVolumes.append(vol)

    with open('AvailableVolumes.csv', 'wb') as fileHandler:
        for aVol in AvailableVolumes:
            if len(aVol) == max([len(i) for i in AvailableVolumes]):
                fieldNames  = aVol.keys()
                break
        writer = DictWriter(fileHandler, fieldnames=fieldNames)
        writer.writeheader()
        for aVol in AvailableVolumes:
            writer.writerow(aVol)

try:
    getAvailableVolumes()
except Exception as ex:
    print "Exception Occurred: %s"%(ex)
