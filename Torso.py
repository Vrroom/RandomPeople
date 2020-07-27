from copy import deepcopy
from SimpleShapes import *
import svgpathtools as svg

class Torso () :
    
    def __init__ (self, h, w) :
        self.body = rectangle(h, w)
        self.joints = [
            (h/4) * 1j,
            w + (h/4) * 1j,
            (w/4) + h * 1j,
            (3*w/4) + h * 1j,
            w/2
        ]
        self.center = (w + h*1j) / 2
        self.pseudoLines = [svg.Line(start=self.center, end=p) for p in self.joints]

    def translated(self, t) :
        newTorso = deepcopy(self)
        newTorso.body = newTorso.body.translated(t)
        newTorso.joints = [j + t for j in newTorso.joints]
        newTorso.center += t
        newTorso.pseudoLines = [l.translated(t) for l in newTorso.pseudoLines]
        return newTorso

    def rotated(self, angle) :
        newTorso = deepcopy(self)
        newTorso.body = newTorso.body.rotated(angle, newTorso.center)
        newTorso.pseudoLines = [l.rotated(angle, self.center) for l in newTorso.pseudoLines]
        newTorso.joints = [l.end for l in newTorso.pseudoLines]
        return newTorso


