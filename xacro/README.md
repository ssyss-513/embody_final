# Xacro File Dependency Graph

## 介绍

此项目包含一个Python脚本，用于生成和可视化xacro文件之间的引用关系图。xacro文件是ROS（机器人操作系统）中用于生成复杂URDF文件的宏文件。此脚本使用Graphviz来创建引用关系图，帮助理解和维护复杂的xacro文件结构。

## 先决条件

在运行此脚本之前，请确保你的系统已安装以下软件：

- **Python 3**: 脚本使用Python编写。
- **Graphviz**: 用于生成图形。
- **Graphviz Python 包**: 用于在Python中使用Graphviz。

### 安装Graphviz

```bash
sudo apt-get install graphviz
```

### 安装Graphviz Python 包

```bash
pip install graphviz
```

## 使用方法

### 1. 克隆或下载此项目

将此项目克隆到你的本地机器或直接下载项目文件。

### 2. 配置xacro文件目录

在`xacro_graph.py`脚本中，配置包含你所有xacro文件的目录路径。在脚本中找到以下部分：

```python
# 设置你的xacro文件目录路径列表
xacro_directories = [
    '/path/to/first/xacro_files_directory',
    '/path/to/second/xacro_files_directory',
    # 添加更多目录路径
]
```

将/path/to/first/xacro_files_directory和/path/to/second/xacro_files_directory替换为你实际的xacro文件目录路径。你可以添加多个目录路径。

