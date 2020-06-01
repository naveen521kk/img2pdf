# Img2pdf [![GitHub license](https://img.shields.io/github/license/naveen521kk/img2pdf)](https://github.com/naveen521kk/img2pdf/blob/master/LICENSE)  [![GitHub stars](https://img.shields.io/github/stars/naveen521kk/img2pdf)](https://github.com/naveen521kk/img2pdf/stargazers)
This is command line utility to convert images in a directory to  file.

This is very simple CLI to convert images in a directory to a PDF file. This use Pillow( PIL ), to achieve this.

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
pip install -r requirements.txt
```
would install necessary Requirements for it to run.

After that typing 
```sh
python img2pdf.py -h
```
in your terminal would run the program and show the necessary arguments required like below.
```ssh
usage: img2pdf.py [-h] -i INPUT -o OUTPUT -ext EXTENSION

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file folder full path. Realti
  -o OUTPUT, --output OUTPUT
                        Output file name,No pdf required
  -ext EXTENSION, --extension EXTENSION
                        File extension of image to add.
```

Each of it are self explanatory.

Crafted with 💓 by Naveen.
