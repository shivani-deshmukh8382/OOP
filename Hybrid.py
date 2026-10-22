class SP:
    def __init__(self):
        print("SP")

class P1:
    def __init__(self):
        print("P1")

class P2(SP):
    def __init__(self):
        super().__init__()
        print("P2")

class C(P1,P2):
    def __init__(self):
        super().__init__()
        print("C")

class CC(C):
    def __init__(self):
        super().__init__()
        print("CC")

print(CC.mro())
print(C.mro())
print(P1.mro())
print(P2.mro())
print(SP.mro())
        
cc=CC()
p2=P2()
c=C()
        