#!/usr/bin/env python
"""This file starts the CLI
"""
from . import img2pdf


__version__ = "0.2.2"


def main():
    """Calling CLI
    """
    img2pdf.parse_cli()


if __name__ == "__main__":
    main()
