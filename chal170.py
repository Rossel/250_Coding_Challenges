try:
    print(25 % 5 ** 5 + 5)
except ZeroDivisionError:
    print("Zero!")
else:
    print("Clean!")
finally:
    print("Finish!")