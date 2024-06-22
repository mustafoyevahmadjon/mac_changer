import subprocess

interface = "eth0"
new_mac = "00:22:22:22:22:22"

print("[+] Changing MAC address for " + interface + "to  new_mac" )

# subprocess.call("ifconfig")
# subprocess.call("ifconfig eth0 down", shell=True)
# subprocess.call("ifconfig eth0 hw ether 88:77:66:55:44:33", shell=True)
# subprocess.call("ifconfig eth0 up", shell=True)
# subprocess.call("ifconfig", shell=True)