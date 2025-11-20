AIM:
To write a python program to combine select pages from many PDFs.

ALGORITHM:
1. Start
2. Import the required module: PyPDF2
3. Create a PdfWriter object to write the final output PDF
4. For each input PDF:
a) Open the file in binary read mode
b) Create a PdfReader object
c) For each required page number:
i) Check if the page exists
ii) Add the selected page to the PdfWriter object

5. Write the combined pages into a new PDF file
6. Close all file streams
7. End
REQUIRED LIBRARY:
1. Page numbers are zero-indexed (0 = page 1).
2. Make sure all input PDF files exist in the same directory or give full paths.
3. Install PyPDF2 if not already installed:
Install using the statement - pip install PyPDF2
PROGRAM:
import PyPDF2
def combine_selected_pages(pdf_info_list, output_filename):
&quot;&quot;&quot;
Combines selected pages from multiple PDF files.
:param pdf_info_list: List of tuples (pdf_filename, list_of_page_numbers)
:param output_filename: Name of the output PDF file
&quot;&quot;&quot;

pdf_writer = PyPDF2.PdfWriter()

for pdf_file, page_numbers in pdf_info_list:
with open(pdf_file, &#39;rb&#39;) as file:
pdf_reader = PyPDF2.PdfReader(file)
total_pages = len(pdf_reader.pages)

for page_num in page_numbers:
if 0 &lt;= page_num &lt; total_pages:
pdf_writer.add_page(pdf_reader.pages[page_num])
else:
print(f&quot;Page number {page_num} is out of range in {pdf_file}&quot;)

with open(output_filename, &#39;wb&#39;) as output_file:
pdf_writer.write(output_file)
print(f&quot;Combined PDF saved as &#39;{output_filename}&#39;&quot;)

# Example usage:
pdf_inputs = [
(&quot;sample1.pdf&quot;, [0, 2]), # 1st and 3rd page from sample1.pdf
(&quot;sample2.pdf&quot;, [1]), # 2nd page from sample2.pdf
(&quot;sample3.pdf&quot;, [0, 1]) # 1st and 2nd pages from sample3.pdf
]

combine_selected_pages(pdf_inputs, &quot;combined_output.pdf&quot;)

OUTPUT:

Combined PDF saved as &#39;combined_output.pdf&#39;
