import json
from xml.etree import ElementTree as ET
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
