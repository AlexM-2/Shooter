from lxml import etree
import pygame
from math import floor, ceil
import subprocess
import os

svg_dict = {}
NS = {"svg": "http://www.w3.org/2000/svg"}
RECOGNISED_STYLE_ATTRS = {"fill", "fill-opacity", "stroke", "stroke-width", "stroke-opacity"}

def prettyprint(element, **kwargs):
    xml = etree.tostring(element, pretty_print=True, **kwargs)
    print(xml.decode(), end='')

def rmns(string: str):
    return string.split("}")[1][0:]

def rd(n: float) -> int:
    """Round to the nearest integer"""
    n = float(n)
    if n % 1 < 0.5:
        return floor(n)
    else:
        return ceil(n)

class SVGElementLookup(etree.CustomElementClassLookup):
    def lookup(self, node_type, document, namespace, name):
        match (node_type, name):
            case ("element", "rect"):
                return SVGRect
            case ("element", "svg"):
                return None
            case ("element", _):
                return SVGElementBase
        return None

class SVGElementBase(etree.ElementBase):
    def _init(self):
        self._parent_tree = self.getroottree()
        self._init_()
    
    def _init_(self):
        pass
    
    def render(self) -> pygame.Surface:

        original_svg_path = self.getroottree().docinfo.URL

        def get_modified_svg():

            in_path = original_svg_path
            out_path = os.path.join("cache", self.get("id") + ":" + os.path.basename(os.path.normpath(in_path)))

            svg_out = self.getsvg()

            with open(out_path, "w") as out_svg:
                out_svg.write(svg_out)
            return out_path

        def get_png_from_svg(in_path):
            root, ext = os.path.splitext(in_path)
            out_path = root + ".png"

            with open(in_path) as in_file:
                for line in in_file.readlines():
                    print(line.rstrip())

            subprocess.run([
                "inkscape",
                os.path.abspath(in_path),
                "--export-type=png",
                f"--export-id={self.get("id")}",
                "--export-id-only",
                f"--export-filename={os.path.abspath(out_path)}"
            ])
            return out_path
        
        svg_in_path = get_modified_svg()
        png_out_path = get_png_from_svg(svg_in_path)

        return pygame.image.load(png_out_path)
    
    def tree(self):
        """The corresponding ElementTree object for this element"""
        return self._parent_tree
    tree = property(tree)

class SVGRect(SVGElementBase):

    def _init_(self):

        self._x = rd(self.get("x"))
        self._y = rd(self.get("y"))

        self._width = rd(self.get("width"))
        self._height = rd(self.get("height"))

        r_try = (self.get("rx"), self.get("ry"))
        match r_try:
            case (None, None):
                self._r = None
            case (_, None):
                self._r = rd(r_try[0])
            case (None, _):
                self._r = rd(r_try[1])
            case (_, _):
                self._r = rd(sum(r_try) / 2)

        self._style = {item.split(":")[0]: item.split(":")[1] for item in self.get("style").split(";")}

        for key, value in self._style.items():
            match (key in RECOGNISED_STYLE_ATTRS, key):
                case (True, "fill"):
                    setattr(self, "_fill", value)
                case (True, "fill-opacity"):
                    setattr(self, "_fill_opacity", value)
                case (True, "stroke-width"):
                    setattr(self, "_stroke_width", rd(value))
                case (True, "stroke"):
                    setattr(self, "_stroke_fill", value)
                case (True, "stroke-opacity"):
                    setattr(self, "_stroke_opacity", float(value))
        # self._fill = self._style["fill"]
        # self._fill_opacity = self._style["fill-opacity"]

        # self._stroke_width = rd(float(self._style["stroke-width"]))
        # self._stroke_fill = self._style["stroke"]
        # self._stroke_opacity = float(self._style["stroke-opacity"])
    
    def getsvg(self):
        self.attrib["x"] = str(self._x)
        self.attrib["y"] = str(self._y)
        self.attrib["width"] = str(self._width)
        self.attrib["height"] = str(self._height)

        self._style["fill"] = str(self._fill)
        self._style["stroke"] = str(self._stroke_fill)
        self._style["stroke-width"] = str(self._stroke_width)

        style = ""
        for key, value in self._style.items():
            if not style == "":
                style+= ";"
            style+= f"{key}:{value}"
        self.attrib["style"] = str(style)

        return etree.tostring(self.getroottree(), pretty_print= True, encoding= "unicode")

    def get_x(self) -> int:
        return rd(self._x)
    def set_x(self, x: int | str):
        self._x = str(x)
    x: int = property(get_x, set_x, doc= "The x position of the Rect (offset from the top-right of the svg file)")

    def get_y(self) -> int:
        return rd(self._y)
    def set_y(self, y: int | str):
        self._y = str(y)
    y: int = property(get_y, set_y, doc= "The y position of the Rect (offset from the top-right of the svg file)")

    def get_width(self) -> int:
        return rd(self._width)
    def set_width(self, width: int | str):
        self._width = str(width)
    width: int = property(get_width, set_width, doc= "The width of the Rect")

    def get_height(self) -> int:
        return rd(self._height)
    def set_height(self, height: int | str):
        self._height = str(height)
    height: int = property(get_height, set_height, doc= "The height of the Rect")

    def get_color(self) -> pygame.Color:
        return pygame.Color(self._fill)
    def set_color(self, color: pygame.Color | str):
        self._fill = str(color)
    color: pygame.Color = property(get_color, set_color, doc= """The fill color of the Rect""")

    def get_stroke_width(self) -> int:
        return rd(self._stroke_width)
    def set_stroke_width(self, stroke_width: int | str):
        self._stroke_width = str(stroke_width)
    stroke_width: int = property(get_stroke_width, set_stroke_width, doc= "The width of the stroke of the Rect")

    def get_stroke_color(self) -> pygame.Color:
        return pygame.Color(self._stroke_fill)
    def set_stroke_color(self, stroke_color: pygame.Color | str):
        self._stroke_fill = str(stroke_color)
    stroke_color: pygame.Color = property(get_stroke_color, set_stroke_color, doc= "The stroke color")

    def get_corner_radius(self) -> int:
        return rd(self._r)
    def set_corner_radius(self, radius: int | str):
        self._r = str(radius)
    corner_radius: int = property(set_corner_radius, get_corner_radius, doc= "How curved the corners of the Rect are")

class SVGFile:
    def __init__(self, file_path: str, custom_element_lookup = SVGElementLookup()):

        self.file_path = os.path.abspath(file_path)
        self.info = {
            "source": file_path,
            "namespaces": {"svg": "http://www.w3.org/2000/svg"}
        }
        self.ns = {"svg": "http://www.w3.org/2000/svg"}

        self.parser = etree.XMLParser()
        self.parser.set_element_class_lookup(custom_element_lookup)

        print(file_path)
        self.tree: etree._ElementTree = etree.parse(file_path, self.parser)
    
    def render(self):
        def get_modified_svg():
            in_path = self.file_path
            print(type(in_path))
            out_path = os.path.join("cache", os.path.basename(os.path.normpath(in_path)))

            with open(out_path, "w") as out_svg_file:
                out_svg_file.write(etree.tostring(self.tree, encoding= "unicode"))
                print(etree.tostring(self.tree, encoding= "unicode"))
                return out_path

        def get_png_from_svg(in_path: str):
            root, ext = os.path.splitext(in_path)
            out_path = root + ".png"

            subprocess.run([
                "inkscape",
                os.path.abspath(in_path),
                "--export-type=png",
                f"--export-filename={os.path.abspath(out_path)}"
            ])
            return out_path

        in_svg_path = get_modified_svg()
        out_png_path = get_png_from_svg(in_svg_path)

        return pygame.image.load(out_png_path)

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()