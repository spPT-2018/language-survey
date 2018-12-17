#!/bin/bash

KEY=$(<key.conf)
USER=$(<user.conf)

for y in {2014..2018} #Year
do
    for m in 0{1..9} {10..12} #Month
    do
        for i in {1..10} #Search page 1-10 provides 1k results (which is max)
        do
            echo "Crawling $y-$m page $i"
            curl -s -u "$USER:$KEY" "https://api.github.com/search/repositories?q=game+created:<$y-$m-01&sort=stars&per_page=100&page=$i" | jq -r '.["items"] | .[] | .html_url' >> gitcrawl.txt
            #curl -s -u "$USER:$KEY" "https://api.github.com/search/repositories?q=game+created:<$y-$m-01&sort=stars&per_page=100&page=$i" | jq -r '.["items"] | .[] | .html_url' >> gitcrawl.txt
            #curl -u "$USER:$KEY" "https://api.github.com/search/repositories?q=game&sort=stars&per_page=100&page=$i" | jq -r '.["items"] | .[] | .html_url' >> gitcrawl.txt
        done
    done
done

