import subprocess

subprocess.call("ifconfig")
subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 88:77:66:55:44:33", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
subprocess.call("ifconfig", shell=True)