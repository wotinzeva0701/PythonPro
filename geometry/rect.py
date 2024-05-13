class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimeter(self):
        return 2 * (self.w + self.h)


print(__name__)

__author__ = "admin"
if __name__ == "__main__":
    print(f"Module {__name__} (author: {__author__}).")
