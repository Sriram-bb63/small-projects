from essential_generators import DocumentGenerator
from time import time

gen = DocumentGenerator()
print(gen.paragraph())
input("Press ENTER to start")
start = time()
ans = input(">>>")
stop = time()
totaltime = stop - start
print("Time taken taken = ", totaltime)
l = len(ans.split())
timeperword = totaltime / l
print("Time taken per word = ", timeperword)
