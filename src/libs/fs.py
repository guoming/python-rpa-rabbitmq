import codecs
import os
import sys
from pathlib import Path
from posixpath import join


# 文件读取
def fs_readLines(fileName):
    # 第一步：（以只读模式）打开文件
    f = codecs.open(fileName, 'r')

    # 第二步：读取文件内容
    lines = f.readlines()

    # 第三步：关闭文件
    f.close()

    return lines


# 文件读取
def fs_read(fileName):
    # 第一步：（以只读模式）打开文件
    f = codecs.open(fileName, 'r')

    # 第二步：读取文件内容
    lines = f.read()

    # 第三步：关闭文件
    f.close()

    return lines


# 文件写入
def fs_write(fileName, content):
    # 第一步：（以只读模式）打开文件
    f = codecs.open(fileName, 'w', "utf-8")
    # 第二步：读取文件内容
    f.write(content)
    # 第三步：关闭文件
    f.close()


# 文件写入
def fs_append(fileName, content):
    # 第一步：（以只读模式）打开文件
    f = codecs.open(fileName, 'a+', "utf-8")
    # 第二步：读取文件内容
    f.write(content)
    # 第三步：关闭文件
    f.close()


# 文件写入
def fs_appendLine(fileName, content):
    # 第一步：（以只读模式）打开文件
    f = codecs.open(fileName, 'a+', 'utf-8')
    # 第二步：读取文件内容
    f.write(content)
    f.write("\n")
    # 第三步：关闭文件
    f.close()


# 文件写入
def fs_remove(fileName):
    ret = False

    dir = Path(fileName)
    if dir.exists():
        try:
            # 第一步：（以只读模式）打开文件
            os.remove(fileName)
            ret = True
        except IOError:
            print("delete file " + fileName + " failed.reason=FileNotFoundError")

        finally:
            print("delete file:", fileName)

    return ret