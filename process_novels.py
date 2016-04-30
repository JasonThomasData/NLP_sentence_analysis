#!/usr/bin/env python
from stanford_NLTK import run_prog
from text_locations import novels_scrape_dict

print 'Processing novels'
run_prog(novels_scrape_dict)