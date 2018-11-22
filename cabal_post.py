import subprocess
from random import randint


message='Temp = 30'
key='[KEY]'
channel = 'sensor_test'
timeout = 1000

while True:
    
    message='Temp='+str(randint(0, 100))
    
    output=subprocess.check_output(['cabal', '--message',str(message), '--key', str(key), '--channel', str(channel), '--timeout', str(timeout)])
