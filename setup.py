from distutils.core import setup

with open("./Readme.md", "r") as f:
    long_description = f.read()

setup(
    name="main",
    version="1.0",
    description="This program checks to see if the digits given is "
                "a valid ISBN digit. If it's a ISBN-10 digit it gets"
                "converted to a ISBN-13 digit",
    author="Ilerioluwa Akinola",
    author_email="ilerioluwaakinola@akinola",
    url="https://github.com/IAkinola/ISBN-Digits",
    py_modules=["main", "test_isbn"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
