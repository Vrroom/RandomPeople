from copy import deepcopy
from SimpleShapes import *
import svgpathtools as svg

class Limb () : 

    def __init__ (self, h1, w1, h2, w2) :
        self.top = rectangle(h1, w1)
        self.joint = (h1/2) * 1j
        self.joint2 = w1 + (h1/2) * 1j
        self.bottom = rectangle(h2, w2).translated(self.joint2 - (h2/2) * 1j)
        self.pseudoLine = svg.Line(start=self.joint, end=self.joint2)

    def translated(self, t) : 
        newLimb = deepcopy(self)
        newLimb.top = newLimb.top.translated(t)
        newLimb.bottom = newLimb.bottom.translated(t)
        newLimb.joint += t
        newLimb.joint2 += t
        return newLimb

    def rotated (self, angle) :
        newLimb = deepcopy(self)
        newLimb.top = newLimb.top.rotated(angle, newLimb.joint)
        newLimb.bottom = newLimb.bottom.rotated(angle, newLimb.joint)
        newLimb.pseudoLine = newLimb.pseudoLine.rotated(angle, newLimb.joint)
        newLimb.joint2 = newLimb.pseudoLine.end
        return newLimb

    def bottomRotated (self, angle) :
        newLimb = deepcopy(self)
        newLimb.bottom = newLimb.bottom.rotated(angle, newLimb.joint2)
        return newLimb
