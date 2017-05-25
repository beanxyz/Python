c='/cgi-bin/mmwebwx-bin/webwxgetheadimg?=seq=647040681&username=@@5a9ead9065f470577f86aaca1be9270b25c015481ef592037411321c69e01a92&skey=@crypt_228f9bb1_01303257f826732d31d51cc660f8f523'


import re
a=c.split('=@')[1].split('&')[0]
print(a)


re.search('(@\w+)',c)