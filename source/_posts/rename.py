import os

bad_names = filter(lambda s: s.endswith('md'), os.listdir('.'))

import re

for name in bad_names:
    date = name[:10]
    print date
    with 