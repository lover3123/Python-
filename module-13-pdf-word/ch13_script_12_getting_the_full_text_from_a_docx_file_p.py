"""Chapter 13: PDF and Word Documents
Section: Getting the Full Text from a .docx File
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter13
Type: book script/example
PPT map: Syllabus Ch13: PyPDF2, python-docx
File: ch13_script_12_getting_the_full_text_from_a_docx_file_p.py (12 of 23 in this chapter)
"""

#! python3

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
