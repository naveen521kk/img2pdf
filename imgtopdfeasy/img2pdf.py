#!/usr/bin/env python
"""This module defines the funtions necessary for PDF conversion as well as CLI from argparse.

Has the following function:
    img2pdf()
    convertToPageSize()
    parse_cli()
"""
from pathlib import Path
from PIL import Image
from customerrors import ImageSizeTooSmall


def img2pdf(input, output, extension):
    """This function convert images to PDF of sepcific extension and saves in specific location.
    Parameters
    ----------
    input : path
        Input file folder to search images , in `input` directory.
    output : path
        Place to save output file (Doesn't need .pdf extension)
    extension : str
        The extension for Images to search for. Supports the images supported by Pillow.
        Eg. `jpeg`,`png etc.

    Returns
    -------
    str
        Filepath stored of PDF stored. Sucessfully saved ay `filepath`
    Raises
    ------
    FileNotFoundError
        If there is no files of given extension in the `input`.
    Examples
    --------
    >>> imgtopdfeasy.img2pdf.img2pdf(r"D:\Chemistry\Chemistry",r"D:\chemistrydemo","jpeg")
    D:\Chemistry\Chemistry\1.jpeg
    D:\Chemistry\Chemistry\2.jpeg
    D:\Chemistry\Chemistry\3.jpeg
    D:\Chemistry\Chemistry\4.jpeg
    D:\Chemistry\Chemistry\5.jpeg
    D:\Chemistry\Chemistry\6.jpeg
    D:\Chemistry\Chemistry\7.jpeg
    'Sucessfully saved at D:\\chemistrydemo.pdf'

    """
    imagelist = []
    for path in Path(input).rglob("*." + extension):
        if path == None:
            raise FileNotFoundError("NO files with Specified extension in the folder")
        im = Image.open(path)
        im1 = im.convert("RGB")
        imagelist.append(im1)
        print(path)
    for path in Path(input).rglob("*." + extension):
        im = Image.open(path)
        break
    im1 = im.convert("RGB")
    im1.save(output + ".pdf", save_all=True, append_images=imagelist[1:])
    return "Sucessfully saved at " + output + ".pdf"


def convertToPageSize(imgPath, height, width, border, bgColor):
    """This converts the image so same size as specified. It doesn't scale it but creates a white background on it.
    A white background on which the image is pasted.

    Parameters
    ----------
    imgPath : path
        Location of Image which need background.
    height : int
        Height in px.  As PIL standard.
    width : int
        Width in px. As PIL standard
    border : int
        Border width of the image.
    bgColor : ColorHex
        Colour of background.

    Returns
    -------
    PIL.Image.Image
        An PIL.Image.Image object with modified image data.
    """

    whiteBackground = Image.new("RGB", (width, height), color=bgColor)
    mainImage = Image.open(imgPath)
    mainImageWidth, mainImageHeight = mainImage.size[0], mainImage.size[1]
    if (
        height - 2 * (border) > mainImageHeight
        and width - 2 * (border) > mainImageWidth
    ):
        # Image height is inside background height
        whiteBackground.paste(
            mainImage,
            box=(
                ((width - 2 * (border) - mainImageWidth) // 2) + border,
                ((height - 2 * (border) - mainImageHeight) // 2) + border,
            ),
        )
    else:
        raise ImageSizeTooSmall(
            "The Images size combined with the border should be more than of the background."
        )
    return whiteBackground


def parse_cli():
    """This is the CLI for img2pdf using argparse.
    """
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        help="Input file folder full path. \n Realtive or abosolute",
        required=True,
    )
    parser.add_argument(
        "-o", "--output", help="Output file name,No pdf required", required=True
    )
    parser.add_argument(
        "-ext", "--extension", help="File extension of image to add.", required=True
    )
    args = parser.parse_args()
    inputPath = args.input
    outputPath = args.output
    extension = args.extension
    print(img2pdf(inputPath, outputPath, extension))


print(
    convertToPageSize(
        r"C:\Users\Naveen User\Desktop\tribonacci.png", 800, 800, 200, "#000"
    )
)
