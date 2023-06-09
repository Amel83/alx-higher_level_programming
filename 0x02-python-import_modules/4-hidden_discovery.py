#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4.pyc import *
    a = dir()
    for i in range(0, len(a)):
        if a[i][0:2] != "__":
            print("{}".format(a[i]))
