# @Time    : 2019/10/16 0016 上午 8:47
# @Author  : h.user
# @Email   : h.user.com
# @File    : setup.py.py
# @Software: PyCharm

import setuptools

with open("README.md") as file:
    long_desc = file.read()

setuptools.setup(
    name="queue_plus",
    version="2.2",
    author="h.user",
    author_email="h.user@qq.com",
    description="a simple self-use class",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/h1code2/queue_plus/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=["queue"]
)
