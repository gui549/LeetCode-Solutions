# clean solution
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((val, min(val, self.stack[-1][1])))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# first solution
# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min_values = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if len(self.min_values) == 0 or self.min_values[-1] >= val:
#             self.min_values.append(val)

#     def pop(self) -> None:
#         ele = self.stack.pop()
#         if self.min_values[-1] == ele:
#             self.min_values.pop()

#     def top(self) -> int:
#         return self.stack[-1]        

#     def getMin(self) -> int:
#         return self.min_values[-1]
