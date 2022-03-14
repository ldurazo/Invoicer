import invoicer.invoicer
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


invoicer.invoicer.generate_invoice()
