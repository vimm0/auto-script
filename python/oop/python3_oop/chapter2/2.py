# Making it do something


class Point:
    def reset(self):
        self.x = 0
        self.y = 0


p = Point()
p.reset()
# Point.reset(p) # call class method using object instance
print(p.x, p.y)
