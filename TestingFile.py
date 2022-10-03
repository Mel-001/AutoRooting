

import os
from ctypes import windll

def CheckAdminRights():
    """Return True if user has admin privileges.

    Raises:
        AdminStateUnknownError if user privileges cannot be determined.
    """
    try:
        return os.getuid() == 0
    except AttributeError:
        pass
    try:
        return windll.shell32.IsUserAnAdmin() == 1
    except AttributeError:
        print('Program hasn\'t been executed as Administrator Rights!')
        print('Quitting...')
        exit()



