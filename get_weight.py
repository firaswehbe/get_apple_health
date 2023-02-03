#!/usr/bin/env python

# Export the data from Apple Health
# You will get an export.zip file
# Unzip that file. 
# You will get a bunch of files use export.xml and save it in input/
import tqdm
import xml.etree.ElementTree as ET 
myfilename = 'input/export.xml'
myweightfile = 'output/weights.csv'

itertree = ET.iterparse(myfilename)
myrecordstqdm = tqdm.tqdm(itertree, unit=' records', unit_scale=True)

with open(myweightfile,'w') as fh: 
    fh.write('Date,Weight,Source\n')
    for x in myrecordstqdm:
        myelement = x[1]
        # If you want weights from a specific sources remove or alter the last condition in the expression
        if myelement.tag == 'Record' and myelement.attrib['type'] == 'HKQuantityTypeIdentifierBodyMass' and myelement.attrib['sourceName'] == 'Renpho':
            fh.write(f"{myelement.attrib['startDate']},{myelement.attrib['value']},{myelement.attrib['sourceName']}\n")

