class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    try:
        def description(self):
            return self.a, self.b, self.c

        def Paragic(self):
            return self.a + self.b + self.c

        def hs(self):
            if self.a == self.b != self.c or self.b == self.c != self.a or self.a == self.c != self.b:
                print('-havasarasrun erankyun-')
            elif self.a == self.b and self.a == self.c and self.b == self.c:
                print('-havasarakoxm erankyun-')
            elif self.a != self.b != self.c:
                print('-ankanon erankyun-')
    except AttributeError as text:
        print(text)


f = Triangle(4, 4, 20)
# print(f.Paragic())
f.hs()
