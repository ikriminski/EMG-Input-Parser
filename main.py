import numpy as np
import time
import util
import threading
import driver as drv
import engine as eng
import output as out

DONE = False


driver = drv.Driver()
print("GLB - Driver instantiated - " + util.pretty_time())
engine = eng.Engine()
print("GLB - Engine instantiated - " + util.pretty_time())
output = out.Output()
print("GLB - Output instantiated - " + util.pretty_time())

driver.start(engine)
print("GLB - Driver started - " + util.pretty_time())
engine.start(driver, output)
print("GLB - Engine started - " + util.pretty_time())
output.start(engine)
print("GLB - Output started - " + util.pretty_time())

driver.run()


