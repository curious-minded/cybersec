import os
import argparse
import PyPDF2
import docx

def get_pdf_metadata(file_path):
    try:
        with open(file_path, 'rb') as pdf_file:
            pdf = PyPDF2.PdfReader(pdf_file)
            info = pdf.metadata
            
            print("PDF Metadata:")
            print("---------------")
            print("Title:", info.get('/Title', 'N/A'))
            print("Author:", info.get('/Author', 'N/A'))
            print("Subject:", info.get('/Subject', 'N/A'))
            print("Creator:", info.get('/Creator', 'N/A'))
            print("Producer:", info.get('/Producer', 'N/A'))
            print("Creation Date:", info.creation_date)
            print("Modification Date:", info.modification_date)
            print("Keywords:", info.get('/Keywords', 'N/A'))
            print("Trapped:", info.get('/Trapped', 'N/A'))

    except Exception as e:
        print("Error:", e)

def get_docx_metadata(file_path):
    try:
        doc = docx.Document(file_path)
        print("DOCX Metadata:")
        print("---------------")
        print("Language:", doc.core_properties.language or 'N/A')
        print("Title:", doc.core_properties.title or 'N/A')
        print("Author:", doc.core_properties.author or 'N/A')
        print("Subject:", doc.core_properties.subject or 'N/A')
        print("Keywords:", doc.core_properties.keywords or 'N/A')
        print("Creation Date:", doc.core_properties.created or 'N/A')
        print("Modification Date:", doc.core_properties.modified or 'N/A')

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    """parser = argparse.ArgumentParser(description = "Examine metadata in PDFs and Microsoft Documents")
    parser.add_argument("file_name",help = "path to the file")
    args = parser.parse_args()"""
    file_path = str(input("Enter file path/name: "))
    file_extension = os.path.splitext(file_path)

    if file_extension[1] == ".pdf":
        get_pdf_metadata(file_path)
    elif file_extension[1] == ".docx":
        get_docx_metadata(file_path)
    else:
        print("Unsupported file format. Make sure to remove the inverted commas and check as well if the file path given has an extension of .pdf or .docx.")
        
            
