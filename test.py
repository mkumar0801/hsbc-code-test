
class D():
    def __init__(self):
        print('D')


class A(D):
    def __init__(self):
        print('A')

    def print_name(self):
        print('print A')

class B():
    def __init__(self):
        print('B')
    
    def print_name(self):
        print('print B')


class C(A, B):
    def __init__(self):
        print('init C')
    def test(self):
        pass



c_obj1 = C()
c_obj1.print_name()

# c_obj2 = C()
# print(c_obj1 == c_obj2)
# c_obj1 =  c_obj2
# print(c_obj1 == c_obj2)
# c_obj.print_name()

# a_obj = A()




