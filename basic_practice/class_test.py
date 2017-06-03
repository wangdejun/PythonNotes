class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3 == 180):
            print self.angle1
            print self.angle2
            print self.angle3

            return True
        else:
            return False

a = Triangle(30, 60, 90)
print a.check_angles()