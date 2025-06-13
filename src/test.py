class Obj:
    def __init__(self):
        super().__init__()

obj = Obj()

obj.blah = [34, 56]

setattr(obj, "blah", (2, obj.blah[1]))

print(obj.blah)