import subprocess

interface = input("enter the interface you want to change > ")
new_mac = input("enter new MAC Adress > ")

print("[+] Changing MAC address for " + interface + "to " + new_mac )

subprocess.call("ifconfig")
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig", shell=True)