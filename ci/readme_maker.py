"""Readme file maker"""
from typing import List
import sys


ITEM_TEMPLATE = "- [{name}]({path})\n"


def generate_readme_content(dirs: List[str]):
    """Generate content for structure of this project for README file"""
    with open(file="./ci/template.md", mode="r", encoding="utf-8") as template_file:
        readme_template = template_file.read()
        content = ""
        for path in dirs:
            if path == "./README.md":
                continue
            elements = path.split("/")
            content += ITEM_TEMPLATE.format(name="-".join(elements[2:-1]), path="/".join(elements))
        return readme_template.format(content=content)


if __name__ == "__main__":
    md_files = sys.argv[1].split(",")
    print(generate_readme_content(dirs=md_files))
