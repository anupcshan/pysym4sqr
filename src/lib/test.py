#!/usr/bin/python

# Will attempt to instantiate each class in the package.

import pyfoursquare

n = pyfoursquare.Network('root', 'v1', '919916816898', 'passwd', 'json')
cmgr = pyfoursquare.CacheMgr()
u = pyfoursquare.User(n, cmgr, '1')
v = pyfoursquare.Venue(n, cmgr, '1')
c = pyfoursquare.Checkin(n, cmgr, '1')
c.getObject()
