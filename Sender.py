"""
 -- Run this on Android -- 
Usage : send X Y values of the accelometer
By    : @_hddananjaya
Ver   : 0.0.1
"""

import socket as skt 
import android, time

s= skt.socket()
host = skt.gethostname()
port = 5555

s.bind(("",port))
s.listen(5)
c, addr = s.accept()


droid = android.Android()
droid.startSensingTimed(1, 250)
time.sleep(1)
 
while 1:
   try:
      droid.readSensors().result
      data = droid.sensorsReadAccelerometer().result
      aX = data[0]
      aY = data[1] 
      
      sendData = str(aX)+","+str(aY)
      print (aX,aY)
      c.send(sendData.encode('utf8')) 
      time.sleep(0.1)
   
   except:
      c.close()
      droid.stopSensing()
      exit
