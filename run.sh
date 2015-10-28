#!/bin/bash

echo Cleaning Database.
python ./wesaidshesaid/db/CleanDatabase.py

echo Running Crawler in Background.
pushd ./wesaidshesaid/Crawler > /dev/null
scrapy crawl cspan &
popd > /dev/null

