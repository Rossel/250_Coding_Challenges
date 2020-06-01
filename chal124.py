x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
     
if sorted(x.keys())[-1] % sorted(x.keys())[-2] == sorted(x.keys())[0]:
    print("True!")
else:
    print("False!")