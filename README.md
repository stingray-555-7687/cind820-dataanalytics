# cind820 Data Analytics Project Fall 2022

# Data Sources

## NHSTA Fatality Analisys Report System (FARS)

https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars

FARS 2020 Data:
https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/2020/National/

## NHSTA Crash Report Sampling System (CRSS)

https://www.nhtsa.gov/crash-data-systems/crash-report-sampling-system

CRSS 2020 Data:
https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/CRSS/2020/

## New York State Vehicle, Snowmobile, and Boat Registrations

https://data.ny.gov/Transportation/Vehicle-Snowmobile-and-Boat-Registrations/w4pv-hbkt


## NHSTA VIN decoder API

https://vpic.nhtsa.dot.gov/api/

New standalone database: "[vPICList]" updated on 9/17/2022, file size: 158 MB

[vPICList]: https://vpic.nhtsa.dot.gov/api/vPICList_lite_2022_09.bak.zip

Covert MS SQL 2012 back to csv:
```
curl -F 'files[]=@vPICList_lite_2022_09.bak/vPICList_lite_2022_09.bak' 'https://www.rebasedata.com/api/v1/convert?outputFormat=csv&errorResponse=zip' -o output.zip
```
or using docker as follows: https://gist.github.com/llimllib/f0b869c66f4487fcf8af4e8194c39993

