'''
from os import system
import ipaddress


print(''
      Proyecto Calculadora de redes. 
      Ingresa la IP que desea conocer.
      
      CLase     SubRedes       Host
      '')

ingreso = input()

def ip_calculator(ip_cidr):
    network = ipaddress.ip_network(ip_cidr, strict=False)

    # Determinar la clase de la IP
    first_octet = int(ip_cidr.split('.')[0])
    if 1 <= first_octet <= 126:
        ip_class = 'A'
    elif 128 <= first_octet <= 191:
        ip_class = 'B'
    elif 192 <= first_octet <= 223:
        ip_class = 'C'
    else:
        ip_class = 'Otra'

    # Calcular el número de subredes (para Clase A, B, C)
    if ip_class in ['A', 'B', 'C']:
        mask = network.prefixlen
        base_masks = {'A': 8, 'B': 16, 'C': 24}
        subnet_count = 2 ** (mask - base_masks[ip_class])    
    else:
        subnet_count = 'No aplicable'

    host_count = 2 ** (32 - network.prefixlen) - 2

    return f"Clase = {ip_class}, SubRedes = {subnet_count}, Hosts = {host_count}"

print(ip_calculator(ingreso))
'''

from ipaddress import ip_network

print(''' 
      Proyecto Calculadora de redes. 
      Ingresa la IP que desea conocer.
      
      ''')

ingreso = input()

def ip_calculator(ip_cidr):
    network = ip_network(ip_cidr, strict=False)
    netmask = network.netmask
    wildcard = network.hostmask
    network_address = network.network_address
    broadcast_address = network.broadcast_address
    host_min = list(network.hosts())[0]
    host_max = list(network.hosts())[-1]
    num_hosts = network.num_addresses - 2  # Excluye la dirección de red y broadcast

    # Convertir a formato binario
    def to_binary(ip):
        return '.'.join([format(int(octet), '08b') for octet in str(ip).split('.')])

    return (
        f"Address:    \t{network_address}\t{to_binary(network_address)}\n"
        f"Netmask:    \t{netmask} = {network.prefixlen}\t{to_binary(netmask)}\n"
        f"Wildcard:   \t{wildcard}\t{to_binary(wildcard)}\n"
        "=>\n"
        f"Network:    \t{network_address}/{network.prefixlen}\t{to_binary(network_address)}\n"
        f"HostMin:    \t{host_min}\t{to_binary(host_min)}\n"
        f"HostMax:    \t{host_max}\t{to_binary(host_max)}\n"
        f"Broadcast:  \t{broadcast_address}\t{to_binary(broadcast_address)}\n"
        f"Hosts/Net:  \t{num_hosts}\tClass {network_address.max_prefixlen - network.prefixlen}"
    )

print(ip_calculator(ingreso))

