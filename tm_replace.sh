#!/bin/bash

# --- Configuration for HAIL ---
FILES1=("data/maps/ShoalCave_LowTideIceRoom/map.json" "include/constants/flags.h")
FIND1="TM_HAIL"
REPLACE1="TM_SNOWSCAPE"

for file in "${FILES1[@]}"; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        sed -i "s|${FIND1}|${REPLACE1}|g" "$file"
        echo "Replaced ${FIND1} with ${REPLACE1}"
    else
        echo "Error: File '$file' not found. Skipping."
    fi
done

# --- Configuration for HIDDEN_POWER ---
#FILES2=("data/maps/FortreeCity_House2/scripts.inc" "data/maps/SlateportCity/scripts.inc")
#FIND2="TM_HIDDEN_POWER"
#REPLACE2="TM_FLAMETHROWER"
#
#for file in "${FILES2[@]}"; do
#    if [ -f "$file" ]; then
#        echo "Processing $file..."
#        sed -i "s|${FIND2}|${REPLACE2}|g" "$file"
#        echo "Replaced ${FIND2} with ${REPLACE2}"
#    else
#        echo "Error: File '$file' not found. Skipping."
#    fi
#done

# --- Configuration for SAFEGUARD ---
FILE3="data/maps/LilycoveCity_DepartmentStore_4F/scripts.inc"
FIND3="TM_SAFEGUARD"
REPLACE3="TM_HAZE"

if [ -f "$FILE3" ]; then
    echo "Processing $FILE3..."
    sed -i "s|${FIND3}|${REPLACE3}|g" "$FILE3"
    echo "Replaced ${FIND3} with ${REPLACE3}"
else
        echo "Error: File '$FILE3' not found. Skipping."
fi

# --- Configuration for FRUSTRATION ---
FILE4="data/maps/PacifidlogTown_House2/scripts.inc"
FIND4="TM_FRUSTRATION"
REPLACE4="TM_CURSE"

if [ -f "$FILE4" ]; then
    echo "Processing $FILE4..."
    sed -i "s|${FIND4}|${REPLACE4}|g" "$FILE4"
    echo "Replaced ${FIND4} with ${REPLACE4}"
else
        echo "Error: File '$FILE4' not found. Skipping."
fi

# --- Configuration for IRON_TAIL ---
FILES5=("data/maps/MeteorFalls_1F_1R/map.json" "include/constants/flags.h")
FIND5="TM_IRON_TAIL"
REPLACE5="TM_IRON_HEAD"

for file in "${FILES5[@]}"; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        sed -i "s|${FIND5}|${REPLACE5}|g" "$file"
        echo "Replaced ${FIND5} with ${REPLACE5}"
    else
        echo "Error: File '$file' not found. Skipping."
    fi
done

# --- Configuration for RETURN ---
#FILES6=("data/maps/PacifidlogTown_House2/scripts.inc" "data/maps/FallarborTown_CozmosHouse/scripts.inc")
#FIND6="TM_RETURN"
#REPLACE6="TM_TERA_BLAST"
#
#for file in "${FILES6[@]}"; do
#    if [ -f "$file" ]; then
#        echo "Processing $file..."
#        sed -i "s|${FIND6}|${REPLACE6}|g" "$file"
#        echo "Replaced ${FIND6} with ${REPLACE6}"
#    else
#        echo "Error: File '$file' not found. Skipping."
#    fi
#done

# --- Configuration for DOUBLE_TEAM ---
FILES7=("data/maps/Route113/map.json" "data/maps/MauvilleCity_GameCorner/scripts.inc" "include/constants/flags.h")
FIND7="TM_DOUBLE_TEAM"
REPLACE7="TM_AGILITY"
FIND7_2="DoubleTeam"
REPLACE7_2="Agility"

for file in "${FILES7[@]}"; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        sed -i "s|${FIND7}|${REPLACE7}|g" "$file"
        echo "Replaced ${FIND7} with ${REPLACE7}"
        sed -i "s|${FIND7_2}|${REPLACE7_2}|g" "$file"
        echo "Replaced ${FIND7_2} with ${REPLACE7_2}"
    else
        echo "Error: File '$file' not found. Skipping."
    fi
done

# --- Configuration for SHOCK_WAVE ---
FILES8=("data/maps/MauvilleCity_Gym/scripts.inc" "include/constants/flags.h")
FIND8="TM_SHOCK_WAVE"
REPLACE8="TM_VOLT_SWITCH"
#FIND8_2="ShockWave"
#REPLACE8_2="VoltSwitch"
#FIND8_3="SHOCK WAVE"
#REPLACE8_3="VOLT SWITCH"

for file in "${FILES8[@]}"; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        sed -i "s|${FIND8}|${REPLACE8}|g" "$file"
        echo "Replaced ${FIND8} with ${REPLACE8}"
        #sed -i "s|${FIND8_2}|${REPLACE8_2}|g" "$file"
        #echo "Replaced ${FIND8_2} with ${REPLACE8_2}"
        #sed -i "s|${FIND8_3}|${REPLACE8_3}|g" "$file"
        #echo "Replaced ${FIND8_3} with ${REPLACE8_3}"
    else
        echo "Error: File '$file' not found. Skipping."
    fi
done

# --- Configuration for TORMENT ---
FILES9=("data/maps/SlateportCity_BattleTentLobby/scripts.inc" "include/constants/flags.h")
FIND9="TM_TORMENT"
REPLACE9="TM_TAUNT"

for file in "${FILES9[@]}"; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        sed -i "s|${FIND9}|${REPLACE9}|g" "$file"
        echo "Replaced ${FIND9} with ${REPLACE9}"
    else
        echo "Error: File '$file' not found. Skipping."
    fi
done

# --- Configuration for SECRET_POWER ---
#FILES10=("data/maps/SlateportCity/scripts.inc" "data/scripts/secret_power_tm.inc")
#FIND10="TM_SECRET_POWER"
#REPLACE10="TM_ENDEAVOR"
#
#for file in "${FILES10[@]}"; do
#    if [ -f "$file" ]; then
#        echo "Processing $file..."
#        sed -i "s|${FIND10}|${REPLACE10}|g" "$file"
#        echo "Replaced ${FIND10} with ${REPLACE10}"
#    else
#        echo "Error: File '$file' not found. Skipping."
#    fi
#done

# --- Configuration for ATTRACT ---
FILES11=("data/maps/VerdanturfTown_BattleTentLobby/scripts.inc" "include/constants/flags.h")
FIND11="TM_ATTRACT"
REPLACE11="TM_CHARM"

for file in "${FILES11[@]}"; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        sed -i "s|${FIND11}|${REPLACE11}|g" "$file"
        echo "Replaced ${FIND11} with ${REPLACE11}"
    else
        echo "Error: File '$file' not found. Skipping."
    fi
done

# --- Configuration for STEEL_WING ---
FILE12="data/maps/GraniteCave_StevensRoom/scripts.inc"
FIND12="TM_STEEL_WING"
REPLACE12="TM_SMART_STRIKE"
FIND12_2="STEEL WING"
REPLACE12_2="SMART STRIKE"

if [ -f "$FILE12" ]; then
    echo "Processing $FILE12..."
    sed -i "s|${FIND12}|${REPLACE12}|g" "$FILE12"
    echo "Replaced ${FIND12} with ${REPLACE12}"
    sed -i "s|${FIND12_2}|${REPLACE12_2}|g" "$FILE12"
    echo "Replaced ${FIND12_2} with ${REPLACE12_2}"
else
        echo "Error: File '$FILE12' not found. Skipping."
fi

# --- Configuration for SNATCH ---
FILES13=("data/maps/SSTidalRooms/scripts.inc" "data/maps/SSTidalCorridor/scripts.inc" "include/constants/flags.h")
FIND13="TM_SNATCH"
REPLACE13="TM_KNOCK_OFF"

for file in "${FILES13[@]}"; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        sed -i "s|${FIND13}|${REPLACE13}|g" "$file"
        echo "Replaced ${FIND13} with ${REPLACE13}"
    else
        echo "Error: File '$file' not found. Skipping."
    fi
done

echo "All replacement tasks completed."
