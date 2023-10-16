#!/usr/bin/python3

from bpfcc import BPF

text = """

#define KBUILD_MODENAME "filter"
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/in.h>
#include <linux/tcp.h>


int tcpfilter(struct xdp_md *ctx) 
{ 
    //bpf_trace_printk("got a packet\\n"); 
    void *data = (void *)(long)ctx->data; 
    void *data_end = (void *)(long)ctx->data_end; 
    struct ethhdr *eth = data; 
    if ((void*)eth + sizeof(*eth) <= data_end) 
    { 
        struct iphdr *ip = data + sizeof(*eth); 
        if ((void*)ip + sizeof(*ip) <= data_end) 
        { 
            
            //if (ip->protocol == IPPROTO_IP) 
            //{ 
                struct tcphdr *tcp = (void*)ip + sizeof(*ip); 
                if ((void*)tcp + sizeof(*tcp) <= data_end) 
                { 
                    bpf_trace_printk("tcp port %d \\n", htons(tcp->source)); 
                    
                    if (tcp->source == ntohs(84)) 
                    { 
                        bpf_trace_printk("tcp port 999\\n"); 
                        tcp->dest = ntohs(999); 
                    } 
                } 
            //} 
        } 
    } 
    return XDP_PASS; 
}
"""

device = "vethd91a1af3"
b = BPF(text=text)
fn = b.load_func("tcpfilter", BPF.XDP)
b.attach_xdp(device,fn, 0)


try:
    b.trace_print()
except KeyboardInterrupt:
    pass
b.remove_xdp(device,0)