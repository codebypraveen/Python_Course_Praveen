# Goal:
# Print a countdown before something “exciting” happens (like “Launching...” or
# “Happy New Year!”).

import time

count=int(input("Enter countDown num"))

print("/n countdown starts Now: ")

for i in range(count, 0, -1):
    print(i)
    time.sleep(1)

print("\n WOHOOO! Happy new uear!")