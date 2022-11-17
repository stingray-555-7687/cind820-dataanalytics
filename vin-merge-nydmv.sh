#!/bin/sh

# Fix header of NYDMV-VIN-OUTPUT-ST- vin-decode.py generated files
# they were missing 'entry' column heading (leftmost column)

fixedheader="'entry', 'ORIG_VIN', 'ABS', 'ActiveSafetySysNote', 'AdaptiveCruiseControl', 'AdaptiveDrivingBeam', 'AdaptiveHeadlights', 'AdditionalErrorText', 'AirBagLocCurtain', 'AirBagLocFront', 'AirBagLocKnee', 'AirBagLocSeatCushion', 'AirBagLocSide', 'AutoReverseSystem', 'AutomaticPedestrianAlertingSound', 'AxleConfiguration', 'Axles', 'BasePrice', 'BatteryA', 'BatteryA_to', 'BatteryCells', 'BatteryInfo', 'BatteryKWh', 'BatteryKWh_to', 'BatteryModules', 'BatteryPacks', 'BatteryType', 'BatteryV', 'BatteryV_to', 'BedLengthIN', 'BedType', 'BlindSpotIntervention', 'BlindSpotMon', 'BodyCabType', 'BodyClass', 'BrakeSystemDesc', 'BrakeSystemType', 'BusFloorConfigType', 'BusLength', 'BusType', 'CAN_AACN', 'CIB', 'CashForClunkers', 'ChargerLevel', 'ChargerPowerKW', 'CoolingType', 'CurbWeightLB', 'CustomMotorcycleType', 'DaytimeRunningLight', 'DestinationMarket', 'DisplacementCC', 'DisplacementCI', 'DisplacementL', 'Doors', 'DriveType', 'DriverAssist', 'DynamicBrakeSupport', 'EDR', 'ESC', 'EVDriveUnit', 'ElectrificationLevel', 'EngineConfiguration', 'EngineCycles', 'EngineCylinders', 'EngineHP', 'EngineHP_to', 'EngineKW', 'EngineManufacturer', 'EngineModel', 'EntertainmentSystem', 'ErrorCode', 'ErrorText', 'ForwardCollisionWarning', 'FuelInjectionType', 'FuelTypePrimary', 'FuelTypeSecondary', 'GCWR', 'GCWR_to', 'GVWR', 'GVWR_to', 'KeylessIgnition', 'LaneCenteringAssistance', 'LaneDepartureWarning', 'LaneKeepSystem', 'LowerBeamHeadlampLightSource', 'Make', 'MakeID', 'Manufacturer', 'ManufacturerId', 'Model', 'ModelID', 'ModelYear', 'MotorcycleChassisType', 'MotorcycleSuspensionType', 'NCSABodyType', 'NCSAMake', 'NCSAMapExcApprovedBy', 'NCSAMapExcApprovedOn', 'NCSAMappingException', 'NCSAModel', 'NCSANote', 'NonLandUse', 'Note', 'OtherBusInfo', 'OtherEngineInfo', 'OtherMotorcycleInfo', 'OtherRestraintSystemInfo', 'OtherTrailerInfo', 'ParkAssist', 'PedestrianAutomaticEmergencyBraking', 'PlantCity', 'PlantCompanyName', 'PlantCountry', 'PlantState', 'PossibleValues', 'Pretensioner', 'RearAutomaticEmergencyBraking', 'RearCrossTrafficAlert', 'RearVisibilitySystem', 'SAEAutomationLevel', 'SAEAutomationLevel_to', 'SeatBeltsAll', 'SeatRows', 'Seats', 'SemiautomaticHeadlampBeamSwitching', 'Series', 'Series2', 'SteeringLocation', 'SuggestedVIN', 'TPMS', 'TopSpeedMPH', 'TrackWidth', 'TractionControl', 'TrailerBodyType', 'TrailerLength', 'TrailerType', 'TransmissionSpeeds', 'TransmissionStyle', 'Trim', 'Trim2', 'Turbo', 'VIN', 'ValveTrainDesign', 'VehicleDescriptor', 'VehicleType', 'WheelBaseLong', 'WheelBaseShort', 'WheelBaseType', 'WheelSizeFront', 'WheelSizeRear', 'Wheels', 'Windows'"
outfilename="NYDMV-VIN-OUTPUT-merged.csv"
echo "$fixedheader" > $outfilename
# merge every file
for f in $(ls NYDMV-VIN-OUTPUT-ST-*.csv)
do
    echo "Adding file: $f"
    tail -n+2 $f >> $outfilename
    # compress file
    gzip -v $f
done

