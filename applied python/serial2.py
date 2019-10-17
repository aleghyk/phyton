import json
from xml.etree import ElementTree as ET
from xml.dom import minidom as MD
from xml.dom import pulldom as PD
from xml import sax
#json
obj1 = {"asd": (1, 2, 3), 123: "223", 2: 122}
s = json.dumps(obj1)
obj2 = json.loads(s)
#xml
root = ET.Element("tasks")
day = ET.SubElement(root,"day")
day.set('date','01.10.2012')
task1 = ET.SubElement(day,"task")
task1.text = 'Wake up'
task2 = ET.SubElement(day,"task")
task2.text = 'make coffe'
tree = ET.ElementTree("root")
tree.write('tasks.xml')

#parsing
tree = ET.parse'tasks.xml')
for node in tree.getroot()[0]:
    print(node.text)
    
print (tree.findall(".//task"))
for node in tree.findall("./day[@date='01.10.2012']/task")
    print(node.text)


#minidom
tree MD.parse(tasks.xml)

#pulldom
tree PD.parse(tasks.xml)
for event, node in tree:
    if event = PD.START_ELEMENT and node.localName == 'task':
        tree.expandNode(node)
        print (node.toxml())
#sax
class TaskContentHandler(sax.ContentHandler):
    def __init__ (self):
        self.is_task = False
    def startElement(self, name, attr):
        if name == 'task':
            self.is_task = True
    def endElement(self, name, attr):
        if name == 'task':
            self.is_task = False      
    def characters(self, name, attr):
        if name == 'task':
            print(content)
parser = sax.make_parser()
parser.setContentHandler(TaskContentHandler())
parser.parse('tasks.xml')
