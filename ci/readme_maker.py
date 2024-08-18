"""Readme file maker"""
from typing import List
import sys


README_TEMPLATE = """DevOps handbook
===

**Table of contents**

{content}

"""

ITEM_TEMPLATE = "- [{name}]({path})\n"


def generate_readme_content(dirs: List[str]):
    """Generate content for structure of this project for README file"""
    content = ""
    for path in dirs:
        if path == "./README.md":
            continue
        elements = path.split("/")
        content += ITEM_TEMPLATE.format(name="-".join(elements[1:-1]), path="/".join(elements))
    return README_TEMPLATE.format(content=content)


if __name__ == "__main__":
    md_files = sys.argv[1].split(",")
    print(generate_readme_content(dirs=md_files))
