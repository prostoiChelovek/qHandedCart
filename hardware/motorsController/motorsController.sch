EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
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
$Comp
L Motor:Motor_DC M?
U 1 1 5F794D70
P 5000 3050
F 0 "M?" H 4842 2954 50  0000 R CNN
F 1 "Motor_DC" H 4842 3045 50  0000 R CNN
F 2 "" H 5000 2960 50  0001 C CNN
F 3 "~" H 5000 2960 50  0001 C CNN
	1    5000 3050
	-1   0    0    1   
$EndComp
Wire Wire Line
	5000 2750 4550 2750
Wire Wire Line
	4550 2750 4550 2950
Wire Wire Line
	4550 2950 4000 2950
Wire Wire Line
	5000 3250 4550 3250
Wire Wire Line
	4550 3250 4550 3050
Wire Wire Line
	4550 3050 4000 3050
$EndSCHEMATC
