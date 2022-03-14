import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import invoicer.invoicer

invoicer.invoicer.generate_invoice()