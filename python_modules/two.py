from python_modules import one
import flask

print("top-level in two.py")

print(type(one.yossi()))
if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")
