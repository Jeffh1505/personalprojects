class A:
    def __init__(self, val) -> None:
        self.val = val
    def __str__(self) -> str:
        return "A"
    
class B(A):
    def add(self, x):
        self.val.append(x)
    def __str__(self) -> str:
        v = [str(v) for v in self.val]
        return "B({})".format(' '.join(v))
    
class C(B):
    def __init__(self, val) -> None:
        self.val = val

    def __str__(self) -> str:
        return str(self.val)
    

li = []
a = A(li)
b = B(li)
c = C(li)

b.add(1)
print(li)
print(a)
print(b)
print(c)