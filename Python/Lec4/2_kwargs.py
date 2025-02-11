from typing import TypedDict, Unpack

class DrawArgs(TypedDict):
    color: str
    size: int
    text: str
    font: str
    bold: bool
    italic: bool
    underline: bool

def draw_text(**kwargs: Unpack[DrawArgs]):
    """
    kwargs: color, size, text, font, bold, italic, underline
    """
    print(kwargs["color"])
    print(kwargs["size"])
    print(kwargs["text"])

 
draw_text(color="red", size=12, text="Hello World", font="Arial", bold=True, italic=False, underline=False)
draw_text(text="Hello World", font="Arial",underline=False)