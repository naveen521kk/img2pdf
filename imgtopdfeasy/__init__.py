#!/usr/bin/env python
'''This file starts the CLI
'''
from . import img2pdf

__version__ = '0.2.0'
def main():
    '''Calling CLI
    '''
    img2pdf.parse_cli()

