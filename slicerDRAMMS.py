#!/usr/bin/env python

xml = """<?xml version="1.0" encoding="utf-8"?>
<executable>
  <category>Filtering</category>
  <title>slicerDRAMMS</title>
  <description><![CDATA[DRAMMS Image Registration tool in 3DSlicer.]]></description>
  <version>1.4.0.$Revision$</version>
  <documentation-url>http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.3/Modules/MyDRAMMS</documentation-url>
  <license/>
  <contributor>Yangming Ou (MGH)</contributor>
  <acknowledgements><![CDATA[This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.]]></acknowledgements>
  <parameters>
    <label>IO</label>
    <description><![CDATA[Input/output parameters]]></description>
    <image>
      <name>inputSourceImage</name>
      <label>Input Source Image</label>
      <channel>input</channel>
      <index>0</index>
      <description><![CDATA[First Input volume]]></description>
    </image>
    <image>
      <name>inputTargetImage</name>
      <label>Input Target Image</label>
      <channel>input</channel>
      <index>1</index>
      <description><![CDATA[Second Input volume]]></description>
    </image>
    <image>
      <name>outputRegisteredImage</name>
      <label>Output Registered Image</label>
      <channel>output</channel>
      <index>2</index>
      <description><![CDATA[Output filtered]]></description>
    </image>
	<image>
      <name>outputDeformation</name>
      <label>Output Deformation</label>
      <channel>output</channel>
      <index>2</index>
      <description><![CDATA[Output filtered]]></description>
    </image>
  </parameters>
</executable>
"""


print (xml)
