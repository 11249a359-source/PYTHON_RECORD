from PyPDF2 import PdfReader, PdfWriter

writer = PdfWriter()

pdf_files = ["file1.pdf", "file2.pdf"]

for pdf in pdf_files:
    reader = PdfReader(pdf)
    print(f"{pdf} has {len(reader.pages)} pages.")

    for page_num in range(min(2, len(reader.pages))):
        writer.add_page(reader.pages[page_num])

with open("merged_selected_pages.pdf", "wb") as output:
    writer.write(output)

print("Selected pages merged successfully into merged_selected_pages.pdf")
