class Rectangle():
    def _init_(rec, len, wid):
        rec.length = len
        rec.width = wid
        
    def rectan_area(rec):
        return rec.length*rec.width

newRectangle = Rectangle(int(input()), int(input()))
print(newRectangle.rectan_area())
