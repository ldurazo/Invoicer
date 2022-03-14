from datetime import datetime

INVOICE_ID = "0001"

BILLED_BY = "Carl Johnson"
BILLED_BY_ADDRESS_LINE_1 = "Grove Street"
BILLED_BY_ADDRESS_LINE_2 = "Los Santos, CA 12345"
BILLED_BY_EMAIL = "cj@rockstar.com"
BILLED_BY_PHONE = "843-555-0124"

BILLED_TO = "Dunder Mifflin"
BILLED_TO_ADDRESS_LINE_1 = "1725 Slough Avenue"
BILLED_TO_ADDRESS_LINE_2 = "Scranton Business Park Suite 200"
BILLED_TO_ADDRESS_LINE_3 = "Scranton, PA 94129"
BILLED_TO_ADDRESS_LINE_4 = "United States"

INVOICE_ITEMS_HEADERS = ["DESCRIPTION", "HOURS", "RATE", "AMOUNT"]
INVOICE_ITEMS = [
    ("Assistant to the regional manager", 10,
     datetime(2020, 1, 1), datetime(2020, 1, 31))
]

WORKING_HOURS = 8
