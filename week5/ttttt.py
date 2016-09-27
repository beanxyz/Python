#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import logging
#logging.warning("user [alex] attempted wrong password more than 3 times")
#logging.critical("server is down")

logging.basicConfig(filename='example.log',level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('This message should go to the log file')
logging.info('dsfsdf')
logging.warning('sdfsfsdf')