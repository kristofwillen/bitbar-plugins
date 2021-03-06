#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3

# <bitbar.title>Docker status</bitbar.title>
# <bitbar.version>0.2.0</bitbar.version>
# <bitbar.author>Kristof Willen</bitbar.author>
# <bitbar.desc>Docker status</bitbar.desc>

import re
import subprocess
import pprint

output = subprocess.run("PATH=/bin:/usr/bin:/usr/local/bin docker ps",
  shell=True,
  stdout=subprocess.PIPE,
  stderr=subprocess.STDOUT,
  universal_newlines=True)


result = re.search("^CONTAINER ID", output.stdout)
if (result):
    numberofrunningcontainers = len(output.stdout.split('\n')) - 2
    print("[D] ► (", str(numberofrunningcontainers), ")")
    print('---')
    print(output.stdout)
else:
    print("[D] ✖")
