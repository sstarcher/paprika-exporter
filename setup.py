import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="papexp",
    version="0.4.1",
    author="Chris Nicholson",
    author_email="datapolitical@gmail.com",
    description="A simple exporter for the paprika app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.25.0',
        'python-dotenv>=0.15.0',
        'PyYAML>=5.4'
    ]
)
