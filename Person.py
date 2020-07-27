from copy import deepcopy
from SimpleShapes import *
import svgpathtools as svg
from Limb import Limb
from Head import Head
from Torso import Torso
import random

class Person () :

    def __init__ (self) :
        self.center = 50 + 50j
        headRotation = random.randint(-30, 30)
        torsoRotation = random.randint(-15, 15)
        h, w = random.randint(20, 35), random.randint(15, 25)
        diff = self.center - (w + (h * 1j))/2
        self.torso = Torso(h, w).translated(diff).rotated(torsoRotation)
        self.head = Head(random.randint(5, 10)).rotated(headRotation)
        self.arms = [Limb(*self.limbDimensions()).rotated(random.randint(135, 225)).bottomRotated(random.randint(-30, 30)),
                     Limb(*self.limbDimensions()).rotated(random.randint(-45, 45)).bottomRotated(random.randint(-30, 30))]
        self.legs = [Limb(*self.limbDimensions()).rotated(random.randint(70, 110)).bottomRotated(random.randint(-30, 30)),
                     Limb(*self.limbDimensions()).rotated(random.randint(70, 110)).bottomRotated(random.randint(-30, 30))]
        self.attach()

    def limbDimensions (self) :
        h1 = random.randint(5, 10)
        h2 = random.randint(5, 10)
        w1 = random.randint(15, 20)
        w2 = random.randint(15, 20)
        return h1, w1, h2, w2

    def attach (self) :
        self.head = self.head.translated(self.torso.joints[-1] - self.head.joint)
        self.arms = [a.translated(self.torso.joints[i] - a.joint) for i, a in enumerate(self.arms)]
        self.legs = [l.translated(self.torso.joints[2 + i] - l.joint) for i, l in enumerate(self.legs)]

    def addToDocument (self, doc) :
        top = doc.add_group(group_attribs={"fill":"black"})
        body = doc.add_group(parent=top)
        limbs = doc.add_group(parent=top)
        legsGroup = doc.add_group(parent=limbs)
        armsGroup = doc.add_group(parent=limbs)
        bothLegGroups = [doc.add_group(parent=legsGroup) for _ in range(2)]
        bothArmGroups = [doc.add_group(parent=armsGroup) for _ in range(2)]
        doc.add_path(self.head.circle, group=body)
        doc.add_path(self.torso.body, group=body)

        for element, group in zip(self.legs, bothLegGroups) :
            doc.add_path(element.top, group=group)
            doc.add_path(element.bottom, group=group)

        for element, group in zip(self.arms, bothArmGroups) :
            doc.add_path(element.top, group=group)
            doc.add_path(element.bottom, group=group)

        return doc
