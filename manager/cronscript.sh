#!/bin/bash

docker exec system-db mysql -u root -proot -e "use system_data; insert into disk_stats (used ,free, timestamp) values (`df | grep 'sda1' | awk '{ print $3 }'`,`df | grep 'sda1' | awk '{ print $4 }'` , '`date '+%Y-%m-%d %H:%M:%S'`');"

docker exec system-db mysql -u root -proot -e "use system_data; insert into mem_stats (used ,free, timestamp) values (`free | grep 'Mem' | awk '{ print $3 }'`,`free | grep 'Mem' | awk '{ print $4 }'` , '`date '+%Y-%m-%d %H:%M:%S'`');"

docker exec system-db mysql -u root -proot -e "use system_data; insert into cpu_stats (idle, timestamp) values (`mpstat | grep 'all' | awk '{ print $13 }'`, '`date '+%Y-%m-%d %H:%M:%S'`');"


