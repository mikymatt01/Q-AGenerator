#!/bin/bash
comandi=(
    "docker compose up summarizer"
    "docker compose up question-generator"
    "docker compose up key-extractor"
    "docker compose up generate-distractors"
)
lunghezza=${#comandi[@]}
cwd=$(pwd)
echo "execute: ${cwd} ${comandi[0]}"
osascript -e "tell application \"Terminal\" to do script \"cd $cwd; ${comandi[0]}\""
sleep 200

echo "execute: ${cwd} ${comandi[1]}"
osascript -e "tell application \"Terminal\" to do script \"cd $cwd; ${comandi[1]}\""
sleep 200

echo "execute: ${cwd} ${comandi[2]}"
osascript -e "tell application \"Terminal\" to do script \"cd $cwd; ${comandi[2]}\""
sleep 200

echo "execute: ${cwd} ${comandi[3]}"
osascript -e "tell application \"Terminal\" to do script \"cd $cwd; ${comandi[3]}\""
