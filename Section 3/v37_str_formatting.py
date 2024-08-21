for i in range(1,5):
    print("The number {0}'s squre is {1} and qube is {2}".format(i, i**2, i**3))
# for i in range(1,13):
#     print("The number {0:2}'s squre is {1:3} and qube is {2:4}".format(i, i**2, i**3))
for i in range(1,13):
    print("The number {0:<2}'s squre is {1:<3} and qube is {2:>4}".format(i, i**2, i**3)) ## here <> arrows are declaring the alingments and :n is declaring the how much space it will take

#####################
## using the f string
print(f"The approximate value of pie is {22/7} - 1")
print(f"The approximate value of pie is {22/7:12} -2")
print(f"The approximate value of pie is {22/7:12f} -3")
print(f"The approximate value of pie is {22/7:<12f} -4")
print(f"The approximate value of pie is {22/7:>12f} -5")
print(f"The approximate value of pie is {22/7:12.3f} -6")
print(f"The approximate value of pie is {22/7:12.20f} -7")