#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    h = len(sys.argv) - 1
    if h == 0:
        print("{} arguments.".format(h))
    elif h == 1:
        print("{} argument:".format(h))
    else:
        print("{} arguments:".format(h))
        if h >= 1:
            h = 0
            for arg in sys.argv:
                if h != 0:
                    print("{}: {}".format(h, arg))
                    h += 1
