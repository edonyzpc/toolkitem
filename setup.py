from setuptools import setup, find_packages

setup(
        name="toolkitem",
        version="0.1b",
        description="",
        packages=find_packages(),
        install_requires=[
            "html2text>=(2015, 6, 6)",
            "BeautifulSoup4>=4.3.2",
            "requests>=2.7.0",
            "getpass",
            "calendar",
            "time",
            "argparse",
            "platform",
            "hashlib",
            "subprocess"
            ],
        )
