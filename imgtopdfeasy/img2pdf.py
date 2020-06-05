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
def convertToPageSize(imgPath,height,width):
    '''This converts the image so same size as specified. It doesn't scale it but creates a white background on it.
    A white background on which the image is pasted.
    '''
    from PIL import Image
    whiteBackground=Image.new('RGB',(height,width),color="#fff")
    mainImage=Image.open(imgPath)
    mainImageWidth,mainImageHeight=mainImage.size[0],mainImage.size[1]
    if height>mainImageHeight:
        pass
    whiteBackground.save(r"E:\hello.jpg")
    whiteBackground.show()
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
convertToPageSize(1000,1000)