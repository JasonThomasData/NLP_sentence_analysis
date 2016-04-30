#!/usr/bin/env python
from stanford_NLTK import run_prog
from text_locations import articles_essays_scrape_dict

print 'Processing articles and essays'
run_prog(articles_essays_scrape_dict)