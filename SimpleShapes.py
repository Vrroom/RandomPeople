import svgpathtools as svg

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
