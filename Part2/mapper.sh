#!/bin/bash

grep -n 'TagBased="False"' | awk -F'Name="|" Date' '{print $2}' 

