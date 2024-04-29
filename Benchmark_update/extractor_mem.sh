#!/bin/bash
echo "genomes,disk,memory"
for file in bifrost_memory_*.txt; do
    # Extract the number from the file name using pattern matching
    number=$(echo "$file" | grep -oP '(?<=bifrost_memory_)\d+(?=.txt)')
    
    # Read the file and extract disk used and max memory in GB
    while IFS= read -r line; do
        if [[ $line == *"disk used ( KB )"* ]]; then
            disk_used_gb=$(echo "$line" | awk '{print $7}')
        fi
        if [[ $line == *"max memory ( KB )"* ]]; then
            max_memory_gb=$(echo "$line" | awk '{print $7}')
        fi
    done < "$file"
    
    echo "$number,$disk_used_gb,$max_memory_gb"
done
