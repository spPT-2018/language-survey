#!/bin/bash

KEY=$(<key.conf)
USER=$(<user.conf)

repolist="/home/bolhuis/Projects/P9/full-list-names-only.txt"
destfolder="/home/bolhuis/Projects/P9/5krepos"
filerepo="$(echo "$repo" | tr / _)"
echo "Reponame: $filerepo"

while read p; do
    path="$destfolder/$(echo "$p" | tr / _).json"
    #echo "$path --> $p" #See if path and repo match somewhat
    touch "$path"

    curl -s -u "$USER:$KEY" "https://api.github.com/repos/$p/languages" >> "$path"
done <full-list-names-only.txt


