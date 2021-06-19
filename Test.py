from NaiveApproach import NaiveStringMatching
from KnuthMorrisPratt import KMP_StringMatching
from RabinKarp import RabinKarpMethod
from time import time_ns

t, s = open("input", "r").read().split()

a = time_ns()
x = NaiveStringMatching(t, s)
b = time_ns()
# y = RabinKarpMethod(t, s)
c = time_ns()
z = KMP_StringMatching(t, s)
d = time_ns()

print("Correctness : ", x == z)
print("Time Complexity :")
print("Naive : ", (b-a)//1000)
# print("RabinKarp", (c-b)//1000)
print("KMP : ", (d-c)//1000)
