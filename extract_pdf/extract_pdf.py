"""
Requires PyPDF2
Usage: 'extract_pdf.py source.pdf 1-4 target.pdf'
"""

import PyPDF2 as pdf
import sys
import os


def check_args():
    if len(sys.argv) < 4:
        print("Too few arguments")
        return False
    elif not sys.argv[1].lower().endswith(".pdf") \
            or not sys.argv[3].lower().endswith(".pdf"):
        print("File type must be PDF")
        return False
    elif "-" not in sys.argv[2] \
            or not sys.argv[2].replace("-", "").isdigit():
        print("Page number must be only digits separated by -")
        return False
    pages = sys.argv[2].split("-")
    if pages[0] > pages[1]:
        print("Page start range must be lower than end range")
        return False
    return True


def do_extract(source, page_start, page_end, target):
    pages = []
    reader = pdf.PdfReader(source)
    if reader.getNumPages() < page_end:
        page_end = reader.getNumPages()-1
        print("Page range exceeds length of document, "
              "end of range changed to last page")
    for i in range(page_start-1, page_end):
        pages.append(reader.getPage(i))
    writer = pdf.PdfWriter()
    for page in pages:
        writer.add_page(page)
    writer.write(target)


def main():
    if check_args():
        page_range = sys.argv[2].split("-")
        page_start = page_range[0]
        if len(page_range) > 1:
            page_end = page_range[1]
        else:
            page_end = page_start
        if not os.path.exists(sys.argv[1]):
            print("File not found")
            sys.exit(1)
        do_extract(sys.argv[1], int(page_start), int(page_end), sys.argv[3])
    else:
        print("Arguments invalid, exiting")
        sys.exit(1)


if __name__ == "__main__":
    main()
