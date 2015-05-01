0. web page
    (main page)[http://lxml.de/]

    ```
        from lxml import etree
    ```

    ```
        from io import StringIO, BytesIO
    ```

1. parse xml
    ```
        xml = '<a xmlns="test"><b xmlns="test"/></a>'
        root = etree.fromstring(xml)
        etree.tostring(root)
    ```

    ```
        tree = etree.parse(StringIO(xml))
        etree.tostring(tree.getroot())
    ```

    ```
        tree = etree.parse("doc/test.xml")
    ```

2. parse html
    ```
        broken_html = "<html><head><title>test<body><h1>page title</h3>"
        parser = etree.HTMLParser()
        tree   = etree.parse(StringIO(broken_html), parser)
        result = etree.tostring(tree.getroot(),pretty_print=True, method="html")
        print(result)
    ```
    ```
        html = etree.HTML(broken_html)
        result = etree.tostring(html, pretty_print=True, method="html")
        print(result)
    ```
