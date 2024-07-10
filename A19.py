import pdb

def debug_example():
    a = 10
    b = 20
    pdb.set_trace()
    c = a + b
    print(c)

debug_example()
