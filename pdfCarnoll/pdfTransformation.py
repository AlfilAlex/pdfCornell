from re import S
import PyPDF2

filename = '1'
SCALE_FACTOR = 0.85

pdf_path = f"/home/alfilalex/Documentos/pythonPDF/Inputs/{filename}.pdf"
w_path = '/home/alfilalex/Documentos/pythonPDF/utils/whitebg.pdf'
s_path = '/home/alfilalex/Documentos/pythonPDF/utils/bg.pdf'


def pdfTransformation(pdf, SCALE_FACTOR: float, position: str = 'ur', w_path: str = w_path, s_path: str = s_path):
    writer = PyPDF2.PdfFileWriter()
    pdf = PyPDF2.PdfFileReader(pdf)

    for i in range(0, pdf.getNumPages()):
        page = pdf.getPage(i)
        w_page = getPDFPage(w_path)
        s_page = getPDFPage(s_path)

        w_page.mergePage(page)

        page_dim = getPDFDimentions(w_page)
        bg_dim = getPDFDimentions(s_page)

        gamma = getPageScaleFactor(page_dim, bg_dim, SCALE_FACTOR)

        tx, ty = getPosition(bg_dim, page_dim, gamma, position=position)

        s_page.mergeScaledTranslatedPage(
            w_page, scale=gamma, tx=tx, ty=ty)

        writer.addPage(s_page)

    return writer


def getPosition(bg_dim, page_dim, gamma, position):
    # +14 is necesary to compensate the original margin

    # UPPER
    if position == 'ur':
        tx = bg_dim[0] - float(page_dim[0])*gamma + 14
        ty = bg_dim[1] - float(page_dim[1])*gamma + 14

    elif position == 'ul':
        tx = 0
        ty = ty = bg_dim[1] - float(page_dim[1])*gamma + 14

    elif position == 'uc':
        tx = (bg_dim[0] - float(page_dim[0])*gamma + 14) / 2
        ty = bg_dim[1] - float(page_dim[1])*gamma + 14

    # CENTER
    elif position == 'cl':
        tx = 0
        ty = (bg_dim[1] - float(page_dim[1])*gamma + 14) / 2

    elif position == 'cc':
        tx = (bg_dim[0] - float(page_dim[0])*gamma + 14) / 2
        ty = (bg_dim[1] - float(page_dim[1])*gamma + 14) / 2

    elif position == 'cr':
        tx = bg_dim[0] - float(page_dim[0])*gamma + 14
        ty = (bg_dim[1] - float(page_dim[1])*gamma + 14) / 2

    # BOTTOM
    elif position == 'bl':
        tx = 0
        ty = 0

    elif position == 'bc':
        tx = (bg_dim[0] - float(page_dim[0])*gamma + 14) / 2
        ty = 0

    elif position == 'br':
        tx = bg_dim[0] - float(page_dim[0])*gamma + 14
        ty = 0

    return tx, ty


def getPDFDimentions(pdf_page):
    *_, x, y = pdf_page.mediaBox
    return x, y


def getPageScaleFactor(pdf_page_dim, bg_dim, SCALE_FACTOR):
    return (float(bg_dim[0]) * SCALE_FACTOR) / float(pdf_page_dim[0])


def getPDFPage(pdf_path):
    return PyPDF2.PdfFileReader(pdf_path).getPage(0)


if __name__ == "__main__":
    writer = pdfTransformation(
        pdf_path, SCALE_FACTOR, w_path=w_path, s_path=s_path)

    with open(f"./Outputs/{filename}_output.pdf", "wb+") as f:
        writer.write(f)
