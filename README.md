# Img2pdf [![GitHub license](https://img.shields.io/github/license/naveen521kk/img2pdf)](https://github.com/naveen521kk/img2pdf/blob/master/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/naveen521kk/img2pdf)](https://github.com/naveen521kk/img2pdf/stargazers)[![](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
This is command line utility to convert images in a directory to  PDF file.

This is very simple CLI to convert images in a directory to a PDF file. This use Pillow( PIL ), to achieve this.

### Using pip Version

Type the below command to install img2pdf.

```sh
pip install imgtopdfeasy
```

Typing `img2pdf` in your terminal would give the options available and the Parameters required like below.

```sh
usage: img2pdf [-h] -i INPUT -o OUTPUT -ext EXTENSION [--border]
               [--border_size BORDER_SIZE] [--border_color BORDER_COLOR]

Converts Images To Pdf

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file folder full path. Realtive or abosolute
  -o OUTPUT, --output OUTPUT
                        Output file name,No pdf required
  -ext EXTENSION, --extension EXTENSION
                        File extension of image to add.
  --border              Add border to Images
  --border_size BORDER_SIZE
                        Size of border of Images
  --border_color BORDER_COLOR
                        Colour of Border of Images

Made with ❤ By Naveen
```

Its that simple. Typing

```sh
img2pdf -i <Path-to-folder> -o <Path-to-output-file> -ext <extension-of-image-to-add>
```

would simply create you required file.

Note: Path to output file doesn't require `.pdf` to be added at last. Also, border feature would be documented soon.

### Using Development Version

To use this go to the directory where you have images. Then type the commands below.

```sh
git clone https://github.com/naveen521kk/img2pdf.git
```

This create a folder called `img2pdf`. Then go into the folder by

```sh
cd img2pdf
```

After that typing 

```sh
poetry install
```
would install necessary Requirements for it to run. The above command requires [python-poetry](https://python-poetry.org) installed.

After that typing 
```sh
python imgtopdfeasy/img2pdf.py -h
```
in your terminal would run the program and show the necessary arguments required like below.
```sh
usage: img2pdf [-h] -i INPUT -o OUTPUT -ext EXTENSION [--border]
               [--border_size BORDER_SIZE] [--border_color BORDER_COLOR]

Converts Images To Pdf

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file folder full path. Realtive or abosolute
  -o OUTPUT, --output OUTPUT
                        Output file name,No pdf required
  -ext EXTENSION, --extension EXTENSION
                        File extension of image to add.
  --border              Add border to Images
  --border_size BORDER_SIZE
                        Size of border of Images
  --border_color BORDER_COLOR
                        Colour of Border of Images

Made with ❤ By Naveen
```

Each of it are self explanatory.

Crafted with 💓 by Naveen.
