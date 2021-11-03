from location import find_location
import sys

ip = sys.argv[1]

location = find_location(str(ip))
print(location)


#ip = '174.176.60.140'
#ip = str(sys.argv[1])



