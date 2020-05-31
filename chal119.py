x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]
     
if max(x[:3]) <= min(x[3:6]):
    print("True!")
else:
    print("False!")