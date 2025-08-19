import time
from datetime import datetime

import crsp_functions as crsp

# import methods as my

# these must be run using qos=bus for memory and internet access
# need 10 cores
crsp.msf_first_load()
# crsp.dsf_first_load()
# quit()

# update dsf file
# crsp.dsf_update()

# update msf file
crsp.msf_update()
