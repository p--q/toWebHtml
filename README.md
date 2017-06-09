# toWebHtml　LibreOffice Extension

LibreOffice extension that outputs html to default web browser.

This repository contains Eclipse's PyDev project.

## Deployment

Deploy toWebHtml.oxt in the <a href="https://github.com/p--q/toWebHtml/tree/master/toWebHtml/oxt">toWebHtml/toWebHtml/oxt</a> folder with the extension manager of LibreOffice.

## Usage

Instantiate with implementation service name pq.ToWebHtml or UNO service name com.blogspot.pq.ToWebHtml.

setTitle() method takes a string argument and sets the title of the web page.

openInBrowser() method takes a string argument and outputs it to the default browser.

You can also use HTML tags as arguments to openInBrowser() method.

## Usage Example


ctx is the component context, and smgr is the service manager.

```
    page = smgr.createInstanceWithContext("com.blogspot.pq.ToWebHtml", ctx)
    page.setTitle("From toWebHtml Extension")
    page.openInBrowser("<span style='background-color: red;'>Output from toWebHTML extension</span>")
```

macro() in <a href="https://github.com/p--q/toWebHtml/blob/master/toWebHtml/execution_example.py">execution_example.py</a> is an example to call from the macro selector.
