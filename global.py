import numpy as np
import time
import threading
import driver as drv
import engine as eng
import output as out

def pretty_time():
        return str(time.asctime( time.localtime(time.time())))

DONE = False


driver = drv.Driver()
print("GLB - Driver instantiated - " + pretty_time())
engine = eng.Engine()
print("GLB - Engine instantiated - " + pretty_time())
output = out.Output()
print("GLB - Output instantiated - " + pretty_time())

driver.start()
print("GLB - Driver started - " + pretty_time())

