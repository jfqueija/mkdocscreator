import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mkdocscreator',
    version='0.1',
    scripts=['mkdocscreator'],
    author="José Fº",
    author_email="pepekiko@gmail.com",
    description="Template for create mkdocs structure",
    long_description="Template for create mkdocs structure",
    long_description_content_type="text/markdown",
    url="https://github.com/lorthsun/mkdocscreator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 ) 