#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "    "
    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, ind=""):
        out_file.write(ind)
        out_file.write(self._open_tag())
        for content in self.contents:
            try:
                content.render(out_file, ind + self.indent)
            except AttributeError:
                out_file.write(f"{content + ind + self.indent}")
            out_file.write("\n")
        # out_file.write(ind)
        out_file.write(f"{ind + self.indent}{self._close_tag()}\n")

    def _open_tag(self, ind=indent):
        if self.attributes:
            tags = ""
            for attribute, value in self.attributes.items():
                tags += f"{attribute}=\"{value}\" "
            return f"{ind}<{self.tag} {tags.rstrip()}>\n"
        else:
            return f"{ind}<{self.tag}>\n"

    def _close_tag(self):
        return f"</{self.tag}>"

class Html(Element):
    tag = "html"

    def render(self, out_file, ind=""):
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file=out_file, ind=ind)

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def append(self, new_content):
        raise NotImplementedError

    def _open_tag(self):
        open_tag = f'<{self.tag}'
        for attributes in self.attributes:
            open_tag = open_tag + (
                f' {attributes}="{self.attributes[attributes]}"')
        open_tag = open_tag + (">")
        return open_tag

    def render(self, out_file, ind=""):
        out_file.write(ind)
        out_file.write(self._open_tag())
        for content in self.contents:
            if content:
                try:
                    content.render(out_file, ind + self.indent)
                except AttributeError:
                    out_file.write(content)
        out_file.write(self._close_tag())

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content.")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, out_file, ind=""):
        # if self.attributes:
        tag = self._open_tag()[:-1] + " />\n"
        # else:
        #     tag = self._open_tag()[:-2] + " />\n"
        out_file.write(f"{tag}")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content=content, **kwargs)

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):
    def __init__(self, size, content=None, **kwargs):
        self.size = int(size)
        if self.size:
            self.tag = f"h{size}"
        super().__init__(content=content, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"
    indent = ""
