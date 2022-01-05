#!/usr/env/python

import os
import yaml
from jinja2 import Template

#TEMPLATE_FILE="pt_tex_template.tex.j2"
TEMPLATE_FILE="templates/cv_tex_template.tex.j2"
CURRICULUM="cv.yml"
OUTPUT="output.tex"

with open(TEMPLATE_FILE,'r') as template_file:
  with open(CURRICULUM,'r') as cv_input:
    cv_yml = yaml.load(cv_input, Loader=yaml.FullLoader)
    template = Template(template_file.read())
    with open(OUTPUT,'w') as output_file:
      output_file.write(template.render(cv=cv_yml))

os.system('pdflatex {}'.format(OUTPUT))
