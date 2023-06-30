import xml.etree.ElementTree as ET

root = ET.Element("data")
movie_1 = ET.SubElement(root, "movie", {"title": "The Little Prince", "rate": "5"})
movie_2 = ET.SubElement(root, "movie", {"title": "Hamlet", "rate": "5"})

# dump() allows us to debug either the whole tree or a single element
ET.dump(root)

# ElementTree object allows us to save a document by write method
tree = ET.ElementTree(root)
