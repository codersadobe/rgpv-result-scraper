'''
This file demonstrates the usage of the tool.

'''

import rgpvscrape as r

r.scrape(college_code='0103',
         branch='CS',
         year=19,
         roll_num_range=(1001, 1210),
         sem=1)
