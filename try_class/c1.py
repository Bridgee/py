class Point(object):
    def __init__(self, x=0, y=0):
        self._point = [x, y]
        pass

    def get_point(self):
        return self._point

    def set_point(self, in_x, in_y):
        self._point = [in_x, in_y]
        pass


if __name__ == "__main__":
    print('test for class point')

    point1 = Point()
    print(point1.get_point())

    point2 = Point(5, 5)
    print(point2.get_point())

    point3 = Point()
    point3.set_point(9, 9)
    print(point3.get_point())