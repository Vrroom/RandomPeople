from functools import reduce
import svgpathtools as svg
import random

def save(paths, out) : 
    fill = [{'fill': [0, 0, 0]} for _ in paths]
    svg.wsvg(paths, attributes=fill, viewbox='0 0 100 100', filename=out)

def rectangle(h, w) :
    rect = []
    rect.append(svg.Line(0 + 0j, w + 0j))
    rect.append(svg.Line(w + 0j, w + h * 1j))
    rect.append(svg.Line(w + h * 1j, 0 + h * 1j))
    rect.append(svg.Line(0 + h * 1j, 0 + 0j))
    return svg.Path(*rect)

def circle (r) :
    arcs = []
    arcs.append(svg.Arc(-r + 0j, r + r * 1j, 0, False, False, r + 0j))
    arcs.append(svg.Arc(-r + 0j, r + r * 1j, 0, False, True, r + 0j))
    return svg.Path(*arcs)

def person() :
    """ Assume 100 by 100 viewbox """
    torsoHeight = random.randint(30, 50)
    torsoWidth = random.randint(20, 30)
    torso_ = torso(torsoHeight, torsoWidth)
    legs_ = legs(torsoHeight, torsoWidth)
    arms_ = arms(torsoHeight, torsoWidth)
    head_ = head(torsoHeight, torsoWidth)
    return [head_, torso_, arms_, legs_]

def legs(torsoHeight, torsoWidth): 
    legsY = 50 + torsoHeight / 2
    lJoint = (50 - torsoWidth / 4) + legsY * 1j
    rJoint = (50 + torsoWidth / 4) + legsY * 1j
    h, w = random.randint(5, 10), random.randint(15, 24)
    alpha = random.randint(-90, 0)
    beta = random.randint(-180, -90)
    return [limb(lJoint, alpha, h, w), limb(rJoint, beta, h, w)]

def arms(torsoHeight, torsoWidth):
    armY = 50 - torsoHeight / 3
    lJoint = (50 - torsoWidth / 2) + armY * 1j
    rJoint = (50 + torsoWidth / 2) + armY * 1j
    h, w = random.randint(5, 10), random.randint(15, 20)
    alpha = random.randint(-90, 90)
    beta = random.randint(90, 270)
    return [limb(lJoint, alpha, h, w), limb(rJoint, beta, h, w)]

def limb(joint, angle, h, w): 
    t = joint - (w + ((h / 2) * 1j))
    return rectangle(h, w).translated(t).rotated(angle, joint)

def torso(h, w) :
    tx = 50 - w / 2
    ty = 50 - h / 2
    return rectangle(h, w).translated(tx + ty * 1j)

def head(torsoWidth, torsoHeight) :
    r = 10
    topX = 50
    topY = 50 - torsoHeight / 2 - r
    return circle(r).translated(topX + topY * 1j)

def flatten(l) :
    if len(l) == 0 : 
        return []
    else :
        paths1 = list(filter(lambda x: isinstance(x, svg.Path), l))
        paths2 = reduce(lambda a, b: a + b, map(flatten, filter(lambda x : isinstance(x, list), l)), [])
        return paths1 + paths2

if __name__ == "__main__": 
    for i in range(10) :
        p = flatten(person())
        save(flatten(person()), f'body{i}.svg')
