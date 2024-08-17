"""Readme file maker"""
from hashlib import md5
from typing import Generator, Tuple, List
import logging
import re
import sys


README_TEMPLATE = """DevOps handbook
===

**Table of contents**

{content}

"""

ITEM_TEMPLATE = "- [{name}]({path})\n"


class TreePaths:
    """Tree Paths for Hdfs files"""
    def __init__(self):
        """Initialize object"""
        self.domain = ""
        self.valid_path_pattern = re.compile(
            r"^[a-zA-Z0-9\+\=\[\]\.\:\/()!~&#@%_\s-]*$"
        )
        self.root_node = (".", md5(".".encode()).hexdigest())
        self.graph = {}

    def append_file_path(self, file_path: str):
        """Split file path to nodes and insert these nodes to tree

        Parameters:
            file_path(str): path of file in HDFS
        """
        if self.valid_path_pattern.match(string=file_path) is None:
            logging.warning("Path is invalid [%s]", file_path)
            return
        list_nodes = [node for node in file_path[len(self.domain):].split("/") if node.strip()]
        for i, value in enumerate(list_nodes[:-1]):
            key = (value, md5("/".join(list_nodes[:i + 1]).encode()).hexdigest())
            if not self.graph.get(key):
                self.graph[key] = set()
            self.graph.get(key).add((
                list_nodes[i + 1], md5("/".join(list_nodes[:i + 2]).encode()).hexdigest())
            )

    def list_all_leaf_node_paths(self, current: Tuple, path: str) -> Generator[str, None, None]:
        """List all paths of leaf nodes in tree

        Parameters:
            current(tuple(node_name: str, id: str)): current node identified
                by node name and its hashed value
            path(str): init file path

        Return list of paths corresponding to leaf nodes
        """
        path += f"/{current[0]}"
        if not self.graph.get(current):
            yield path
        else:
            for node in self.graph[current]:
                yield from self.list_all_leaf_node_paths(current=node, path=path)


def generate_readme_content(dirs: List[str]):
    """Generate content for structure of this project for README file"""
    tree_paths = TreePaths()
    content = ""
    for dir in dirs:
        tree_paths.append_file_path(dir)
    for dir in tree_paths.list_all_leaf_node_paths(current=tree_paths.root_node, path=tree_paths.domain):
        if dir == "/./README.md":
            continue
        content += ITEM_TEMPLATE.format(name=dir[3:], path=dir[1:])
    return README_TEMPLATE.format(content=content)


if __name__ == "__main__":
    md_files = sys.argv[1].split(",")
    print(generate_readme_content(dirs=md_files))
