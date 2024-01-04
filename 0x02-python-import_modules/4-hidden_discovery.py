#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_6

    names = dir(hidden_6)
    for name in names:
        if name[:2] != "__":
            print(name)
