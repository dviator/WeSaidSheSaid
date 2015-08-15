#!/usr/bin/python
# Usage: python tt2srt.py source.xml output.srt

from xml.dom.minidom import parse
import sys

def translate(source, output):
    i=1
    # dom = parse(sys.argv[1])
    # out = open(sys.argv[], 'w')
    dom = parse(source)
    out = open(output, 'w')
    body = dom.getElementsByTagName("body")[0]
    paras = body.getElementsByTagName("p")
    for para in paras:
        out.write(str(i) + "\n")
        try:
            a=float(para.attributes['begin'].value)
        except ValueError:
            a=0
        out.write('%02d' %(int(a/3600)))
        out.write(":")
        out.write('%02d' % (int(a/60)-60*(int(a/3600))))
        out.write(':')
        out.write('%02d' % (a%60))
        out.write(',')
        out.write('%03d' % (a%60.0-a%60))
        out.write(' --> ')

        a= float(para.attributes['end'].value)

        out.write('%02d' %(int(a/3600)))
        out.write(":")
        out.write('%02d' % (int(a/60)-60*(int(a/3600))))
        out.write(':')
        out.write('%02d' % (a%60))
        out.write(',')
        out.write('%03d' % (a%60.0-a%60))

        out.write("\n")
        for child in para.childNodes:
            if child.nodeName == 'br':
                out.write("\n")
            elif child.nodeName == '#text':
                out.write(unicode(child.data).encode('utf=8'))
        out.write("\n\n")
        i += 1
# end function 'translate'