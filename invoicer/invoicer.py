from borb.pdf.document import document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from datetime import datetime
from decimal import Decimal
from borb.pdf.pdf import PDF

def generate_invoice():
  pdf = document.Document()
  page = Page()
  pdf.append_page(page)
  page_layout = SingleColumnLayout(page)
  page_layout.add(Paragraph(" asdfasdf"))
  with open("out/output.pdf", "wb") as pdf_file_handle:
    PDF.dumps(pdf_file_handle, pdf)

def _build_invoice_information():    
    table_001 = Table(number_of_rows=5, number_of_columns=3)
	
    table_001.add(Paragraph("[Street Address]"))    
    table_001.add(Paragraph("Date", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))    
    now = datetime.now()    
    table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year)))
	
    table_001.add(Paragraph("[City, State, ZIP Code]"))    
    table_001.add(Paragraph("Invoice #", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))
    table_001.add(Paragraph("%d" % random.randint(1000, 10000)))   
	
    table_001.add(Paragraph("[Phone]"))    
    table_001.add(Paragraph("Due Date", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))
    table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year))) 
	
    table_001.add(Paragraph("[Email Address]"))    
    table_001.add(Paragraph(" "))
    table_001.add(Paragraph(" "))

    table_001.add(Paragraph("[Company Website]"))
    table_001.add(Paragraph(" "))
    table_001.add(Paragraph(" "))

    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))    		
    table_001.no_borders()
    return table_001

if __name__ == "__main__":
    generate_invoice()