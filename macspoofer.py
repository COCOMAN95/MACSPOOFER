import subprocess
import random

def random_mac():
    return ':'.join([random.choice('0123456789ABCDEF') for x in range(6)])

def change_mac(interface, mac):
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['ifconfig', interface, 'up'])

interface = input("Enter the interface name (e.g. eth0): ")

new_mac = random_mac()

change_mac(interface, new_mac)

print("The new MAC address is " + new_mac)