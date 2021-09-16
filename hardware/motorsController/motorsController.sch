EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Motor:Motor_DC M?
U 1 1 614246F8
P 5500 2000
F 0 "M?" V 5205 1950 50  0000 C CNN
F 1 "Motor_DC" V 5296 1950 50  0000 C CNN
F 2 "" H 5500 1910 50  0001 C CNN
F 3 "~" H 5500 1910 50  0001 C CNN
	1    5500 2000
	0    1    1    0   
$EndComp
Wire Wire Line
	4850 2400 4850 2000
Wire Wire Line
	4850 2000 5200 2000
$Comp
L IRF540NSTRLPBF:IRF540NSTRLPBF Q?
U 1 1 6142A096
P 4750 1400
F 0 "Q?" H 4958 1446 50  0000 L CNN
F 1 "IRF540NSTRLPBF" H 4958 1355 50  0000 L CNN
F 2 "TO254P1524X483-3N" H 4750 1400 50  0001 L BNN
F 3 "" H 4750 1400 50  0001 L BNN
F 4 "4.83 mm" H 4750 1400 50  0001 L BNN "MAXIMUM_PACKAGE_HEIGHT"
F 5 "3/18/04" H 4750 1400 50  0001 L BNN "PARTREV"
F 6 "IPC 7351B" H 4750 1400 50  0001 L BNN "STANDARD"
F 7 "Infineon" H 4750 1400 50  0001 L BNN "MANUFACTURER"
	1    4750 1400
	1    0    0    -1  
$EndComp
Wire Wire Line
	4850 1600 4850 2000
Connection ~ 4850 2000
Wire Wire Line
	6050 2400 6050 2000
Wire Wire Line
	6050 2000 5700 2000
$Comp
L IRF540NSTRLPBF:IRF540NSTRLPBF Q?
U 1 1 6143418A
P 6150 1400
F 0 "Q?" H 6358 1446 50  0000 L CNN
F 1 "IRF540NSTRLPBF" H 6300 1250 50  0000 L CNN
F 2 "TO254P1524X483-3N" H 6150 1400 50  0001 L BNN
F 3 "" H 6150 1400 50  0001 L BNN
F 4 "4.83 mm" H 6150 1400 50  0001 L BNN "MAXIMUM_PACKAGE_HEIGHT"
F 5 "3/18/04" H 6150 1400 50  0001 L BNN "PARTREV"
F 6 "IPC 7351B" H 6150 1400 50  0001 L BNN "STANDARD"
F 7 "Infineon" H 6150 1400 50  0001 L BNN "MANUFACTURER"
	1    6150 1400
	-1   0    0    -1  
$EndComp
Wire Wire Line
	6050 1600 6050 2000
Connection ~ 6050 2000
$Comp
L IRF540NSTRLPBF:IRF540NSTRLPBF Q?
U 1 1 614340B0
P 6150 2600
F 0 "Q?" H 6358 2646 50  0000 L CNN
F 1 "IRF540NSTRLPBF" H 6300 2475 50  0000 L CNN
F 2 "TO254P1524X483-3N" H 6150 2600 50  0001 L BNN
F 3 "" H 6150 2600 50  0001 L BNN
F 4 "4.83 mm" H 6150 2600 50  0001 L BNN "MAXIMUM_PACKAGE_HEIGHT"
F 5 "3/18/04" H 6150 2600 50  0001 L BNN "PARTREV"
F 6 "IPC 7351B" H 6150 2600 50  0001 L BNN "STANDARD"
F 7 "Infineon" H 6150 2600 50  0001 L BNN "MANUFACTURER"
	1    6150 2600
	-1   0    0    -1  
$EndComp
$Comp
L IRF540NSTRLPBF:IRF540NSTRLPBF Q?
U 1 1 61422DFF
P 4750 2600
F 0 "Q?" H 4958 2646 50  0000 L CNN
F 1 "IRF540NSTRLPBF" H 4958 2555 50  0000 L CNN
F 2 "TO254P1524X483-3N" H 4750 2600 50  0001 L BNN
F 3 "" H 4750 2600 50  0001 L BNN
F 4 "4.83 mm" H 4750 2600 50  0001 L BNN "MAXIMUM_PACKAGE_HEIGHT"
F 5 "3/18/04" H 4750 2600 50  0001 L BNN "PARTREV"
F 6 "IPC 7351B" H 4750 2600 50  0001 L BNN "STANDARD"
F 7 "Infineon" H 4750 2600 50  0001 L BNN "MANUFACTURER"
	1    4750 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	4850 2800 4850 2850
Wire Wire Line
	4850 2850 5450 2850
Wire Wire Line
	6050 2850 6050 2800
Wire Wire Line
	4850 1200 4850 1175
Wire Wire Line
	4850 1175 5450 1175
Wire Wire Line
	6050 1175 6050 1200
Wire Wire Line
	5450 2925 5450 2850
Connection ~ 5450 2850
Wire Wire Line
	5450 2850 6050 2850
$Comp
L power:+12V #PWR?
U 1 1 61446CAA
P 5450 1100
F 0 "#PWR?" H 5450 950 50  0001 C CNN
F 1 "+12V" H 5465 1273 50  0000 C CNN
F 2 "" H 5450 1100 50  0001 C CNN
F 3 "" H 5450 1100 50  0001 C CNN
	1    5450 1100
	1    0    0    -1  
$EndComp
Wire Wire Line
	5450 1100 5450 1175
Connection ~ 5450 1175
Wire Wire Line
	5450 1175 6050 1175
$Comp
L Driver_FET:IR2011 U?
U 1 1 61449045
P 3425 2000
F 0 "U?" H 3200 2550 50  0000 C CNN
F 1 "IR2011" H 3200 2450 50  0000 C CNN
F 2 "" H 3425 2000 50  0001 C CIN
F 3 "https://www.infineon.com/dgdl/ir2011.pdf?fileId=5546d462533600a4015355c49b831663" H 3425 2000 50  0001 C CNN
	1    3425 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	4375 2200 4375 1600
Wire Wire Line
	4375 1600 4850 1600
Connection ~ 4850 1600
Wire Wire Line
	3725 1800 4125 1800
Wire Wire Line
	4125 1800 4125 1500
$Comp
L Device:R R?
U 1 1 6144C40C
P 4425 1500
F 0 "R?" V 4218 1500 50  0000 C CNN
F 1 "R" V 4309 1500 50  0000 C CNN
F 2 "" V 4355 1500 50  0001 C CNN
F 3 "~" H 4425 1500 50  0001 C CNN
	1    4425 1500
	0    1    1    0   
$EndComp
Wire Wire Line
	4650 1500 4575 1500
Wire Wire Line
	4275 1500 4125 1500
$Comp
L Device:CP1 C?
U 1 1 6144F35E
P 3925 2050
F 0 "C?" H 4040 2096 50  0000 L CNN
F 1 "CP1" H 4040 2005 50  0000 L CNN
F 2 "" H 3925 2050 50  0001 C CNN
F 3 "~" H 3925 2050 50  0001 C CNN
	1    3925 2050
	1    0    0    -1  
$EndComp
Wire Wire Line
	3725 2200 3925 2200
Connection ~ 3925 2200
Wire Wire Line
	3925 2200 4375 2200
Wire Wire Line
	3925 1900 3925 1700
Wire Wire Line
	3925 1700 3725 1700
$Comp
L Device:D D?
U 1 1 61451DEE
P 3925 1550
F 0 "D?" V 3971 1470 50  0000 R CNN
F 1 "D" V 3880 1470 50  0000 R CNN
F 2 "" H 3925 1550 50  0001 C CNN
F 3 "~" H 3925 1550 50  0001 C CNN
	1    3925 1550
	0    -1   -1   0   
$EndComp
Connection ~ 3925 1700
Wire Wire Line
	3425 1500 3425 1375
Wire Wire Line
	3425 1375 3650 1375
Wire Wire Line
	3925 1375 3925 1400
Wire Wire Line
	3650 1375 3650 1275
Connection ~ 3650 1375
Wire Wire Line
	3650 1375 3925 1375
$Comp
L power:+5V #PWR?
U 1 1 61455E8B
P 3650 1275
F 0 "#PWR?" H 3650 1125 50  0001 C CNN
F 1 "+5V" H 3665 1448 50  0000 C CNN
F 2 "" H 3650 1275 50  0001 C CNN
F 3 "" H 3650 1275 50  0001 C CNN
	1    3650 1275
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 61456F19
P 4425 2700
F 0 "R?" V 4218 2700 50  0000 C CNN
F 1 "R" V 4309 2700 50  0000 C CNN
F 2 "" V 4355 2700 50  0001 C CNN
F 3 "~" H 4425 2700 50  0001 C CNN
	1    4425 2700
	0    1    1    0   
$EndComp
Wire Wire Line
	4650 2700 4575 2700
Wire Wire Line
	3725 2300 4125 2300
Wire Wire Line
	4125 2300 4125 2700
Wire Wire Line
	4125 2700 4275 2700
Wire Wire Line
	3425 2500 3425 2850
Wire Wire Line
	3425 2850 4850 2850
Connection ~ 4850 2850
$Comp
L Isolator:CPC-5002 U?
U 1 1 6145BE64
P 2225 2050
F 0 "U?" H 1950 2600 50  0000 C CNN
F 1 "CPC-5002" H 1950 2500 50  0000 C CNN
F 2 "Package_DIP:DIP-8_W7.62mm" H 2325 1330 50  0001 C CNN
F 3 "http://www.ixysic.com/home/pdfs.nsf/www/CPC5002.pdf" H 1825 2400 50  0001 C CNN
	1    2225 2050
	1    0    0    -1  
$EndComp
Wire Wire Line
	2525 1850 2800 1850
Wire Wire Line
	2800 1850 2800 2000
Wire Wire Line
	2800 2000 3125 2000
Wire Wire Line
	2525 2250 2800 2250
Wire Wire Line
	2800 2250 2800 2100
Wire Wire Line
	2800 2100 3125 2100
$Comp
L power:+5V #PWR?
U 1 1 61469578
P 2225 1450
F 0 "#PWR?" H 2225 1300 50  0001 C CNN
F 1 "+5V" H 2240 1623 50  0000 C CNN
F 2 "" H 2225 1450 50  0001 C CNN
F 3 "" H 2225 1450 50  0001 C CNN
	1    2225 1450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2225 1450 2225 1550
$Comp
L power:GNDPWR #PWR?
U 1 1 6146C0AF
P 2225 2625
F 0 "#PWR?" H 2225 2425 50  0001 C CNN
F 1 "GNDPWR" H 2229 2471 50  0000 C CNN
F 2 "" H 2225 2575 50  0001 C CNN
F 3 "" H 2225 2575 50  0001 C CNN
	1    2225 2625
	1    0    0    -1  
$EndComp
Wire Wire Line
	2225 2625 2225 2550
$Comp
L power:GND #PWR?
U 1 1 61471294
P 1650 2425
F 0 "#PWR?" H 1650 2175 50  0001 C CNN
F 1 "GND" H 1655 2252 50  0000 C CNN
F 2 "" H 1650 2425 50  0001 C CNN
F 3 "" H 1650 2425 50  0001 C CNN
	1    1650 2425
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 6146F754
P 1850 2425
F 0 "#PWR?" H 1850 2175 50  0001 C CNN
F 1 "GND" H 1855 2252 50  0000 C CNN
F 2 "" H 1850 2425 50  0001 C CNN
F 3 "" H 1850 2425 50  0001 C CNN
	1    1850 2425
	1    0    0    -1  
$EndComp
Wire Wire Line
	1850 2425 1850 2150
Wire Wire Line
	1850 2150 1925 2150
Wire Wire Line
	1650 2425 1650 1950
Wire Wire Line
	1650 1950 1925 1950
Wire Wire Line
	1925 2350 1500 2350
Wire Wire Line
	1925 1750 1500 1750
Text GLabel 1500 1750 0    50   Input ~ 0
AD
Text GLabel 1500 2350 0    50   Input ~ 0
BC
$Comp
L Driver_FET:IR2011 U?
U 1 1 61491A79
P 7475 2000
F 0 "U?" H 7250 2550 50  0000 C CNN
F 1 "IR2011" H 7250 2450 50  0000 C CNN
F 2 "" H 7475 2000 50  0001 C CIN
F 3 "https://www.infineon.com/dgdl/ir2011.pdf?fileId=5546d462533600a4015355c49b831663" H 7475 2000 50  0001 C CNN
	1    7475 2000
	-1   0    0    -1  
$EndComp
Wire Wire Line
	6525 2200 6525 1600
Wire Wire Line
	6525 1600 6050 1600
Wire Wire Line
	7175 1800 6775 1800
Wire Wire Line
	6775 1800 6775 1500
$Comp
L Device:R R?
U 1 1 61491CED
P 6475 1500
F 0 "R?" V 6268 1500 50  0000 C CNN
F 1 "R" V 6359 1500 50  0000 C CNN
F 2 "" V 6405 1500 50  0001 C CNN
F 3 "~" H 6475 1500 50  0001 C CNN
	1    6475 1500
	0    -1   1    0   
$EndComp
Wire Wire Line
	6250 1500 6325 1500
Wire Wire Line
	6625 1500 6775 1500
$Comp
L Device:CP1 C?
U 1 1 61491CF9
P 6975 2050
F 0 "C?" H 7090 2096 50  0000 L CNN
F 1 "CP1" H 7090 2005 50  0000 L CNN
F 2 "" H 6975 2050 50  0001 C CNN
F 3 "~" H 6975 2050 50  0001 C CNN
	1    6975 2050
	-1   0    0    -1  
$EndComp
Wire Wire Line
	7175 2200 6975 2200
Connection ~ 6975 2200
Wire Wire Line
	6975 2200 6525 2200
Wire Wire Line
	6975 1900 6975 1700
Wire Wire Line
	6975 1700 7175 1700
$Comp
L Device:D D?
U 1 1 61491D08
P 6975 1550
F 0 "D?" V 7021 1470 50  0000 R CNN
F 1 "D" V 6930 1470 50  0000 R CNN
F 2 "" H 6975 1550 50  0001 C CNN
F 3 "~" H 6975 1550 50  0001 C CNN
	1    6975 1550
	0    1    -1   0   
$EndComp
Connection ~ 6975 1700
Wire Wire Line
	7475 1500 7475 1375
Wire Wire Line
	7475 1375 7250 1375
Wire Wire Line
	6975 1375 6975 1400
Wire Wire Line
	7250 1375 7250 1275
Connection ~ 7250 1375
Wire Wire Line
	7250 1375 6975 1375
$Comp
L power:+5V #PWR?
U 1 1 61491D19
P 7250 1275
F 0 "#PWR?" H 7250 1125 50  0001 C CNN
F 1 "+5V" H 7265 1448 50  0000 C CNN
F 2 "" H 7250 1275 50  0001 C CNN
F 3 "" H 7250 1275 50  0001 C CNN
	1    7250 1275
	-1   0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 61491D23
P 6475 2700
F 0 "R?" V 6268 2700 50  0000 C CNN
F 1 "R" V 6359 2700 50  0000 C CNN
F 2 "" V 6405 2700 50  0001 C CNN
F 3 "~" H 6475 2700 50  0001 C CNN
	1    6475 2700
	0    -1   1    0   
$EndComp
Wire Wire Line
	6250 2700 6325 2700
Wire Wire Line
	7175 2300 6775 2300
Wire Wire Line
	6775 2300 6775 2700
Wire Wire Line
	6775 2700 6625 2700
Wire Wire Line
	7475 2500 7475 2850
Wire Wire Line
	7475 2850 6050 2850
$Comp
L Isolator:CPC-5002 U?
U 1 1 61491D33
P 8675 2050
F 0 "U?" H 8400 2600 50  0000 C CNN
F 1 "CPC-5002" H 8400 2500 50  0000 C CNN
F 2 "Package_DIP:DIP-8_W7.62mm" H 8775 1330 50  0001 C CNN
F 3 "http://www.ixysic.com/home/pdfs.nsf/www/CPC5002.pdf" H 8275 2400 50  0001 C CNN
	1    8675 2050
	-1   0    0    -1  
$EndComp
Wire Wire Line
	8375 1850 8100 1850
Wire Wire Line
	8100 1850 8100 2000
Wire Wire Line
	8100 2000 7775 2000
Wire Wire Line
	8375 2250 8100 2250
Wire Wire Line
	8100 2250 8100 2100
Wire Wire Line
	8100 2100 7775 2100
$Comp
L power:+5V #PWR?
U 1 1 61491D43
P 8675 1450
F 0 "#PWR?" H 8675 1300 50  0001 C CNN
F 1 "+5V" H 8690 1623 50  0000 C CNN
F 2 "" H 8675 1450 50  0001 C CNN
F 3 "" H 8675 1450 50  0001 C CNN
	1    8675 1450
	-1   0    0    -1  
$EndComp
Wire Wire Line
	8675 1450 8675 1550
$Comp
L power:GNDPWR #PWR?
U 1 1 61491D4E
P 8675 2625
F 0 "#PWR?" H 8675 2425 50  0001 C CNN
F 1 "GNDPWR" H 8679 2471 50  0000 C CNN
F 2 "" H 8675 2575 50  0001 C CNN
F 3 "" H 8675 2575 50  0001 C CNN
	1    8675 2625
	-1   0    0    -1  
$EndComp
Wire Wire Line
	8675 2625 8675 2550
$Comp
L power:GND #PWR?
U 1 1 61491D59
P 9250 2425
F 0 "#PWR?" H 9250 2175 50  0001 C CNN
F 1 "GND" H 9255 2252 50  0000 C CNN
F 2 "" H 9250 2425 50  0001 C CNN
F 3 "" H 9250 2425 50  0001 C CNN
	1    9250 2425
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 61491D63
P 9050 2425
F 0 "#PWR?" H 9050 2175 50  0001 C CNN
F 1 "GND" H 9055 2252 50  0000 C CNN
F 2 "" H 9050 2425 50  0001 C CNN
F 3 "" H 9050 2425 50  0001 C CNN
	1    9050 2425
	-1   0    0    -1  
$EndComp
Wire Wire Line
	9050 2425 9050 2150
Wire Wire Line
	9050 2150 8975 2150
Wire Wire Line
	9250 2425 9250 1950
Wire Wire Line
	9250 1950 8975 1950
Wire Wire Line
	8975 2350 9400 2350
Wire Wire Line
	8975 1750 9400 1750
Text GLabel 9400 1750 2    50   Input ~ 0
BC
Connection ~ 6050 1600
Connection ~ 6050 2850
Text GLabel 9400 2350 2    50   Input ~ 0
AD
$Comp
L IRF540NSTRLPBF:IRF540NSTRLPBF Q?
U 1 1 6148742F
P 5350 3125
F 0 "Q?" H 5558 3171 50  0000 L CNN
F 1 "IRF540NSTRLPBF" H 5558 3080 50  0000 L CNN
F 2 "TO254P1524X483-3N" H 5350 3125 50  0001 L BNN
F 3 "" H 5350 3125 50  0001 L BNN
F 4 "4.83 mm" H 5350 3125 50  0001 L BNN "MAXIMUM_PACKAGE_HEIGHT"
F 5 "3/18/04" H 5350 3125 50  0001 L BNN "PARTREV"
F 6 "IPC 7351B" H 5350 3125 50  0001 L BNN "STANDARD"
F 7 "Infineon" H 5350 3125 50  0001 L BNN "MANUFACTURER"
	1    5350 3125
	1    0    0    -1  
$EndComp
$Comp
L power:GNDPWR #PWR?
U 1 1 61492108
P 5450 3400
F 0 "#PWR?" H 5450 3200 50  0001 C CNN
F 1 "GNDPWR" H 5454 3246 50  0000 C CNN
F 2 "" H 5450 3350 50  0001 C CNN
F 3 "" H 5450 3350 50  0001 C CNN
	1    5450 3400
	1    0    0    -1  
$EndComp
Wire Wire Line
	5450 3400 5450 3325
$Comp
L eec:FAN3100TSX U?
U 1 1 6149F7E5
P 3100 3225
F 0 "U?" H 3650 3490 50  0000 C CNN
F 1 "FAN3100TSX" H 3650 3399 50  0000 C CNN
F 2 "ON_Semi-527AH-0-0-*" H 3100 3625 50  0001 L CNN
F 3 "http://www.onsemi.com/pub/Collateral/FAN3100T-D.PDF" H 3100 3725 50  0001 L CNN
F 4 "+125°C" H 3100 3825 50  0001 L CNN "ambient temperature range high"
F 5 "-40°C" H 3100 3925 50  0001 L CNN "ambient temperature range low"
F 6 "IC" H 3100 4025 50  0001 L CNN "category"
F 7 "Integrated Circuits (ICs)" H 3100 4125 50  0001 L CNN "device class L1"
F 8 "Power Management ICs" H 3100 4225 50  0001 L CNN "device class L2"
F 9 "Gate Drivers" H 3100 4325 50  0001 L CNN "device class L3"
F 10 "IC GATE DRVR SGL TTL 2A SOT23-5" H 3100 4425 50  0001 L CNN "digikey description"
F 11 "FAN3100TSXCT-ND" H 3100 4525 50  0001 L CNN "digikey part number"
F 12 "9ns" H 3100 4625 50  0001 L CNN "fall time"
F 13 "1.45mm" H 3100 4725 50  0001 L CNN "height"
F 14 "yes" H 3100 4825 50  0001 L CNN "lead free"
F 15 "67d593e38a04d9fa" H 3100 4925 50  0001 L CNN "library id"
F 16 "ON Semi" H 3100 5025 50  0001 L CNN "manufacturer"
F 17 "+150°C" H 3100 5125 50  0001 L CNN "max junction temp"
F 18 "18V" H 3100 5225 50  0001 L CNN "max supply voltage"
F 19 "4.5V" H 3100 5325 50  0001 L CNN "min supply voltage"
F 20 "512-FAN3100TSX" H 3100 5425 50  0001 L CNN "mouser part number"
F 21 "0.5mA" H 3100 5525 50  0001 L CNN "nominal supply current"
F 22 "1" H 3100 5625 50  0001 L CNN "number of drivers"
F 23 "1" H 3100 5725 50  0001 L CNN "number of outputs"
F 24 "3A" H 3100 5825 50  0001 L CNN "output current"
F 25 "SOT23-5" H 3100 5925 50  0001 L CNN "package"
F 26 "16ns" H 3100 6025 50  0001 L CNN "propagation delay"
F 27 "13ns" H 3100 6125 50  0001 L CNN "rise time"
F 28 "yes" H 3100 6225 50  0001 L CNN "rohs"
F 29 "0mm" H 3100 6325 50  0001 L CNN "standoff height"
F 30 "+125°C" H 3100 6425 50  0001 L CNN "temperature range high"
F 31 "-40°C" H 3100 6525 50  0001 L CNN "temperature range low"
	1    3100 3225
	1    0    0    -1  
$EndComp
$Comp
L power:GNDPWR #PWR?
U 1 1 614A413A
P 4200 3550
F 0 "#PWR?" H 4200 3350 50  0001 C CNN
F 1 "GNDPWR" H 4204 3396 50  0000 C CNN
F 2 "" H 4200 3500 50  0001 C CNN
F 3 "" H 4200 3500 50  0001 C CNN
	1    4200 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	4200 3550 4200 3525
Wire Wire Line
	4200 3525 4100 3525
Wire Wire Line
	4100 3225 5250 3225
$Comp
L power:GNDPWR #PWR?
U 1 1 614B7D39
P 3100 3550
F 0 "#PWR?" H 3100 3350 50  0001 C CNN
F 1 "GNDPWR" H 3104 3396 50  0000 C CNN
F 2 "" H 3100 3500 50  0001 C CNN
F 3 "" H 3100 3500 50  0001 C CNN
	1    3100 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	3100 3550 3100 3525
Wire Wire Line
	3100 3525 3200 3525
$Comp
L power:+12C #PWR?
U 1 1 614D176A
P 3100 3200
F 0 "#PWR?" H 3100 3050 50  0001 C CNN
F 1 "+12C" H 3115 3373 50  0000 C CNN
F 2 "" H 3100 3200 50  0001 C CNN
F 3 "" H 3100 3200 50  0001 C CNN
	1    3100 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	3100 3200 3100 3225
Wire Wire Line
	3100 3225 3200 3225
Text GLabel 3150 3425 0    50   Input ~ 0
PWM
Wire Wire Line
	3150 3425 3200 3425
$EndSCHEMATC
