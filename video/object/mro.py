class A:
    def method(self):
        print("class A~")


class B(A):
    pass


class C(A):
    def method(self):
        print("class C~")


class D(B, C):
    pass


d = D()
d.method()

print(D.mro())
print(C.mro())
