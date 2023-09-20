#####################################################################################
# Author: 江河湖海小浪浪
# CreateTime: 2023-07-21
# Version: v0.1 Alpha
# Desc: 端口访问封禁工具，设置白名单，禁止名单外的IP访问名单内的端口
# eg: ./refusePortSeal [地址列表] [端口列表] [IPSet名称]
#     ./refusePortSeal 192.168.1.1,192.168.1.2,192.168.1.3 4444,5555,6666,7777 chineyanSet
# tel:
####################################################################################

#!/bin/bash

echo "programName: ${0}"

readonly ips=${1}
readonly ips_array=($(echo $ips | tr -d '[]' | tr ',' '\n'))
readonly ports=${2}
readonly ports_array=($(echo $ports | tr -d '[]' | tr ',' '\n'))
readonly ipset=${3}
ipset_create_result=`ipset create ${ipset} hash:ip`
echo "${ipset_create_result}"


for ip in "${ips_array[@]}"
do 
    echo "Add IP in Manager: ${ip}"
    ipset add ${ipset} ${ip}    
done

for port in "${ports_array[@]}"
do 
    echo "Add Port in Manager: ${port}"
    iptables -A INPUT -p tcp --dport ${port} -m set ! --match-set ${ipset} src -j DROP
    iptables -A INPUT -p udp --dport ${port} -m set ! --match-set ${ipset} src -j DROP
done

echo "iptables rule is ready !"

