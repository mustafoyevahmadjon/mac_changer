import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")
parser.parse_args()

interface = raw_input("enter the interface you want to change > ")
new_mac = raw_input("enter new MAC Adress > ")

print("[+] Changing MAC address for " + interface + "to " + new_mac )

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])