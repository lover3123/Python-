# Ch13 | 01/23 | Extracting Text from PDFs [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter13

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
# OUT:    19
pageObj = pdfReader.getPage(0)
pageObj.extractText()
# OUT:    'OOFFFFIICCIIAALL BBOOAARRDD MMIINNUUTTEESS Meeting of March 7, 2015
# OUT:    \n     The Board of Elementary and Secondary Education shall provide leadership
# OUT:    and create policies for education that expand opportunities for children,
# OUT:    empower families and communities, and advance Louisiana in an increasingly
# OUT:    competitive global market. BOARD of ELEMENTARY and SECONDARY EDUCATION '
