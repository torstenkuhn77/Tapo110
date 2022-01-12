import json

from PyP100 import PyP110

p110 = PyP110.P110("192.168.0.111", "torstenk@hotmail.de", ",Damokles1.") #Creating a P110 plug object

p110.handshake() #Creates the cookies required for further methods
p110.login() #Sends credentials to the plug and creates AES Key and IV for further methods

p110.turnOn() #Sends the turn on request

di = p110.getDeviceInfo() #Returns dict with all the device info

print ("Device Info")
print(di)

#PyP110 has all Pyp100 functions and additionally allows to query energy usage infos
e = p110.getEnergyUsage() #Returns dict with all the energy usage
#workaround getDeviceInfo returns decrypted payload not deserialized json via json.loads
if isinstance(e,str):
    eu = json.loads(e)
else:
    eu = e

print ("Energy Usage")
print (eu)

with open('device_info.json', 'w') as outfile:
    json.dump(di, outfile)
outfile.close()
with open('energy_usage.json', 'w') as outfile2:
    json.dump(eu, outfile2)
outfile2.close()

p110.turnOff() #Sends the turn off request