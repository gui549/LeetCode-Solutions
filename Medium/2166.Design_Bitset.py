class Bitset:

    def __init__(self, size: int):
        self.bit = 0
        self.size = size
        self.ones = 0

    def fix(self, idx: int) -> None:
        if self.bit & (1 << (self.size - 1 - idx)) == 0:
            self.bit |= 1 << (self.size - 1 - idx)
            self.ones += 1

    def unfix(self, idx: int) -> None:
        if self.bit & (1 << (self.size - 1 - idx)):
            self.bit ^= 1 << (self.size - 1 - idx)
            self.ones -= 1

    def flip(self) -> None:
        self.bit ^= (1 << self.size) - 1
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.bit == (1 << self.size) - 1

    def one(self) -> bool:
        return self.bit

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return bin(self.bit)[2:].zfill(self.size)