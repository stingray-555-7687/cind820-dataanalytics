# define libraries to use
import pandas as pd
import numpy as np
#from pathlib import Path
import requests,json
#import matplotlib.pyplot as plt
#%matplotlib inline
import time
import sys


#vinDf = pd.read_csv("tmp/NYDMV-VIN.csv")
#vinDf.columns = ["entry","ORIG_VIN"]

"""
print(dict(vinDf.head(10)))
dd = dict(vinDf.head(10))
print(type(dd['entry']))
print(dict(vinDf.head(10).values))
print(vinDf.head(10).values)
ll = vinDf.head(10).values
print(ll[0][0],ll[0][1])
"""

vpicFieldToKeep = [
	"ForwardCollisionWarning",
	"DynamicBrakeSupport",
	#"CrashImminentBraking",
	"CIB",
	#"PedestrianAutoEmergencyBraking",
	"PedestrianAutomaticEmergencyBraking",
	#"BlindSpotWarning",
	"BlindSpotMon",
	"BlindSpotIntervention",
	"LaneDepartureWarning",
	#"LaneKeepingAssistance",
	"LaneKeepSystem",
	"LaneCenteringAssistance",
	#"BackupCamera",
	"RearVisibilitySystem",
	"RearCrossTrafficAlert",
	"RearAutomaticEmergencyBraking",
	"ParkAssist",
	"DaytimeRunningLight",
	#"HeadlampLightSource",
	"LowerBeamHeadlampLightSource",
	#"SemiAutoHeadlampBeamSwitching",
	"SemiautomaticHeadlampBeamSwitching",
	"AdaptiveDrivingBeam",
	"AdaptiveCruiseControl",
	#"AntilockBrakeSystem",
	"ABS",
	#"ElectronicStabilityControl",
	"ESC",
	"TPMS",
	"TractionControl",
	#"AutoPedestrianAlertingSound",
	"AutomaticPedestrianAlertingSound",
	"VIN",
	"BodyClass",
	"Make",
	"MakeID",
	"Model",
	"ModelID",
	"ModelYear",
	"ErrorCode",
]

vinDf = pd.read_csv("tmp/NYDMV-VIN.csv")
vinDf.columns = ["entry","ORIG_VIN"]
#for x in vpicFieldToKeep:
#    vinDf[x] = None
vinDf.set_index("entry", inplace=True)
#vinDf.info(verbose=True)

url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/';
vinStep = np.int64(sys.argv[3])
vinRecords = vinDf.shape[0]
vinStart = np.int64(sys.argv[1])
vinStop = min(np.int64(sys.argv[2]),vinRecords)
print(vinStart,vinStop,vinStep,vinRecords)
fileName = f"tmp/NYDMV-VIN-OUTPUT-ST-{vinStart:08d}-{vinStop:08d}.csv"
#f = open("tmp/NYDMV-VIN-OUTPUT-ST-" + str(vinStart) + "-" + str(vinStop) + ".csv","w")
f = open(fileName,"w")
for idx in range(vinStart,vinStop,vinStep):
    print("Current index:",idx,round(idx/vinRecords*100,1),"%",end="\r")
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
            headerStr = str(list(vinDf.columns) + list(vpicResults[resIdx].keys()))
            f.write(headerStr[1:-1] + "\n")
        #print(vinDf.index[idx + resIdx],vinDf.iloc[idx + resIdx]["ORIG_VIN"],list(vpicResults[resIdx].values()))
        f.write(str(lstToPrint)[1:-1] + "\n")
    #    #rowLabel = vinDf.index[idx + resIdx]
    #    for x in vpicFieldToKeep:
    #        #vinDf.at[rowLabel,x] = vpicResults[resIdx][x]
    #        vinDf.iat[idx + resIdx,vinDf.columns.get_loc(x)] = vpicResults[resIdx][x]
    #        #print((rowLabel,x),(resIdx,x))
    
    #time.sleep(0.05)

#vinDf.to_csv("tmp/NYDMV-VIN-OUTPUT-99.csv",index=True)
