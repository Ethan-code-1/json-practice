#!/bin/bash 

curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" | jq -r '.[:6] | .[].receiptTime'
#Opted for more concise indexing method and added silent flag to hide curl feedback


