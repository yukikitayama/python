# File Processing

## XML

Markup language for storing and transporting data by systems using the SOAP communication protocol.

`<!-- -->` is a comment.

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

## CSV

Typically comma-separated values, but other separators such as semicolon or tab are also allowed.

Only one type of separator can be used.

Save special characters
- `csv.QUOTE_MINIMAL` quotes only values with special characters such as separator or `quotechar`
- `csv.QUOTE_ALL` quotes all values with `quotechar`.
- `csv.QUOTE_NONNUMERIC` quotes only non-numeric values with `quotechar`

## Logging

Use `logging` module to find the cause of an error

Hierarchy is assigned based on the names passed to the `getLogger()` Logger names use the dot separator similar to modules.
For example, `getLogger("hello")` creates a logger as a **child** of the root logger. `getLogger("hello.world")` creates
a logger which is a child of `hello` logger

Recommended way is to assign `__name__` to `getLogger()` because it's easy to specify the source of the logged message by
the current module name.

**Root logger** is at the highest point in the hierarchy.

