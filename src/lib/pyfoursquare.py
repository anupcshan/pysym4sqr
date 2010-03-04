#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010 Anup C Shan
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA

"""
pyfoursquare - A Python interface to Foursquare

Design and structure is borrowed from pylast - http://code.google.com/p/pylast
Thanks to Amr Hassan!
"""

__author__ = 'Anup C Shan'
__copyright__ = "Copyright (C) 2010 Anup C Shan"
__license__ = "gpl"
__email__ = 'anupcshan@gmail.com'
__version__ = '0.1'

class Network(object):
	"""
		Network interface to Foursquare API.
	"""

	api_root = None
	username = None
	password = None
	format = None

	# "Global" objects / arrays containing all users / venues / checkins
	users = []
	venues = []
	checkins = []

	currentUser = None

	def __init__(self, api_root, api_version, username, password, format):
		"""
			api_root: Root URL of the webservice API
			api_version: API version (eg. v1, v2 etc)
			username: Username of a valid user
			password: Password of the user
			format: json / xml
		"""

		self.api_root = api_root
		self.api_version = api_version
		self.username = username
		self.password = password
		self.format = format

	def doLogin(self):
		"""
			Test whether username and password are valid.
		"""
		pass

	def getCurrentUser(self):
		"""
			Get SelfUser object corresponding to currently logged in
			user.
		"""
		if currentUser == None:
			# TODO : Make call to get current user object
			currentUser = None

		return currentUser

	def makeRequest(self, command, arguments, type, version = None, format =
			None):
		"""
			command: API command (eg. venues)
			arguments: Dict containing parameters to be sent
			type: GET / POST
			version: (Optional) API version parameter (will override
					self.version)
			format: (Optional) json / xml (will override
					self.format)
		"""
		if version == None:
			version = self.version
		if format == None:
			format = self.format

		url = self.api_root + '/' + version + '/' + command + '.' + format

		response = Request(url, arguments, type).execute()

class CacheMgr(object):
	"""Interface to stored and retrieve objects in cache"""

	# TODO : Add data members related to backend storage.

	def __init__(self):
		pass

	def writeback(self, type, object):
		"""
			Method to write a formatted object into the cache.
		"""
		pass

class CacheConfig(object):
	"""Cache configuration object"""

	cacheable = False
	cacheMaxAge = 0
	# Maximum age of a cache object before expiry (in seconds)
	# Negative value => cache valid forever

	def __init__(self, cacheable, cacheMaxAge):
		self.cacheable = cacheable
		self.cacheMaxAge = cacheMaxAge

class _Cacheable(object):
	"""Abstract cacheable object"""

	cacheconfig = None
	cachemgr = None
	objtype = None	# User/Venue/Checkin/...
	id = None # Key used to store object in cache

	def __init__(self, cacheable, cacheMaxAge, cachemgr, id, objtype):
		self.cacheconfig = CacheConfig(cacheable, cacheMaxAge)
		self.cachemgr = cachemgr
		self.id = id
		self.objtype = objtype

	def _cacheWriteback(self):
		"""
			Write object back into the cache. This method is to be
			called immediately after a network request.
		"""
		cacheMgr.writeback(self.objtype, self._cacheFormatObject())

	def _cacheFormatObject(self):
		"""
			Abstract method which defines the format of data to be
			stored in cache. Needs to be implemented by child class.
		"""
		pass

class Request(object):
	"""A network request object"""

	url = None
	arguments = None
	type = None

	def __init__(self, url, arguments, type):
		self.url = url
		self.arguments = arguments
		self.type = type

	def execute(self):
		# TODO : Write code for performing network request
		pass

class _Networked(object):
	"""An abstract webservices object"""

	network = None

	def __init__(self, network):
		self.network = network

class _User(_Networked, _Cacheable):
	"""User Base object"""

	firstname = None
	lastname = None
	photo = None
	gender = None
	phone = None
	email = None
	twitter = None
	facebook = None
	settings = None
	checkin = None
	badges = None

	def __init__(self, network, cachemgr, id):
		_Networked.__init__(self, network)
		_Cacheable.__init__(self, True, 3600, cachemgr, id, 'User')

	def isMe(self):
		pass

	def isFriend(self):
		pass

class SelfUser(_User):
	"""Current User. Only one object of this class can be created."""

	def __init__(self, network, cachemgr, id):
		_User.__init__(self, network, cachemgr, id)

	def isMe(self):
		return True

	def isFriend(self):
		return False

class User(_User):
	"""User other than current user."""

	friendstatus = None

	def __init__(self, network, cachemgr, id):
		_User.__init__(self, network, cachemgr, id)

	def isMe(self):
		return False

	def isFriend(self):
		if friendstatus == "friend":
			return True
		return False
		# TODO : Handle friend request pending states

class Venue(_Networked, _Cacheable):
	"""A venue."""

	name = None
	address = None
	crossstreet = None
	city = None
	state = None
	zip = None
	phone = None
	geolat = None
	geolong = None
	twitter = None
	stats = None
	tips = None
	tags = None
	links = None

	def __init__(self, network, cachemgr, id):
		_Networked.__init__(self, network)
		_Cacheable.__init__(self, True, 86400, cachemgr, id, 'Venue')

class Checkin(_Networked, _Cacheable):
	"""A checkin."""

	created = None
	display = None
	venue = None
	shout = None
	user = None

	def __init__(self, network, cachemgr, id):
		_Networked.__init__(self, network)
		_Cacheable.__init__(self, True, -1, cachemgr, id, 'Checkin')
