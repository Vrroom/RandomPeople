import xml.etree.ElementTree as etree
import svgpathtools as svg
import random
from Person import Person

def main () :
    doc = svg.Document(None)
    doc.set_viewbox('0 0 100 100')
    person = Person()
    doc = person.addToDocument(doc)
    with open(f'./Data/body{i}.svg', 'wb') as fd: 
        fd.write(etree.tostring(doc.tree.getroot(), encoding='utf8', method='xml'))

if __name__ == "__main__": 
    main()
