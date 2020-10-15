EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A3 16535 11693
encoding utf-8
Sheet 1 2
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
Text HLabel 9550 1250 2    50   Output ~ 0
motor_right_front_pwm
Text HLabel 9550 2450 2    50   Output ~ 0
motor_right_front_back
Text HLabel 9550 2550 2    50   Output ~ 0
motor_right_front_fwd
Text HLabel 6950 2950 0    50   Input ~ 0
motor_right_front_cs
Text HLabel 9550 3350 2    50   Input ~ 0
motor_right_front_diag_b
Text HLabel 9550 3250 2    50   Input ~ 0
motor_right_front_diag_a
$Comp
L power:GND #PWR0105
U 1 1 5F7FA8F7
P 6650 5100
F 0 "#PWR0105" H 6650 4850 50  0001 C CNN
F 1 "GND" H 6655 4927 50  0000 C CNN
F 2 "" H 6650 5100 50  0001 C CNN
F 3 "" H 6650 5100 50  0001 C CNN
	1    6650 5100
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 5100 6650 5050
Wire Wire Line
	6650 5050 6950 5050
$Comp
L power:+5V #PWR0106
U 1 1 5F7FCF51
P 6400 5350
F 0 "#PWR0106" H 6400 5200 50  0001 C CNN
F 1 "+5V" H 6415 5523 50  0000 C CNN
F 2 "" H 6400 5350 50  0001 C CNN
F 3 "" H 6400 5350 50  0001 C CNN
	1    6400 5350
	1    0    0    -1  
$EndComp
Wire Wire Line
	6400 5350 6400 5450
Wire Wire Line
	6400 5450 6950 5450
$Comp
L Connector:Screw_Terminal_01x02 J1
U 1 1 5F7F2610
P 1350 4200
F 0 "J1" H 1268 3875 50  0000 C CNN
F 1 "batery_connector" H 1268 3966 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 1350 4200 50  0001 C CNN
F 3 "~" H 1350 4200 50  0001 C CNN
	1    1350 4200
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0107
U 1 1 5F7F3543
P 1700 4250
F 0 "#PWR0107" H 1700 4000 50  0001 C CNN
F 1 "GND" H 1705 4077 50  0000 C CNN
F 2 "" H 1700 4250 50  0001 C CNN
F 3 "" H 1700 4250 50  0001 C CNN
	1    1700 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	1700 4250 1700 4200
Wire Wire Line
	1700 4200 1550 4200
Text HLabel 1550 4100 2    50   Output ~ 0
bat+
Text HLabel 4000 3150 2    50   Input ~ 0
bat+
$Comp
L arduino:Arduino_Due_Shield XA1
U 1 1 5F7F0EA5
P 8250 3400
F 0 "XA1" H 8250 1019 60  0000 C CNN
F 1 "Arduino_Due_Shield" H 8250 913 60  0000 C CNN
F 2 "Arduino:Arduino_Due_Shield" H 8950 6150 60  0001 C CNN
F 3 "https://store.arduino.cc/arduino-due" H 8950 6150 60  0001 C CNN
	1    8250 3400
	1    0    0    -1  
$EndComp
Wire Wire Line
	6950 5450 6950 5350
Connection ~ 6950 5450
Connection ~ 6950 5350
Wire Wire Line
	6950 5350 6950 5250
Wire Wire Line
	6950 5050 6950 4950
Connection ~ 6950 5050
Connection ~ 6950 4750
Wire Wire Line
	6950 4750 6950 4650
Connection ~ 6950 4850
Wire Wire Line
	6950 4850 6950 4750
Connection ~ 6950 4950
Wire Wire Line
	6950 4950 6950 4850
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
$EndSCHEMATC
