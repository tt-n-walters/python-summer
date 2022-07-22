import time

seconds = 0
minutes = 0
hours = 0
day = 19
month = 6
year = 0

while True:
    # print("  ", hours, minutes, seconds, end="\r")
    print(f"   {hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")
    time.sleep(0.016)

    seconds = seconds + 1
    if seconds == 60:
        minutes = minutes + 1
        seconds = 0
    
    if minutes == 60:
        hours = hours + 1
        minutes = 0
