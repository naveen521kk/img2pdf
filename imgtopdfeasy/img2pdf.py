#!/usr/bin/env python
def img2pdf(input,output,extension):
    from PIL import Image
    from pathlib import Path
    imagelist=[]
    for path in Path(input).rglob('*.'+extension):
        im=Image.open(path)
        im1=im.convert('RGB')
        imagelist.append(im1)
        print(path)
    for path in Path(input).rglob('*.'+extension):
        im=Image.open(path)
        break
    im1=im.convert('RGB')
    im1.save(output+'.pdf',save_all=True,append_images=imagelist[1:])
    return 'Sucessfully saved at '+output+'.pdf'
def parse_cli():
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('-i','--input',help='Input file folder full path. \n Realtive or abosolute',required=True)
    parser.add_argument('-o','--output',help='Output file name,No pdf required',required=True)
    parser.add_argument('-ext','--extension',help='File extension of image to add.',required=True)
    args=parser.parse_args()
    inputPath=args.input
    outputPath=args.output
    extension=args.extension
    print(img2pdf(inputPath,outputPath,extension))
