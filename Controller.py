"""
 -- Run this on PC -- 
Usage : press A D W S keys according to X Y values
By    : @_hddananjaya
"""

import socket,time            
from directkeys import *
import threading

# assign hex vals
S = 0x1F
W = 0x11
A = 0x1E
D = 0x20

aY = 0
aX = 0

def controlTurning(aY):
   if (aY > -1.2 and aY < 1.2):
      #print ("no turn "+str(aY))
      try:
         ReleaseKey(A)
         ReleaseKey(D)
      except:
         pass
   
   elif (aY < -1.2):    
      PressKey(A)
      time.sleep(abs(aY)*0.01)
      ReleaseKey(A)

   elif (aY > 1.2):  
      PressKey(D)
      time.sleep(abs(aY)*0.01)
      ReleaseKey(D)
         
def controlGasAndBreak(aX):
   if (aX > -0.7 and aX < 1.7):
      #print ("no gas "+str(aX))
      try:
         ReleaseKey(W)
         ReleaseKey(S)
      except:
         pass
      
   elif (aX < -0.7):    
      PressKey(W)
      time.sleep(abs(aY)*0.01)
      ReleaseKey(S)
      
   elif (aX > 1.9):  
      PressKey(S)
      time.sleep(abs(aY)*0.01)
      ReleaseKey(W)

def main():
 
   # wait till user ready
   time.sleep(5) 

   HOST = "192.168.99.3"
   PORT = 5555 
   conn = socket.socket()                       
   conn.connect((HOST, PORT))
   
   while True:
      
      try :
         txt = conn.recv(1024).decode('utf8')
         #print (txt)
         recvData = txt.split(",")

         """
         aX : acceleration of X axis 
         aY : acceleration of Y axis
         """
         
         _aX = float(recvData[0])
         _aY = float(recvData[1])

         controlTurning(_aY)
         controlGasAndBreak(_aX)

         time.sleep(0.01)
         
      except KeyboardInterrupt:
         conn.close ()
      except Exception as e:
         print (e)

   

if __name__ == '__main__':
   main()
   
