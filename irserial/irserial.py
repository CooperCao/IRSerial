import serial
import time

class IRserialException(IOError):
    """Base class for IRserial related exceptions"""

portNotOpenError = IRserialException('port is not open')

class IRserial:
    
    def __init__(self,
                 port=None,
                 baudrate=9600,
                 timeout = 5,
                 ):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        if port is not None:
            self._port_handle = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        else:
            self._port_handle = None
    
    def get_config(self):
        if self._port_handle is None:
            raise portNotOpenError		
        return self._port_handle.getSettingsDict()
        
        
    def  send(self,key):
        if self._port_handle is None:
            raise portNotOpenError
        # IR send format: [0xA1,0XF1,KEY]
        cmd=[0xA1,0xF1]+key
        self._port_handle.write(cmd)
        for i in range(0,5):
            has_key = self._port_handle.inWaiting()
            if has_key:
                res = self._port_handle.read(has_key)
                if res[0] == 0xF1:
                    return True
            else:
                time.sleep(0.1)
        else:            
            return False
        
    def receive(self):
        if self._port_handle is None:
            raise portNotOpenError
        self._port_handle.flushInput()
        value = self._port_handle.read(3)
        if len(value) == 3:
            user_code = value[0:2]
            key_code = value[2]
            return user_code,key_code
        else:
            return None,None
    
    def close(self):
        if self._port_handle is not None:
            self._port_handle.close()
            self._port_handle = None     
