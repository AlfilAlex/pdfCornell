import argparse
from pdfTransformation import pdfTransformation

parser = argparse.ArgumentParser(
    description='The program takes a specified filename, and tranform by scaling, and traslading over a baackgound with the dimensions of the original file')


parser.add_argument(
    '-f', '--filename', help='The name of the file to be converted', required=True)
parser.add_argument(
    '-s', '--scalefactor', help='Scale factor for the orginal file', default=0.85, required=False)
parser.add_argument(
    '-p', '--position', help='Position of the sscaled file', default='ur', required=False)


args = vars(parser.parse_args())

filename = args['filename']
SCALE_FACTOR = float(args['scalefactor'])
position = args['position']

if __name__ == '__main__':
    pdf_path = f"/home/alfilalex/Documentos/pythonPDF/Inputs/{filename}.pdf"
    writer = pdfTransformation(pdf_path, SCALE_FACTOR, position=position)

    with open(f"./Outputs/{filename}_output.pdf", "wb+") as f:
        writer.write(f)
