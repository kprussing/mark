#!/usr/bin/env python

import subprocess
import xml.etree.ElementTree as ET

import pikepdf


def pdf2svg(target, source, env):
    """Convert the PDF to SVG preserving extra meta data

    This runs ``pdftocairo`` on the given PDF file but looks at the
    metadata and copies over the title, author, and rights information
    to the SVG.
    """
    proc = subprocess.run(
        ["pdftocairo", "-origpagesizes", "-svg", str(source[0]), "-"],
        capture_output=True,
        text=True,
        check=True,
    )

    tree = ET.fromstring(proc.stdout)
    with pikepdf.open(str(source[0])) as pdf:
        meta = pdf.open_metadata()
        for key, value in {"dc:title": "title",
                           "dc:creator": "author",
                           "dc:date": "date",
                           "dc:rights": "rights",
                           "xmpRights:WebStatement": "licenseurl",
                           "pdf:Producer": "producer",
                           }.items():
            if key in meta:
                content = meta[key]
                if isinstance(content, (list, tuple)):
                    content = r"\n".join(content)

                ET.SubElement(tree, "meta", name=value, content=content)

    ET.ElementTree(tree).write(str(target[0]), encoding="unicode")


def pdf2png(target, source, env):
    """Convert the PDF to PNG

    This wraps up the call to ``pdftocairo`` to bypass scons filtering
    of the environment.
    """
    subprocess.run(
        ["pdftocairo", "-png", "-singlefile", "-r", "600", str(source[0])],
        check=True,
    )


pdf = PDF("mark.tex", PDFLATEX="lualatex")  # noqa: F821
svg = Command("mark.svg", pdf, action=pdf2svg)  # noqa: F821
png = Command("mark.png", pdf, action=pdf2png)  # noqa: F821
NoClean(svg, png, pdf)  # noqa: F821
