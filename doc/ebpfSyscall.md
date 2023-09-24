# EBPF

## 1.bpf系统调用

1. int bpf(int cmd, union bpf\_attr *attr, unsigned int size)

- cmd 确认EBPF的BPF\_PROG\_LOAD
- attr 允许数据可以在内核和用户空间传递
- size bpf\_attr的长度

## 2.eBPF程序类型

BPF\_PROG\_LOAD程序决定了四件事

1. 可以在何处附加程序
2. 可以调用验证程序的内核辅助程序
3. 是否可以直接访问网络数据包
4. 作为第一个传递的对象传递给执行参数

- BPF_PROG_TYPE_SOCKET_FILTER:网络数据包过滤器
- BPF_PROG_TYPE_KPROBE:确定是否应触发kprobe
- BPF_PROG_TYPE_SCHED_CLS:网络流量控制分类器
- BPF_PROG_TYPE_SCHED_ACT:网络流量控制操作
- BPF_PROG_TYPE_TRACEPOINT:确定是否应触发跟踪点
- BPF_PROG_TYPE_XDP:从设备驱动程序接收路径运行的网络数据包筛选器
- BPF_PROG_TYPE_PERF_EVENT:确定是否应该触发性能事件处理程序
- BPF_PROG_TYPE_CGROUP_SKB:用于控制组的网络数据包过滤器
- BPF_PROG_TYPE_CGROUP_SOCK:用于控制组的网络数据包筛选器，允许修改套接字选项
- BPF_PROG_TYPE_LWT_ :用于轻型隧道的网络数据包过滤器
- BPF_PROG_TYPE_SOCK_OPS:用于设置套接字参数的程序
- BPF_PROG_TYPE_SK_SKB:网络数据包过滤器，用于在套接字之间转发数据包
- BPF_PROG_CGROUP_DEVICE:确定是否应该允许设备操作


## 3.eBPF MAP数据结构

bpf_map_lookup_elem/bpf_map_update_elem 可以从eBPF或用户空间程序访问所有Map.

- BPF_MAP_TYPE_HASH：哈希表
- BPF_MAP_TYPE_ARRAY：数组映射，已针对快速查找速度进行了优化，通常用于计数器
- BPF_MAP_TYPE_PROG_ARRAY：对应eBPF程序的文件描述符数组；用于实现跳转表和子程序以处理特定的数据包协议
- BPF_MAP_TYPE_PERCPU_ARRAY：每个CPU的阵列，用于实现延迟的直方图
- BPF_MAP_TYPE_PERF_EVENT_ARRAY：存储指向struct perf_event的指针，用于读取和存储perf事件计数器
- BPF_MAP_TYPE_CGROUP_ARRAY：存储指向控制组的指针
- BPF_MAP_TYPE_PERCPU_HASH：每个CPU的哈希表
- BPF_MAP_TYPE_LRU_HASH：仅保留最近使用项目的哈希表
- BPF_MAP_TYPE_LRU_PERCPU_HASH：每个CPU的哈希表，仅保留最近使用的项目
- BPF_MAP_TYPE_LPM_TRIE：最长前缀匹配树，适用于将IP地址匹配到某个范围
- BPF_MAP_TYPE_STACK_TRACE：存储堆栈跟踪
- BPF_MAP_TYPE_ARRAY_OF_MAPS：表中表数组数据结构
- BPF_MAP_TYPE_HASH_OF_MAPS：表中hash表数据结构
- BPF_MAP_TYPE_DEVICE_MAP：用于存储和查找网络设备引用
- BPF_MAP_TYPE_SOCKET_MAP：存储和查找套接字，并允许使用BPF辅助函数进行套接字重定向

## 4.随内核版本演进过程

- 3.18 支持bpf系统调用
- 3.19 支撑套接字和BPFMap
- 4.1 支持kprobe
- 4.4 支持性能事件
- 4.6 支撑堆栈和CPU跟踪
- 4.7 支持跟踪点
- 4.8 支持XDP和行为
- 4.9
- 4.10 支持管理cgroups(套接字过滤)
- 4.11 添加跟踪点eBPF的调试模式 