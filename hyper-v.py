import os
import sys

a = sys.argv[1]
if a in ['auto', 'off']:
    os.system('bcdedit /set hypervisorlaunchtype {}'.format(a))
else:
    print('use \'hyper-v auto/off\' to set status of hyper-v')
