# File Processing

## XML

Markup language for storing and transporting data by systems using the SOAP communication protocol.

Standard Python library

- `xml.etree.ElementTree`
  - First choice.
- `xml.dom.minidom`
  - Parse into a tree structure in which each node is an object.
- `xml.sax`
  - SAX means Simple API for XML. This module requires more work. Event-driven XML document analysis.

**Prolog** is the first line of the document specifying character encoding.

The XML document must have one **root element**.

**Elements** are things with opening and closing tags. The elements include **text**, **attributes** and other child elements.

**Attributes** are the key-value pairs in the opening tags.

### xml.etree.ElementTree

`ET` is the common alias.

`ET.parse(FILE.xml)` which returns `ElementTree` object or `ET.fromstring(XML_AS_STRING)` which returns the root element
`Element` object.

Use `getroot()` to access to the root element and we can reach any elements in the document.

`iter(TAG)` iterates recursively through all child elements and their nested elements with the tag as an argument.

`findall(TAG)` only searches the children at the first nesting level. Only accept **XPath expression**

`get(ATTRIBUTE)` to get the value of the attribute.

`find(TAG)` only returns the first child element containing the tag or matching **XPath expression**

`write(FILE.xml)` to save all the changes in XML document because only modifying the XML document doesn't save anything.
