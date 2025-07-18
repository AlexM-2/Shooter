from pyglet.text import Label
from lxml import etree

NS = {"svg": "http://www.w3.org/2000/svg"}
STR_NS = "{http://www.w3.org/2000/svg}"

class SVGFile:
    def __init__(self, file_path: str):
        self.tree: etree._ElementTree = etree.parse(file_path)

        groups = []
        print("parsing")
        for group_elem in self.tree.xpath("//svg:g", namespaces= NS):
            out_group: list = []

            for elem in group_elem.xpath(".//svg:*", namespaces= NS):
                if elem.tag == STR_NS + "text":

                    translation = elem.get("translation") or group_elem.get("translation")

                    tspans = []
                    for tspan_elem in elem.xpath("/svg:tspan", namespaces=NS):
                        tspans.append(Label(
                            str(tspan_elem.text),
                            float(tspan_elem.get("x"))
                        ))
                
                out_group.append(elem)
        
            groups.append(out_group)
        
        self.groups = groups

        # self.shader_program.vertex_list_indexed()

def main():
    svg = SVGFile("Assets/play_button_plain.svg")
    

if __name__ == "__main__":
    main()