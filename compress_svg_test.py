from lxml import etree
import zlib
#run @ miniconda env
# sample code to compress/decompress using zlib, grpc Message.svg is the compresed
# array
f=open("map.svg")
xml=etree.fromstring(f.read()).getroottree()

svg1=etree.tostring(xml, xml_declaration=True, encoding="utf-8",standalone=False)

print(len(svg1), svg1)
comp = zlib.compressobj(9,zlib.DEFLATED, -zlib.MAX_WBITS, zlib.DEF_MEM_LEVEL,0)
deflated=comp.compress(svg1)
deflated+=comp.flush()
print(len(deflated), deflated)
decomp = zlib.decompressobj()
restored_svg = zlib.decompress(deflated,wbits=-zlib.MAX_WBITS)
print(len(restored_svg), restored_svg)


