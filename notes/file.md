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

```python
import xml.etree.ElementTree as ET
 
root = ET.Element('movies')
 
movie1 = ET.SubElement(root, 'movie')
ET.SubElement(movie1, 'title').text = 'The Shawshank Redemption'
ET.SubElement(movie1, 'rate').text = '9.2'
 
movie2 = ET.SubElement(root, 'movie')
ET.SubElement(movie2, 'title').text = 'The Godhather'
ET.SubElement(movie2, 'rate').text = '9.2'
 
movie3 = ET.SubElement(root, 'movie')
ET.SubElement(movie3, 'title').text = 'The Dark Knight'
ET.SubElement(movie3, 'rate').text = '9.0'
 
tree = ET.ElementTree(root)
tree.write('movies.xml')
```

### DTD

Document Type Definition

`<!ELEMENT book (title, author, price)>` defines that book element must contain title, author and price elements.

`<!ELEMENT title (#PCDATA)>` defines that title element is of type #PCDATA that means parse-able text data.

`<!ATTLIST book category CDATA #REQUIRED>` defines that book element must have category attribute of type CDATA like
`<book category="A">`

### lxml

`lxml` library with XPath expressions to query XML documents

### XPath

Use 1-based index to select data in XPath expression.

For example `store/book[2]/author` to select the author of the **second** book in the following XML

```
<store>
  <book>
    <title>Python Programming</title>
    <author>John Smith</author>
    <price>29.99</price>
  </book>
  <book>
    <title>Web Development Basics</title>
    <author>Jane Johnson</author>
    <price>19.99</price>
  </book>
</store>
```

`//university[location="Palo Alto, CA"]/name` finds any university regardless of its position by `//university` and
filters by `location` and select `name` below.

```
<universities>
  <university name="Harvard University">
    <location>Cambridge, MA</location>
    <rank>1</rank>
  </university>
  <university name="Stanford University">
    <location>Palo Alto, CA</location>
    <rank>2</rank>
  </university>
</universities>
```

`@` is used to search for a specific attributes. `find()` method is used to find the **first child** with a particular 
**tag**.

```
<root>
    <child id="1">
        <grandchild>Grandchild 1</grandchild>
    </child>
    <child id="2">
        <grandchild>Grandchild 2</grandchild>
    </child>
    <child id="3">
        <grandchild>Grandchild 3</grandchild>
    </child>
</root>

import xml.etree.ElementTree as ET

root = ET.fromstring(xml_data)
print(root.find('./child[@id="2"]/grandchild').text)
```

## CSV

Typically comma-separated values, but other separators such as semicolon or tab are also allowed.

Only one type of separator can be used.

Save special characters
- `csv.QUOTE_MINIMAL` quotes only values with special characters such as separator or `quotechar`
- `csv.QUOTE_ALL` quotes all values with `quotechar`.
- `csv.QUOTE_NONNUMERIC` quotes only non-numeric values with `quotechar`

## shelve

`shelve.open("name.shlv", flag="<mode>")` Mode is following

- `"r"` opens an existing database for read only
- `"w"` opens existing database for read and write
- `"c"` opens database for read and write, and if it doesn't exist, create a new database.
- `"n"` always creates a new database with read and write.

## Logging

Use `logging` module to find the cause of an error

Hierarchy is assigned based on the names passed to the `getLogger()` Logger names use the dot separator similar to modules.
For example, `getLogger("hello")` creates a logger as a **child** of the root logger. `getLogger("hello.world")` creates
a logger which is a child of `hello` logger

Recommended way is to assign `__name__` to `getLogger()` because it's easy to specify the source of the logged message by
the current module name.

**Root logger** is at the highest point in the hierarchy.

Root logger has the logging level set to `WARNING`, meaning `INFO` and `DEBUG` won't be printed. This or a higher level
to be logged.

Loggers created using the name argument have `NOTSET` level by default but inherit the logging level from the parent.

`%(name)s` will be replaced by logger name.

`%(levelname)s` will be replaced by logger level.

`%(asctime)s` will be replaced by date format of when `LogRecord` object is created.

`%(message)s` will be replaced by defined message.

Highest level of severity is `CRITICAL`. Lowest level of severity is `NOTSET`. 

### Record logging events to a file

`logging.basicConfig(filename="file.log")` records with default parameters

`logging.basicConfig(filename="file.log", filemode="a", level=logging.CRITICAL)`

## configparser

`configparser` module in Python standard library allows us to use a configuration file read by the code.

The structure of the configuration file is similar to Microsoft Windows **INI files**.

`:` and `=` are used to separate key/value entries.

Use `;` or `#` for comments

`[DEFAULT]` section contains the default values that can be read on the other sections.

`config.read()` can have a list containing several configuration files.

Section names are case sensitive, while the keys aren't

`%(key)s` interpolate values by placing any key between `%(` and `)s`
