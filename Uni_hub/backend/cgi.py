import sys
from urllib.parse import parse_qs
sys.modules['cgi'] = sys.modules[__name__]
