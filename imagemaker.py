file = open("output.ppm", "w")
file.write("P6 \n500 500 \n255 \n")
from itertools import repeat
for i in range(1, 250000):
    file.write("50 50 25 ")
#comment test
