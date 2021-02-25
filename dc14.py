# Defanging an IP Address
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
#
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
#
# Source: https://leetcode.com/problems/defanging-an-ip-address/

def defang(ip):
    new_ip = str(ip).replace('.','[.]')
    return new_ip


defanged_ip = defang("255.100.50.0")
print(defanged_ip)
