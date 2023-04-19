import time
from datetime import datetime

INTERVAL = 2.0

starttime = time.time()

while True:
    print(f'{datetime.now().strftime("%m/%d/%y %H:%M:%S.%f")} - Do a thing every {INTERVAL} s')
    time.sleep(INTERVAL - ((time.time() - starttime) % INTERVAL))