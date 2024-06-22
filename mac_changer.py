import subprocess

interface = raw_input("enter the interface you want to change > ")
new_mac = raw_input("enter new MAC Adress > ")

print("[+] Changing MAC address for " + interface + "to " + new_mac )

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])