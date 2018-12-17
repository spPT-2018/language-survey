#!/bin/bash

while read -r filename; do
  rm "$filename"
done <moved-repos.txt
