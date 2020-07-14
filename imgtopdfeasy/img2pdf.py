#!/usr/bin/env python
"""This module defines the funtions necessary for PDF conversion as well as CLI from argparse.

Has the following function:
    img2pdf()
    convertToPageSize()
    parse_cli()
"""
from pathlib import Path
from PIL import Image
from .customerrors import ImageSizeTooSmall
import os
import platform
import subprocess


def img2pdf(
    input, output, extension, have_border=False, border_color="white", border_size=10
):
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
    have_border : bool
        Whether the images need to have border have border or not. Useful for differet size images.
        Defaults to False
    border_color: str
        The hexcodes of colour you want as border colour. This needs to be Parsed by Pillow.
        Default to white.
    border_size: int
        This is the size of border on one side of the page. Defaults to 10

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
    Found Image at: D:\Chemistry\Chemistry\1.jpeg
    Found Image at: D:\Chemistry\Chemistry\2.jpeg
    Found Image at: D:\Chemistry\Chemistry\3.jpeg
    Found Image at: D:\Chemistry\Chemistry\4.jpeg
    Found Image at: D:\Chemistry\Chemistry\5.jpeg
    Found Image at: D:\Chemistry\Chemistry\6.jpeg
    Found Image at:D:\Chemistry\Chemistry\7.jpeg
    'Sucessfully saved at D:\\chemistrydemo.pdf'

    """
    imageDict = {}
    image_count = 0
    for path in Path(input).rglob("*." + extension):
        if path == None:
            raise FileNotFoundError("NO files with Specified extension in the folder")
        im = Image.open(path)
        im1 = im.convert("RGB")
        imageDict[image_count] = [im1, im1.size]
        image_count += 1
        print("Found Image at: ", path)

    maxImageWidth, maxImageHeight = (
        max([i[1][0] for i in imageDict.values()]),
        max([i[1][1] for i in imageDict.values()]),
    )
    imagelist = []
    if have_border:
        for image_nums in imageDict:
            imagelist.append(
                convertToPageSize(
                    imageDict[image_nums][0],
                    maxImageHeight + (border_size * 2 + 1),
                    maxImageWidth + (border_size * 2 + 1),
                    border_size,
                    border_color,
                )
            )
    else:
        for image_nums in imageDict:
            imagelist.append(imageDict[image_nums][0])
    im = imagelist[0]
    im1 = im.convert("RGB")
    im1.save(output + ".pdf", save_all=True, append_images=imagelist[1:])
    return "Sucessfully saved at " + output + ".pdf"


def convertToPageSize(mainImage, height, width, border, bgColor):
    """This converts the image so same size as specified. It doesn't scale it but creates a white background on it.
    A white background on which the image is pasted.

    Parameters
    ----------
    mainImage : PIL.Image.Image
        An Image Object from Pillow
    height : int
        Height in px.  As PIL standard.
    width : int
        Width in px. As PIL standard.
    border : int
        Border width of the image on one side.
    bgColor : ColorHex
        Colour of background.

    Returns
    -------
    PIL.Image.Image
        An PIL.Image.Image object with modified image data.
    """

    whiteBackground = Image.new("RGB", (width, height), color=bgColor)
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

    parser = argparse.ArgumentParser(
        prog="img2pdf",
        description="Converts Images To Pdf",
        epilog="Made with ❤ By Naveen",
    )
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
    parser.add_argument(
        "--border", help="Add border to Images", required=False, action="store_true"
    )
    parser.add_argument(
        "--border_size", help="Size of border of Images", required=False,
    )
    parser.add_argument(
        "--border_color", help="Colour of Border of Images", required=False,
    )
    args = parser.parse_args()
    inputPath = args.input
    outputPath = args.output
    extension = args.extension
    have_border = args.border
    border_size = int(args.border_size)
    border_color = args.border_color
    print(
        img2pdf(
            inputPath, outputPath, extension, have_border, border_color, border_size
        )
    )
    outputPath = outputPath + ".pdf"
    current_os = platform.system()
    if current_os == "Windows":
        os.startfile(outputPath)
    else:
        commands = []
        if current_os == "Linux":
            commands.append("xdg-open")
        elif current_os.startswith("CYGWIN"):
            commands.append("cygstart")
        else:  # Assume macOS
            commands.append("open")
        commands.append("-R")
        commands.append(outputPath)
        # commands.append("-g")
        FNULL = open(os.devnull, "w")
        subprocess.call(commands, stdout=FNULL, stderr=sp.STDOUT)
        FNULL.close()
