time = int(input("Input time in miliseconds: "))
day = time // (24 * 3600 * 100)
time = time % (24 * 3600 * 100)
hour = time // (3600 * 100)
time %= 3600 *100
minutes = time // (60 * 100)
time %= 60 * 100
seconds = time // 100
miliseconds = time % 100
print("d:h:m:s:ms-> %d:%d:%d:%d:%d" % (day, hour, minutes, seconds, miliseconds))