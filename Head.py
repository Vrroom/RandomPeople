from copy import deepcopy
from SimpleShapes import *
import svgpathtools as svg

class Head () :

    def __init__ (self, r) :
        self.circle = circle(r)
        self.joint = r * 1j

    def translated (self, t) :
        newHead = deepcopy(self)
        newHead.circle = newHead.circle.translated(t)
        newHead.joint += t
        return newHead

    def rotated (self, angle) :
        newHead = deepcopy(self)
        newHead.circle = newHead.circle.rotated(angle, newHead.joint)
        return newHead
