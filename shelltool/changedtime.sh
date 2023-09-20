#!/bin/bash

# 设置要修改的时间  
target_time="2023-10-10 14:23:00"


# 转换 IP 地址为数组  
ip_list="192.168.13.110 192.168.13.111 192.168.13.112"

ip_array=( $(echo "$ip_list" | tr ' ' ' ') )
echo "IP数组地址 $ip_array"


# 遍历 IP 地址范围  
for ip in "${ip_array[@]}"; do  
  echo "尝试修改 IP: $ip 的时间..."  
  # 修改时间  
  sshpass -p "eicas@123" ssh root@$ip " timedatectl set-ntp no && date -s '$target_time'" 
  if [ $? -eq 0 ]; then  
    echo "修改成功：$ip"  
  else  
    echo "修改失败：$ip"  
  fi  
done  
