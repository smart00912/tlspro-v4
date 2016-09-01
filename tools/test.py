# -*- coding:utf-8 -*-
from gpgfunc import decFile

with decFile('keys.tgz.gpg', 'fgmn88+IP.1706') as f:
	tt=f.read()