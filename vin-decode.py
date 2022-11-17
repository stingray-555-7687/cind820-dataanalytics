# define libraries to use
import pandas as pd
import numpy as np
import requests,json
import time
import sys

# decode VIN numbers in tmp/NYDMV-VIN.csv starting at a certain position until a stop position
# usage:
# /usr/bin/python3 ~/code/repo/cind820-dataanalytics/vin-decode.py <start> <stop> <step>

vinDf = pd.read_csv("tmp/NYDMV-VIN.csv")
vinDf.columns = ["entry","ORIG_VIN"]

vinDf.set_index("entry", inplace=True)

url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/';
vinStep = np.int64(sys.argv[3])
vinRecords = vinDf.shape[0]
vinStart = np.int64(sys.argv[1])
vinStop = min(np.int64(sys.argv[2]),vinRecords)
print(vinStart,vinStop,vinStep,vinRecords)
fileName = f"tmp/NYDMV-VIN-OUTPUT-ST-{vinStart:08d}-{vinStop:08d}.csv"
f = open(fileName,"w")
for idx in range(vinStart,vinStop,vinStep):
    print("Current index:",idx,round((idx-vinStart)/(vinStop-vinStart)*100,1),"%",end="")
    if idx + vinStep < vinRecords:
        vinsToCheck = vinDf.iloc[idx:idx+vinStep,0]
    else:
        vinsToCheck = vinDf.iloc[idx:,0]
    vinsToCheckStr = vinsToCheck.to_csv(None,index=False,line_terminator=';',header=False)[:-1] # eliminate last ';'
    #print(vinsToCheckStr)
    post_fields = {'format': 'json', 'data':vinsToCheckStr};
    #tic = time.perf_counter()
    r = requests.post(url, data=post_fields);
    #toc = time.perf_counter()
    #print(f"API call {toc - tic:0.4f} seconds")
    vpicResults = r.json()["Results"]
    # loop through resutls for every VIN

    for resIdx in range(0,len(vpicResults)):
        lstToPrint = [vinDf.index[idx + resIdx],vinDf.iloc[idx + resIdx]["ORIG_VIN"]] + list(vpicResults[resIdx].values())
        # if fist line the write column headings
        if idx == vinStart and resIdx == 0:
            headerStr = str(["entry","ORIG_VIN"] + list(vpicResults[resIdx].keys()))
            f.write(headerStr[1:-1] + "\n")
        #print(vinDf.index[idx + resIdx],vinDf.iloc[idx + resIdx]["ORIG_VIN"],list(vpicResults[resIdx].values()))
        f.write(str(lstToPrint)[1:-1] + "\n")
    print("",end="\r")

print()

