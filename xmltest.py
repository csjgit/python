import xml.etree.ElementTree as ET
tree = ET.parse('D:\\python\\Learning\\Files\\test.xml')

root= tree.getroot();
#for child in root:
 #   print(child.tag, child.attrib)
for movie in root.findall("./y/x/country/[rank='4']/../../../"):
    print(movie.find("./workflow").text);

