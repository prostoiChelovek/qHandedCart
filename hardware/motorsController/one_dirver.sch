EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 5
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
L Driver_Motor:VNH5019A-E U1
U 1 1 5F75DD74
P 3150 2750
AR Path="/5F75D92C/5F75DD74" Ref="U1"  Part="1" 
AR Path="/5F8AE603/5F75DD74" Ref="U?"  Part="1" 
AR Path="/5F8B37BB/5F75DD74" Ref="U?"  Part="1" 
AR Path="/5F8B37DB/5F75DD74" Ref="U?"  Part="1" 
AR Path="/5F8B7961/5F75DD74" Ref="U?"  Part="1" 
AR Path="/5F8B7981/5F75DD74" Ref="U?"  Part="1" 
F 0 "U?" H 3150 3531 50  0000 C CNN
F 1 "VNH5019A-E" H 3150 3440 50  0000 C CNN
F 2 "Package_SO:ST_MultiPowerSO-30" H 4050 2200 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vnh5019a-e.pdf" H 2700 3600 50  0001 C CNN
	1    3150 2750
	1    0    0    -1  
$EndComp
Text HLabel 3650 2650 2    50   Output ~ 0
out_a
Text HLabel 3650 2850 2    50   Output ~ 0
out_b
Wire Wire Line
	3150 3350 3250 3350
Wire Wire Line
	3250 3350 3250 3500
Connection ~ 3250 3350
Wire Wire Line
	3250 3350 3350 3350
$Comp
L Device:R R3
U 1 1 5F764A13
P 2500 2350
AR Path="/5F75D92C/5F764A13" Ref="R3"  Part="1" 
AR Path="/5F8AE603/5F764A13" Ref="R?"  Part="1" 
AR Path="/5F8B37BB/5F764A13" Ref="R?"  Part="1" 
AR Path="/5F8B37DB/5F764A13" Ref="R?"  Part="1" 
AR Path="/5F8B7961/5F764A13" Ref="R?"  Part="1" 
AR Path="/5F8B7981/5F764A13" Ref="R?"  Part="1" 
F 0 "R?" V 2293 2350 50  0000 C CNN
F 1 "1K" V 2384 2350 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2430 2350 50  0001 C CNN
F 3 "~" H 2500 2350 50  0001 C CNN
	1    2500 2350
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 5F765406
P 2500 2450
AR Path="/5F75D92C/5F765406" Ref="R4"  Part="1" 
AR Path="/5F8AE603/5F765406" Ref="R?"  Part="1" 
AR Path="/5F8B37BB/5F765406" Ref="R?"  Part="1" 
AR Path="/5F8B37DB/5F765406" Ref="R?"  Part="1" 
AR Path="/5F8B7961/5F765406" Ref="R?"  Part="1" 
AR Path="/5F8B7981/5F765406" Ref="R?"  Part="1" 
F 0 "R?" V 2293 2450 50  0001 C CNN
F 1 "1K" V 2384 2450 50  0001 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2430 2450 50  0001 C CNN
F 3 "~" H 2500 2450 50  0001 C CNN
	1    2500 2450
	0    1    1    0   
$EndComp
$Comp
L Device:R R5
U 1 1 5F7658F2
P 2500 2550
AR Path="/5F75D92C/5F7658F2" Ref="R5"  Part="1" 
AR Path="/5F8AE603/5F7658F2" Ref="R?"  Part="1" 
AR Path="/5F8B37BB/5F7658F2" Ref="R?"  Part="1" 
AR Path="/5F8B37DB/5F7658F2" Ref="R?"  Part="1" 
AR Path="/5F8B7961/5F7658F2" Ref="R?"  Part="1" 
AR Path="/5F8B7981/5F7658F2" Ref="R?"  Part="1" 
F 0 "R?" V 2293 2550 50  0001 C CNN
F 1 "1K" V 2384 2550 50  0001 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2430 2550 50  0001 C CNN
F 3 "~" H 2500 2550 50  0001 C CNN
	1    2500 2550
	0    1    1    0   
$EndComp
Text HLabel 2350 2350 0    50   Input ~ 0
fwd
Text HLabel 2350 2450 0    50   Input ~ 0
back
Text HLabel 2350 2550 0    50   Input ~ 0
pwm
$Comp
L Device:R R6
U 1 1 5F77E0ED
P 2500 2750
AR Path="/5F75D92C/5F77E0ED" Ref="R6"  Part="1" 
AR Path="/5F8AE603/5F77E0ED" Ref="R?"  Part="1" 
AR Path="/5F8B37BB/5F77E0ED" Ref="R?"  Part="1" 
AR Path="/5F8B37DB/5F77E0ED" Ref="R?"  Part="1" 
AR Path="/5F8B7961/5F77E0ED" Ref="R?"  Part="1" 
AR Path="/5F8B7981/5F77E0ED" Ref="R?"  Part="1" 
F 0 "R?" V 2293 2750 50  0001 C CNN
F 1 "1K" V 2384 2750 50  0001 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2430 2750 50  0001 C CNN
F 3 "~" H 2500 2750 50  0001 C CNN
	1    2500 2750
	0    1    1    0   
$EndComp
Text HLabel 2350 2750 0    50   Output ~ 0
diag_a
$Comp
L Device:R R7
U 1 1 5F781639
P 2500 2850
AR Path="/5F75D92C/5F781639" Ref="R7"  Part="1" 
AR Path="/5F8AE603/5F781639" Ref="R?"  Part="1" 
AR Path="/5F8B37BB/5F781639" Ref="R?"  Part="1" 
AR Path="/5F8B37DB/5F781639" Ref="R?"  Part="1" 
AR Path="/5F8B7961/5F781639" Ref="R?"  Part="1" 
AR Path="/5F8B7981/5F781639" Ref="R?"  Part="1" 
F 0 "R?" V 2293 2850 50  0001 C CNN
F 1 "1K" V 2384 2850 50  0001 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 2430 2850 50  0001 C CNN
F 3 "~" H 2500 2850 50  0001 C CNN
	1    2500 2850
	0    1    1    0   
$EndComp
Text HLabel 2350 2850 0    50   Output ~ 0
diag_b
$Comp
L power:GND #PWR0101
U 1 1 5F781B76
P 2350 3100
AR Path="/5F75D92C/5F781B76" Ref="#PWR0101"  Part="1" 
AR Path="/5F8AE603/5F781B76" Ref="#PWR?"  Part="1" 
AR Path="/5F8B37BB/5F781B76" Ref="#PWR?"  Part="1" 
AR Path="/5F8B37DB/5F781B76" Ref="#PWR?"  Part="1" 
AR Path="/5F8B7961/5F781B76" Ref="#PWR?"  Part="1" 
AR Path="/5F8B7981/5F781B76" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 2350 2850 50  0001 C CNN
F 1 "GND" H 2355 2927 50  0000 C CNN
F 2 "" H 2350 3100 50  0001 C CNN
F 3 "" H 2350 3100 50  0001 C CNN
	1    2350 3100
	1    0    0    -1  
$EndComp
Wire Wire Line
	2350 3100 2350 3050
Wire Wire Line
	2350 3050 2650 3050
$Comp
L Device:R R2
U 1 1 5F782890
P 2000 3750
AR Path="/5F75D92C/5F782890" Ref="R2"  Part="1" 
AR Path="/5F8AE603/5F782890" Ref="R?"  Part="1" 
AR Path="/5F8B37BB/5F782890" Ref="R?"  Part="1" 
AR Path="/5F8B37DB/5F782890" Ref="R?"  Part="1" 
AR Path="/5F8B7961/5F782890" Ref="R?"  Part="1" 
AR Path="/5F8B7981/5F782890" Ref="R?"  Part="1" 
F 0 "R?" H 2070 3796 50  0000 L CNN
F 1 "1.5K" H 2070 3705 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 1930 3750 50  0001 C CNN
F 3 "~" H 2000 3750 50  0001 C CNN
	1    2000 3750
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 5F783B44
P 1700 4050
AR Path="/5F75D92C/5F783B44" Ref="#PWR0102"  Part="1" 
AR Path="/5F8AE603/5F783B44" Ref="#PWR?"  Part="1" 
AR Path="/5F8B37BB/5F783B44" Ref="#PWR?"  Part="1" 
AR Path="/5F8B37DB/5F783B44" Ref="#PWR?"  Part="1" 
AR Path="/5F8B7961/5F783B44" Ref="#PWR?"  Part="1" 
AR Path="/5F8B7981/5F783B44" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 1700 3800 50  0001 C CNN
F 1 "GND" H 1705 3877 50  0000 C CNN
F 2 "" H 1700 4050 50  0001 C CNN
F 3 "" H 1700 4050 50  0001 C CNN
	1    1700 4050
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5F7841BA
P 1700 3600
AR Path="/5F75D92C/5F7841BA" Ref="R1"  Part="1" 
AR Path="/5F8AE603/5F7841BA" Ref="R?"  Part="1" 
AR Path="/5F8B37BB/5F7841BA" Ref="R?"  Part="1" 
AR Path="/5F8B37DB/5F7841BA" Ref="R?"  Part="1" 
AR Path="/5F8B7961/5F7841BA" Ref="R?"  Part="1" 
AR Path="/5F8B7981/5F7841BA" Ref="R?"  Part="1" 
F 0 "R?" V 1493 3600 50  0000 C CNN
F 1 "10K" V 1584 3600 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 1630 3600 50  0001 C CNN
F 3 "~" H 1700 3600 50  0001 C CNN
	1    1700 3600
	0    1    1    0   
$EndComp
Wire Wire Line
	1850 3600 2000 3600
Connection ~ 2000 3600
$Comp
L Device:C C1
U 1 1 5F784D90
P 1400 3750
AR Path="/5F75D92C/5F784D90" Ref="C1"  Part="1" 
AR Path="/5F8AE603/5F784D90" Ref="C?"  Part="1" 
AR Path="/5F8B37BB/5F784D90" Ref="C?"  Part="1" 
AR Path="/5F8B37DB/5F784D90" Ref="C?"  Part="1" 
AR Path="/5F8B7961/5F784D90" Ref="C?"  Part="1" 
AR Path="/5F8B7981/5F784D90" Ref="C?"  Part="1" 
F 0 "C?" H 1515 3796 50  0000 L CNN
F 1 "33nF" H 1515 3705 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric" H 1438 3600 50  0001 C CNN
F 3 "~" H 1400 3750 50  0001 C CNN
	1    1400 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	1550 3600 1400 3600
Wire Wire Line
	1400 3900 1400 3950
Wire Wire Line
	1400 3950 1700 3950
Wire Wire Line
	2000 3950 2000 3900
Wire Wire Line
	1700 4050 1700 3950
Connection ~ 1700 3950
Wire Wire Line
	1700 3950 2000 3950
Wire Wire Line
	1400 3600 1250 3600
Connection ~ 1400 3600
Text HLabel 1250 3600 0    50   Output ~ 0
cs
NoConn ~ 3650 2350
Wire Wire Line
	3150 2150 3150 1850
Text HLabel 3150 1850 1    50   Input ~ 0
bat
$Comp
L power:+5V #PWR0103
U 1 1 5F78A1BC
P 3350 1850
AR Path="/5F75D92C/5F78A1BC" Ref="#PWR0103"  Part="1" 
AR Path="/5F8AE603/5F78A1BC" Ref="#PWR?"  Part="1" 
AR Path="/5F8B37BB/5F78A1BC" Ref="#PWR?"  Part="1" 
AR Path="/5F8B37DB/5F78A1BC" Ref="#PWR?"  Part="1" 
AR Path="/5F8B7961/5F78A1BC" Ref="#PWR?"  Part="1" 
AR Path="/5F8B7981/5F78A1BC" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 3350 1700 50  0001 C CNN
F 1 "+5V" H 3365 2023 50  0000 C CNN
F 2 "" H 3350 1850 50  0001 C CNN
F 3 "" H 3350 1850 50  0001 C CNN
	1    3350 1850
	1    0    0    -1  
$EndComp
Wire Wire Line
	3350 1850 3350 2150
Wire Wire Line
	2500 3600 2500 3150
Wire Wire Line
	2500 3150 2650 3150
Wire Wire Line
	2000 3600 2500 3600
$Comp
L power:GND #PWR0104
U 1 1 5F794080
P 3250 3500
AR Path="/5F75D92C/5F794080" Ref="#PWR0104"  Part="1" 
AR Path="/5F8AE603/5F794080" Ref="#PWR?"  Part="1" 
AR Path="/5F8B37BB/5F794080" Ref="#PWR?"  Part="1" 
AR Path="/5F8B37DB/5F794080" Ref="#PWR?"  Part="1" 
AR Path="/5F8B7961/5F794080" Ref="#PWR?"  Part="1" 
AR Path="/5F8B7981/5F794080" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 3250 3250 50  0001 C CNN
F 1 "GND" H 3255 3327 50  0000 C CNN
F 2 "" H 3250 3500 50  0001 C CNN
F 3 "" H 3250 3500 50  0001 C CNN
	1    3250 3500
	1    0    0    -1  
$EndComp
$EndSCHEMATC
