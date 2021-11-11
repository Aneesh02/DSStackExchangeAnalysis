from datetime import datetime
now = datetime.now()
print("start =", now)
import os
os.system('cat large-file.txt | python mapper.py | sort -k1,1 | python reducer.py')
now = datetime.now()
print("stop =", now)
