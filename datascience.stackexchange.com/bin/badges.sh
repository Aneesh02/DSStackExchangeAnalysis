#!/bin/bash
echo -e '\n'
echo "The number of users per badge:"
cat Badges.xml | grep -n 'TagBased="False"' | awk -F'Name="|" Date' '{print $2}' | sort | uniq -c | sort -r
echo -e '\n'
echo "Total number of badges: "
cat Badges.xml | grep -n 'TagBased="False"' | awk -F'Name="|" Date' '{print $2}' | sort | uniq | wc -l