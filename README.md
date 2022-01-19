# PDF Cornel

This program allows to generate a [cornel] (https://en.wikipedia.org/wiki/Cornell_Notes) Taking note version of a desired pdf file.

## Usage

This is a CLI program, with the following flags:

-   -f: Filename of the pdf file to be transformed

-   -p: Position of the scaled file over the background

-   -s: Scale factor used to scale the original file

It's important to mention that position allows to manage two variables, vertically position (up, center, bottom) and horizontally (left, center, right)

## Example

The following command transform the file "my_pdf" by a 0.8 scale factor and the scaled file is positioned if a background with the size of A4 (ideally) page.

`python pdfCornel -f my_pdf -p ul -s 0.8`
