import time
import sys

text = "Follow for more Python tips and tricks!"


for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)  # adjust here for typing speed
