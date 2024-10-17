from tkinter import Tk, Label


def test_fn(a=1, b=2, c=3):
    print(f"{a},{b},{c}")


# change default value
# test_fn(b=5)


def test_args(*args):
    # unlimited positional arguments
    print(f"type {type(args)}")  # tuple
    for n in args:
        print(f"{n}")


# print(test_args(1, 2, 3, 4, 45, 50))


def test_kwargs(n, **kwargs):
    """kwargs are optional keyword arguments"""
    print(f"n type {type(n)}")
    print(f"kwargs type {type(kwargs)}")  # dict of keyword arguments and their values
    print(f"{kwargs}")


# test_kwargs([1, 2, 3], a=1, b=2)  # a and b are optional keyword arguments and have a default value


window = Tk()
window.minsize(width=500, height=300)
window.title("Tkinter")
label = Label(text="Tkinter", font=("Arial", 24, "bold")).pack(side="top")
window.mainloop()
