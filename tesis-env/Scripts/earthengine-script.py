#!c:\users\usuario\desktop\tesis_\tesis-env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'earthengine-api==0.1.316','console_scripts','earthengine'
__requires__ = 'earthengine-api==0.1.316'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('earthengine-api==0.1.316', 'console_scripts', 'earthengine')()
    )
