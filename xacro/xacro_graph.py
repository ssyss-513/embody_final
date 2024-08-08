import os
import re
from graphviz import Digraph

def find_xacro_includes(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        includes = re.findall(r'<xacro:include\s+filename="([^"]+)"', content)
    return includes

def add_file_to_graph(file_path, graph, xacro_directory, visited):
    if not os.path.isfile(file_path) or file_path in visited:
        return
    
    visited.add(file_path)
    includes = find_xacro_includes(file_path)
    node_name = os.path.relpath(file_path, xacro_directory)
    graph.node(node_name)
    
    for include in includes:
        include_path = os.path.abspath(os.path.join(os.path.dirname(file_path), include))
        include_node_name = os.path.relpath(include_path, xacro_directory)
        graph.edge(node_name, include_node_name)
        print(f"File: {node_name} includes {include_node_name}")
        
        add_file_to_graph(include_path, graph, xacro_directory, visited)

def create_dependency_graph(xacro_directories):
    dot = Digraph(comment='Xacro File Dependency Graph')
    visited = set()
    
    for xacro_directory in xacro_directories:
        for root, _, files in os.walk(xacro_directory):
            for file in files:
                if file.endswith('.xacro'):
                    file_path = os.path.join(root, file)
                    add_file_to_graph(file_path, dot, xacro_directory, visited)
    
    return dot

xacro_directories = [
    '/home/sen/ros/hand_arm_ws/src/allegro_hand_description/panda',
    '/home/sen/ros/hand_arm_ws/src/allegro_hand_description/common',
]

graph = create_dependency_graph(xacro_directories)

print(f"Graph source:\n{graph.source}")

graph.render('xacro_dependency_graph', view=True)




