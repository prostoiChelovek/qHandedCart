EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A3 16535 11693
encoding utf-8
Sheet 1 5
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Sheet
S 1250 1200 2750 2000
U 5F75D92C
F0 "one_dirver" 50
F1 "one_dirver.sch" 50
F2 "out_a" O R 4000 3050 50 
F3 "out_b" O R 4000 2950 50 
F4 "fwd" I R 4000 2750 50 
F5 "back" I R 4000 2650 50 
F6 "pwm" I R 4000 2550 50 
F7 "diag_a" O R 4000 2400 50 
F8 "diag_b" O R 4000 2300 50 
F9 "cs" O R 4000 2200 50 
F10 "bat" I R 4000 3150 50 
$EndSheet
Text HLabel 4000 2550 2    50   Input ~ 0
motor_right_front_pwm
Wire Wire Line
	4300 2950 4000 2950
Wire Wire Line
	4300 3050 4000 3050
Text HLabel 4000 2650 2    50   Input ~ 0
motor_right_front_back
Text HLabel 4000 2750 2    50   Input ~ 0
motor_right_front_fwd
Text HLabel 4000 2200 2    50   Output ~ 0
motor_right_front_cs
Text HLabel 4000 2300 2    50   Output ~ 0
motor_right_front_diag_b
Text HLabel 4000 2400 2    50   Output ~ 0
motor_right_front_diag_a
Text HLabel 14600 1650 2    50   Output ~ 0
motor_right_front_pwm
Text HLabel 15700 2600 2    50   Output ~ 0
motor_right_front_back
Text HLabel 14600 2650 2    50   Output ~ 0
motor_right_front_fwd
Text HLabel 12000 3050 0    50   Input ~ 0
motor_right_front_cs
Text HLabel 14600 3450 2    50   Input ~ 0
motor_right_front_diag_b
Text HLabel 15700 3250 2    50   Input ~ 0
motor_right_front_diag_a
$Comp
L power:GND #PWR0105
U 1 1 5F7FA8F7
P 11700 5200
F 0 "#PWR0105" H 11700 4950 50  0001 C CNN
F 1 "GND" H 11705 5027 50  0000 C CNN
F 2 "" H 11700 5200 50  0001 C CNN
F 3 "" H 11700 5200 50  0001 C CNN
	1    11700 5200
	1    0    0    -1  
$EndComp
Wire Wire Line
	11700 5200 11700 5150
Wire Wire Line
	11700 5150 12000 5150
$Comp
L power:+5V #PWR0106
U 1 1 5F7FCF51
P 11450 5450
F 0 "#PWR0106" H 11450 5300 50  0001 C CNN
F 1 "+5V" H 11465 5623 50  0000 C CNN
F 2 "" H 11450 5450 50  0001 C CNN
F 3 "" H 11450 5450 50  0001 C CNN
	1    11450 5450
	1    0    0    -1  
$EndComp
Wire Wire Line
	11450 5450 11450 5550
Wire Wire Line
	11450 5550 12000 5550
$Comp
L Connector:Screw_Terminal_01x02 J1
U 1 1 5F7F2610
P 1000 10650
F 0 "J1" H 918 10325 50  0000 C CNN
F 1 "batery_connector" H 918 10416 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 1000 10650 50  0001 C CNN
F 3 "~" H 1000 10650 50  0001 C CNN
	1    1000 10650
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0107
U 1 1 5F7F3543
P 1350 10700
F 0 "#PWR0107" H 1350 10450 50  0001 C CNN
F 1 "GND" H 1355 10527 50  0000 C CNN
F 2 "" H 1350 10700 50  0001 C CNN
F 3 "" H 1350 10700 50  0001 C CNN
	1    1350 10700
	1    0    0    -1  
$EndComp
Wire Wire Line
	1350 10700 1350 10650
Wire Wire Line
	1350 10650 1200 10650
Text HLabel 1200 10550 2    50   Output ~ 0
bat_front+
Text HLabel 4000 3150 2    50   Input ~ 0
bat_front+
$Comp
L arduino:Arduino_Due_Shield XA1
U 1 1 5F7F0EA5
P 13300 3500
F 0 "XA1" H 13300 1119 60  0000 C CNN
F 1 "Arduino_Due_Shield" H 13300 1013 60  0000 C CNN
F 2 "Arduino:Arduino_Due_Shield" H 14000 6250 60  0001 C CNN
F 3 "https://store.arduino.cc/arduino-due" H 14000 6250 60  0001 C CNN
	1    13300 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	12000 5550 12000 5450
Connection ~ 12000 5550
Connection ~ 12000 5450
Wire Wire Line
	12000 5450 12000 5350
Wire Wire Line
	12000 5150 12000 5050
Connection ~ 12000 5150
Connection ~ 12000 4850
Wire Wire Line
	12000 4850 12000 4750
Connection ~ 12000 4950
Wire Wire Line
	12000 4950 12000 4850
Connection ~ 12000 5050
Wire Wire Line
	12000 5050 12000 4950
$Comp
L Connector:Screw_Terminal_01x01 J2
U 1 1 5F88908C
P 4500 2950
F 0 "J2" H 4580 2992 50  0000 L CNN
F 1 "Screw_Terminal_01x01" H 4580 2901 50  0000 L CNN
F 2 "Connector_Pin:Pin_D1.3mm_L11.3mm_W2.8mm_Flat" H 4500 2950 50  0001 C CNN
F 3 "~" H 4500 2950 50  0001 C CNN
	1    4500 2950
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x01 J3
U 1 1 5F88A28E
P 4500 3050
F 0 "J3" H 4580 3092 50  0000 L CNN
F 1 "Screw_Terminal_01x01" H 4580 3001 50  0000 L CNN
F 2 "Connector_Pin:Pin_D1.3mm_L11.3mm_W2.8mm_Flat" H 4500 3050 50  0001 C CNN
F 3 "~" H 4500 3050 50  0001 C CNN
	1    4500 3050
	1    0    0    -1  
$EndComp
$Sheet
S 5900 1200 2750 2000
U 5F8AE603
F0 "sheet5F8AE5F8" 50
F1 "one_dirver.sch" 50
F2 "out_a" O R 8650 3050 50 
F3 "out_b" O R 8650 2950 50 
F4 "fwd" I R 8650 2750 50 
F5 "back" I R 8650 2650 50 
F6 "pwm" I R 8650 2550 50 
F7 "diag_a" O R 8650 2400 50 
F8 "diag_b" O R 8650 2300 50 
F9 "cs" O R 8650 2200 50 
F10 "bat" I R 8650 3150 50 
$EndSheet
Text HLabel 8650 2550 2    50   Input ~ 0
motor_left_front_pwm
Wire Wire Line
	8950 2950 8650 2950
Wire Wire Line
	8950 3050 8650 3050
Text HLabel 8650 2650 2    50   Input ~ 0
motor_left_front_back
Text HLabel 8650 2750 2    50   Input ~ 0
motor_left_front_fwd
Text HLabel 8650 2200 2    50   Output ~ 0
motor_left_front_cs
Text HLabel 8650 2300 2    50   Output ~ 0
motor_left_front_diag_b
Text HLabel 8650 2400 2    50   Output ~ 0
motor_left_front_diag_a
Text HLabel 8650 3150 2    50   Input ~ 0
bat_front+
$Comp
L Connector:Screw_Terminal_01x01 J6
U 1 1 5F8AE612
P 9150 2950
F 0 "J6" H 9230 2992 50  0000 L CNN
F 1 "Screw_Terminal_01x01" H 9230 2901 50  0000 L CNN
F 2 "Connector_Pin:Pin_D1.3mm_L11.3mm_W2.8mm_Flat" H 9150 2950 50  0001 C CNN
F 3 "~" H 9150 2950 50  0001 C CNN
	1    9150 2950
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x01 J7
U 1 1 5F8AE618
P 9150 3050
F 0 "J7" H 9230 3092 50  0000 L CNN
F 1 "Screw_Terminal_01x01" H 9230 3001 50  0000 L CNN
F 2 "Connector_Pin:Pin_D1.3mm_L11.3mm_W2.8mm_Flat" H 9150 3050 50  0001 C CNN
F 3 "~" H 9150 3050 50  0001 C CNN
	1    9150 3050
	1    0    0    -1  
$EndComp
$Sheet
S 1250 3650 2750 2000
U 5F8B7961
F0 "sheet5F8B7955" 50
F1 "one_dirver.sch" 50
F2 "out_a" O R 4000 5500 50 
F3 "out_b" O R 4000 5400 50 
F4 "fwd" I R 4000 5200 50 
F5 "back" I R 4000 5100 50 
F6 "pwm" I R 4000 5000 50 
F7 "diag_a" O R 4000 4850 50 
F8 "diag_b" O R 4000 4750 50 
F9 "cs" O R 4000 4650 50 
F10 "bat" I R 4000 5600 50 
$EndSheet
Text HLabel 4000 5000 2    50   Input ~ 0
motor_right_rear_pwm
Wire Wire Line
	4300 5400 4000 5400
Wire Wire Line
	4300 5500 4000 5500
Text HLabel 4000 5100 2    50   Input ~ 0
motor_right_rear_back
Text HLabel 4000 5200 2    50   Input ~ 0
motor_right_rear_fwd
Text HLabel 4000 4650 2    50   Output ~ 0
motor_right_rear_cs
Text HLabel 4000 4850 2    50   Output ~ 0
motor_right_rear_diag_a
Text HLabel 4000 5600 2    50   Input ~ 0
bat_rear+
$Comp
L Connector:Screw_Terminal_01x01 J4
U 1 1 5F8B7970
P 4500 5400
F 0 "J4" H 4580 5442 50  0000 L CNN
F 1 "Screw_Terminal_01x01" H 4580 5351 50  0000 L CNN
F 2 "Connector_Pin:Pin_D1.3mm_L11.3mm_W2.8mm_Flat" H 4500 5400 50  0001 C CNN
F 3 "~" H 4500 5400 50  0001 C CNN
	1    4500 5400
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x01 J5
U 1 1 5F8B7976
P 4500 5500
F 0 "J5" H 4580 5542 50  0000 L CNN
F 1 "Screw_Terminal_01x01" H 4580 5451 50  0000 L CNN
F 2 "Connector_Pin:Pin_D1.3mm_L11.3mm_W2.8mm_Flat" H 4500 5500 50  0001 C CNN
F 3 "~" H 4500 5500 50  0001 C CNN
	1    4500 5500
	1    0    0    -1  
$EndComp
$Sheet
S 5900 3650 2750 2000
U 5F8B7981
F0 "sheet5F8B7956" 50
F1 "one_dirver.sch" 50
F2 "out_a" O R 8650 5500 50 
F3 "out_b" O R 8650 5400 50 
F4 "fwd" I R 8650 5200 50 
F5 "back" I R 8650 5100 50 
F6 "pwm" I R 8650 5000 50 
F7 "diag_a" O R 8650 4850 50 
F8 "diag_b" O R 8650 4750 50 
F9 "cs" O R 8650 4650 50 
F10 "bat" I R 8650 5600 50 
$EndSheet
Text HLabel 8650 5000 2    50   Input ~ 0
motor_left_rear_pwm
Wire Wire Line
	8950 5400 8650 5400
Wire Wire Line
	8950 5500 8650 5500
Text HLabel 8650 5100 2    50   Input ~ 0
motor_left_rear_back
Text HLabel 8650 5200 2    50   Input ~ 0
motor_left_rear_fwd
Text HLabel 8650 4650 2    50   Output ~ 0
motor_left_rear_cs
Text HLabel 8650 4750 2    50   Output ~ 0
motor_left_rear_diag_b
Text HLabel 8650 4850 2    50   Output ~ 0
motor_left_rear_diag_a
Text HLabel 8650 5600 2    50   Input ~ 0
bat_rear+
$Comp
L Connector:Screw_Terminal_01x01 J8
U 1 1 5F8B7990
P 9150 5400
F 0 "J8" H 9230 5442 50  0000 L CNN
F 1 "Screw_Terminal_01x01" H 9230 5351 50  0000 L CNN
F 2 "Connector_Pin:Pin_D1.3mm_L11.3mm_W2.8mm_Flat" H 9150 5400 50  0001 C CNN
F 3 "~" H 9150 5400 50  0001 C CNN
	1    9150 5400
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x01 J9
U 1 1 5F8B7996
P 9150 5500
F 0 "J9" H 9230 5542 50  0000 L CNN
F 1 "Screw_Terminal_01x01" H 9230 5451 50  0000 L CNN
F 2 "Connector_Pin:Pin_D1.3mm_L11.3mm_W2.8mm_Flat" H 9150 5500 50  0001 C CNN
F 3 "~" H 9150 5500 50  0001 C CNN
	1    9150 5500
	1    0    0    -1  
$EndComp
Text HLabel 4000 4750 2    50   Output ~ 0
motor_right_rear_diag_b
Text HLabel 12000 3150 0    50   Input ~ 0
motor_left_front_cs
Text HLabel 12000 3250 0    50   Input ~ 0
motor_right_rear_cs
Text HLabel 12000 3350 0    50   Input ~ 0
motor_left_rear_cs
Text HLabel 14600 3950 2    50   Output ~ 0
motor_right_rear_fwd
Text HLabel 14600 2550 2    50   Output ~ 0
motor_left_rear_back
Text HLabel 14600 3150 2    50   Output ~ 0
motor_left_rear_fwd
Text HLabel 14600 3550 2    50   Input ~ 0
motor_right_rear_diag_b
Text HLabel 14600 3750 2    50   Input ~ 0
motor_right_rear_diag_a
Text HLabel 14600 1550 2    50   Output ~ 0
motor_left_front_pwm
Text HLabel 14600 1450 2    50   Output ~ 0
motor_right_rear_pwm
Text HLabel 14600 1350 2    50   Output ~ 0
motor_left_rear_pwm
$Comp
L Connector:Screw_Terminal_01x02 J10
U 1 1 5F8FE7B8
P 1850 10650
F 0 "J10" H 1768 10325 50  0000 C CNN
F 1 "batery_connector" H 1768 10416 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 1850 10650 50  0001 C CNN
F 3 "~" H 1850 10650 50  0001 C CNN
	1    1850 10650
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0120
U 1 1 5F8FE7BE
P 2200 10700
F 0 "#PWR0120" H 2200 10450 50  0001 C CNN
F 1 "GND" H 2205 10527 50  0000 C CNN
F 2 "" H 2200 10700 50  0001 C CNN
F 3 "" H 2200 10700 50  0001 C CNN
	1    2200 10700
	1    0    0    -1  
$EndComp
Wire Wire Line
	2200 10700 2200 10650
Wire Wire Line
	2200 10650 2050 10650
Text HLabel 2050 10550 2    50   Output ~ 0
bat_rear+
NoConn ~ 13050 900 
NoConn ~ 13150 900 
NoConn ~ 13250 900 
NoConn ~ 13350 900 
NoConn ~ 13450 900 
NoConn ~ 13550 900 
Text HLabel 14600 2750 2    50   Input ~ 0
motor_left_rear_diag_b
Text HLabel 14600 2950 2    50   Input ~ 0
motor_left_rear_diag_a
Text HLabel 14600 3350 2    50   Output ~ 0
motor_right_rear_back
Text HLabel 14600 1850 2    50   Input ~ 0
motor_left_front_diag_a
Text HLabel 14600 1950 2    50   Input ~ 0
motor_left_front_diag_b
Text HLabel 14600 1750 2    50   Output ~ 0
motor_left_front_fwd
Text HLabel 14600 2050 2    50   Output ~ 0
motor_left_front_back
$EndSCHEMATC
