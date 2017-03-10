#!/bin/bash
while  read -r host || [[ -n "$host" ]]; do
        if [ ! -z "$host" ]; then
	node=$(knife node show $host 2>/dev/null)
	name=`echo -e "\r" $host`
	paste <(echo $name) <(echo "$node"|grep "Environment"|awk '{print $2}') <(echo "$node"|grep "Run List"|cut -f2 -d":"|tr -d " " ) -d "\t" 
        fi
done < "$1"

