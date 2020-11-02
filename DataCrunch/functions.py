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

with open("sample1.std","rb") as file:
    Data_IO = io.BytesIO(file.read())
    datalog = Data_IO.getvalue()
    print(datalog)