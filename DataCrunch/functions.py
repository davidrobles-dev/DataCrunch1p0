# Import library required
#import os
import io

"""
# Read the STDF File
datalog = open("1.stdf","rb")
for line in datalog:
    print(line)

datalog.close()
"""

with open("1.stdf","rb") as file:
    hexdata=file.read().hex()
    print(hexdata)