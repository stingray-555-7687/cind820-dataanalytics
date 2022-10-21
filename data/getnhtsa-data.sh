#!/bin/sh

# download NHSTA data
curl -O https://static.nhtsa.gov/nhtsa/downloads/FARS/2020/National/FARS2020NationalAuxiliaryCSV.zip
curl -O https://static.nhtsa.gov/nhtsa/downloads/FARS/2020/National/FARS2020NationalCSV.zip
curl -O https://static.nhtsa.gov/nhtsa/downloads/CRSS/2020/CRSS2020AuxiliaryCSV.zip
curl -O https://static.nhtsa.gov/nhtsa/downloads/CRSS/2020/CRSS2020CSV.zip
curl -O https://vpic.nhtsa.dot.gov/api/vPICList_lite_2022_09.bak.zip

# test zipped files
unzip -tq \*.zip

# extract data into individual directories
for f in $(ls *.zip)
do
    echo "Unzipping file: $f"
    mydir=$(basename $f .zip)
    mkdir $mydir
    unzip $f -d $mydir
done

# download NY vehicle registration data
mkdir nydmv
curl  -o nydmv/nydmv.csv "https://data.ny.gov/api/views/w4pv-hbkt/rows.csv?accessType=DOWNLOAD&sorting=true"


