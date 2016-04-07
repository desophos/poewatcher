from setuptools import setup

setup(
    name="poewatcher",
    packages=["poewatcher"],
    version="0.1b",
    description="PoE log watcher",
    author="Guillaume Dupuy",
    author_email="glorf@glorf.fr",
    url="https://github.com/Gloorf/poewatcher",
    license="AGPL v3+",
    keywords=["poe"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)"
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
    ],
    install_requires=["click", "configparser", "pyglet", "pyperclip", "requests"],
    entry_points={
        "console_scripts": [
            "poewatcher = poewatcher.main:main",
            "poewatcher-sendcsv = poewatcher.send_csv:main"
        ]
    },
    package_data={
        "poewatcher": ["config.ini", "data/*"]
    }
)
