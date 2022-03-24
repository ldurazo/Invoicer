from numbers import Number
from datetime import timedelta
import numpy as np
import functools
from borb.pdf.document import document
from borb.pdf.page.page import Page
from borb.pdf.canvas.color.color import HexColor, X11Color
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from datetime import datetime
from decimal import Decimal
from borb.pdf.pdf import PDF
import os
from configuration import *


def generate_invoice():
    pdf = document.Document()
    page = Page()
    pdf.append_page(page)
    page_layout = SingleColumnLayout(page)
    page_layout.add(_build_invoice_metadata())
    page_layout.add(_build_invoice_information())
    page_layout.add(Paragraph(" "))  # Spacing
    page_layout.add(_build_invoice_items())
    filename = "out/invoice-{}.pdf".format(INVOICE_ID)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, pdf)


def _build_invoice_metadata():
    now = datetime.now()
    invoice_metadata = Table(number_of_rows=2, number_of_columns=1)
    invoice_metadata.add(Paragraph("Date: %d/%d/%d" % (now.month, now.day, now.year),
                                   font="Helvetica-Bold",
                                   horizontal_alignment=Alignment.RIGHT))
    invoice_metadata.add(Paragraph("Invoice #{}".format(INVOICE_ID), font="Helvetica-Bold",
                                   horizontal_alignment=Alignment.RIGHT))

    invoice_metadata.no_borders()
    return invoice_metadata


def _build_invoice_information():
    invoice_info = Table(number_of_rows=6, number_of_columns=2)

    # Bill info headers
    invoice_info.add(
        Paragraph(
            "BILLED BY",
            background_color=HexColor("263238"),
            font_color=X11Color("White"),
        )
    )
    invoice_info.add(
        Paragraph(
            "BILLED TO",
            background_color=HexColor("263238"),
            font_color=X11Color("White"),
        )
    )

    # Row 1
    invoice_info.add(Paragraph(BILLED_BY))
    invoice_info.add(Paragraph(BILLED_TO))

    # Row 2
    invoice_info.add(Paragraph(BILLED_BY_ADDRESS_LINE_1))
    invoice_info.add(Paragraph(BILLED_TO_ADDRESS_LINE_1))

    # Row 3
    invoice_info.add(Paragraph(BILLED_BY_ADDRESS_LINE_2))
    invoice_info.add(Paragraph(BILLED_TO_ADDRESS_LINE_2))

    # Row 4
    invoice_info.add(Paragraph(BILLED_BY_PHONE))
    invoice_info.add(Paragraph(BILLED_TO_ADDRESS_LINE_3))

    # Row 5
    invoice_info.add(Paragraph(BILLED_BY_EMAIL))
    invoice_info.add(Paragraph(BILLED_TO_ADDRESS_LINE_4))

    invoice_info.set_padding_on_all_cells(
        Decimal(2), Decimal(2), Decimal(2), Decimal(2))
    invoice_info.no_borders()
    return invoice_info


def _build_invoice_items():
    invoice_items = Table(
        column_widths=[40, 20, 20, 20], number_of_rows=len(INVOICE_ITEMS) + 4, number_of_columns=4)
    for h in INVOICE_ITEMS_HEADERS:
        invoice_items.add(
            TableCell(
                Paragraph(h, font_color=X11Color("White")),
                background_color=HexColor("000000"),
            )
        )
        odd_color = HexColor("BBBBBB")
    even_color = HexColor("FFFFFF")

    invoice_total = 0
    for row_number, item in enumerate(INVOICE_ITEMS):
        c = even_color if row_number % 2 == 0 else odd_color

        invoice_item_description = _build_item_description(item)
        invoice_item_hours = _build_item_hours(item)
        invoice_item_total = _build_item_total(item, invoice_item_hours)
        invoice_total += invoice_item_total
        invoice_rate = str(item[1])

        invoice_items.add(
            TableCell(Paragraph(invoice_item_description), background_color=c))
        invoice_items.add(
            TableCell(Paragraph(str(invoice_item_hours)), background_color=c))
        invoice_items.add(
            TableCell(Paragraph(invoice_rate), background_color=c))
        invoice_items.add(
            TableCell(Paragraph("$" + str(invoice_item_total)), background_color=c))

    # Some empty rows to have a fixed number of rows for styling purposes
    for row_number in range(3, 5):
        c = even_color if row_number % 2 == 0 else odd_color
        for _ in range(0, 4):
            invoice_items.add(TableCell(Paragraph(" "), background_color=c))

    invoice_items.add(TableCell(Paragraph("Total", font="Helvetica-Bold",
                      horizontal_alignment=Alignment.RIGHT), col_span=3,))
    invoice_items.add(TableCell(Paragraph("${}".format(
        invoice_total), horizontal_alignment=Alignment.RIGHT)))

    invoice_items.set_padding_on_all_cells(
        Decimal(2), Decimal(2), Decimal(2), Decimal(2))
    invoice_items.no_borders()
    return invoice_items


def _build_item_description(item):
    return "{} {} - {}".format(
        item[0], item[2], (datetime.strptime(item[3], "%Y/%m/%d") + timedelta(days=-1)).strftime("%Y/%m/%d"))


def _build_item_total(item, invoice_item_hours):
    return round(item[1] * invoice_item_hours, 2)


def _build_item_hours(item):
    return np.busday_count(
        datetime.strptime(item[2], "%Y/%m/%d").date(), datetime.strptime(item[3], "%Y/%m/%d").date()) * WORKING_HOURS


if __name__ == "__main__":
    generate_invoice()
