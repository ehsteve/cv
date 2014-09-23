#!/usr/bin/env python
import os
import subprocess

bio_filename = "bio"

try:
    os.remove(bio_filename + '.aux')
except:
    pass

try:
    os.remove(bio_filename + '.bbl')
except:
    pass

os.system('pdflatex ' + bio_filename)

subprocess.call(["python", "bib_to_markdown.py"])

#os.system('bibtex ' + paper_name)
#os.system('pdflatex -shell-escape ' + paper_name)