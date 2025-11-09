class Num:
    def __init__(self, v): self.v = v
    def __mul__(self, other): return Num(self.v * other)
    def __repr__(self): return f"Num({self.v})"
if __name__ == "__main__": print(Num(10) * 5)
