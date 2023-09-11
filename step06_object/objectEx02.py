from pythonstudy.step06_object.objectEx01 import *
if __name__ == '__main__':
    ps = Person()
    print(ps)
    print(ps.viewPerson())

    ps.setPerson('장길산', 14, 168.2)
    print(ps.viewPerson())