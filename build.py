#!/usr/bin/env python
import os
import subprocess

bio_filename = "bio"

def build_tex(name, bib=False):
    try:
        os.remove(bio_filename + '.aux')
    except:
        pass

    try:
        os.remove(bio_filename + '.bbl')
    except:
        pass

    os.system('pdflatex ' + name)
    if bib:
        os.system('bibtex ' + name)
        os.system('pdflatex ' + name)

build_tex("bio")
build_tex("cv", bib=True)

subprocess.call(["python", "bib_to_markdown.py"])