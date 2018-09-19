class A(object):
    def test(self):
        print("A")


class B(A):
    def test(self):
        print("B")


class C(B):
    def test(self):
        print("C")


class D(C):
    def test(self):
        print("D")


class E(C):
    def test(self):
        print("E")


class F(D):
    pass


class G(D):
    pass

class L(object):
    pass

class M(E):
    pass

class K(F,G,L,M):
    pass
print(K.__mro__)
