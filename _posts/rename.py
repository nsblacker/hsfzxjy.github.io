import os

bad_names = filter(lambda s: s.endswith('html'), os.listdir('.'))

import re

for name in bad_names:
    with open(name, 'r') as f:
        content = f.read()
        results = re.findall(r'permalink:\s*/(.+)/$', content, re.MULTILINE)
    if not results:
        os.rename(name, name[:-5]+'.md')
        continue
    os.rename(name, name[:11]+results[0]+'.md')