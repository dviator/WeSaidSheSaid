#!/bin/bash

echo Cleaning Database.
python ./wesaidshesaid/db/CleanDatabase.py

echo Running Crawler in Background.
pushd ./wesaidshesaid/Crawler > /dev/null
scrapy crawl cspan &
popd > /dev/null

# when scrapy job is finished, let the user know
RUNNING=true
while [ $RUNNING ]; do
    if [ -z "$(pgrep scrapy)" ]
    then
        echo -ne "\n-I- WEB SCRAPING JOB COMPLETE\n"
        let RUNNING=false
        break
    fi 
done &
