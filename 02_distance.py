
print("Enter starting pixel of x and y:-> ")
a, b = [int(x) for x in input().split()]
print("Enter ending pixel of x and y:-> ")
c, d = [int(x) for x in input().split()]

E = ((a-c)**2 + (b-d)**2)**(1/2)
print("Euclidean Distance :", E)

C = abs(a-c) + abs(b-d)
print("D4 Distance :", C)
Ch = max(abs(a-c), abs(b-d))
print("D8 Distance:",Ch)