#!/usr/bin/env python
# --------------------------------------------------------------------
# generate.py
#
# Author: Lain Musgrove (lain.musgrove@hearst.com)
# Date: Saturday September 16, 2023
# -------------------------------------------------------------------

import re
import os
import json
from pathlib import Path
from jinja2 import Template


# -------------------------------------------------------------------
def load_base16():
    xdefaults_file = Path.home() / ".Xdefaults"

    base16 = {}
    with open(xdefaults_file, "r") as infile:
        for line in infile.readlines():
            match = re.match(r"#define (base.*) (#.*)$", line.strip())
            if match:
                base16[match.group(1)] = match.group(2)
    return base16


# -------------------------------------------------------------------
def load_template(filename):
    with open(filename, "r") as infile:
        return Template(infile.read())


# -------------------------------------------------------------------
def load_font_config():
    with open(os.path.expanduser("~/.font/config.json"), "r") as infile:
        return json.load(infile)


# -------------------------------------------------------------------
BASE16 = load_base16()
FONT = load_font_config()


# -------------------------------------------------------------------
def main():
    template = load_template("warpd.config.jinja")
    print(template.render(base16=BASE16, font=FONT))


# -------------------------------------------------------------------
if __name__ == "__main__":
    main()
