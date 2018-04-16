from c1 import Point
import math


class Line(object):
    def __init__(self, p1=Point(), p2=Point()):
        self._line = [p1, p2]
        pass

    def get_line(self):
        return [self._line[0].get_point(), self._line[1].get_point()]

    def set_line(self, in_l1_x, in_l1_y, in_l2_x, in_l2_y):
        self._line[0].set_point(in_l1_x, in_l1_y)
        self._line[1].set_point(in_l2_x, in_l2_y)
        pass

    def length(self):
        return math.sqrt(pow(abs(self.get_line()[0][0]-self.get_line()[1][0]), 2) + pow(abs(self.get_line()[0][1]-self.get_line()[1][1]), 2))


if __name__ == "__main__":
    line1 = Line()
    print(line1.get_line())

    line2 = Line()
    line2.set_line(0, 0, 5, 5)
    print(line2.get_line())
    print(line2.length())

    line3 = Line()
    line3.set_line(2, 3, -9, -2)
    print(line3.get_line())
    print(line3.length())