from datetime import datetime

# Periodically modifiable fields
INVOICE_ID = "000X"
# Calculations are inclusive of this value
INVOICE_START_DATE = "2020/1/1"
# Calculations are exclusive of this value
INVOICE_END_DATE = "2020/1/2"

# Fixed fields
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

HOURLY_RATE = 10
WORKING_HOURS = 8


# Table-specific variables
INVOICE_ITEMS_HEADERS = ["DESCRIPTION", "HOURS", "RATE", "AMOUNT"]
# Not configurable at the moment, used to calculate working hours, items in the tuple represent in order:
# Description, hourly rate, date start, date end. amount of hours and totals are calculated.
INVOICE_ITEMS = [
    ("Assistant to the regional manager", HOURLY_RATE,
     INVOICE_START_DATE, INVOICE_END_DATE)
]
