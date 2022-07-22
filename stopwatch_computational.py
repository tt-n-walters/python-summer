import time

seconds = 1658230492


while True:
    # print(seconds // 3600, seconds // 60 % 60, seconds % 60)
    print(f"  {(seconds // 3600):02d}:{(seconds // 60 % 60):02d}:{(seconds % 60):02d}\t\t{seconds}", end=" \r")

    time.sleep(0.1)
    seconds = seconds + 1

