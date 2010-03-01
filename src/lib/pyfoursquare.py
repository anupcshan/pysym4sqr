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

	def __init__(self, api_root, username, password, format):
		"""
			api_root: Root URL of the webservice API
			username: Username of a valid user
			password: Password of the user
			format: json / xml
		"""

		self.api_root = api_root
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
			Get SelfUser object corresponding to currently logged in user.
		"""
		if currentUser == None:
			# TODO : Make call to get current user object
			currentUser = None

		return currentUser

class _Networked(object):
	"""An abstract webservices object"""

	network = None

	def __init__(self, network):
		self.network = network

class _User(_Networked):
	"""User Base object"""

	id = None
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

	def __init__(self, network):
		_Networked.__init__(network)

	def isMe(self):
		pass

	def isFriend(self):
		pass

class SelfUser(_User):
	"""Current User. Only one object of this class can be created."""

	def __init__(self, network):
		_User.__init__(network)

	def isMe(self):
		return True

	def isFriend(self):
		return False

class User(_User):
	"""User other than current user."""

	friendstatus = None

	def __init__(self, network):
		_User.__init__(network)

	def isMe(self):
		return False

	def isFriend(self):
		return friendstatus == "friend" ? True : False
		# TODO : Handle friend request pending states

class Venue(_Networked):
	"""A venue."""

	id = None
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

	def __init__(self, network):
		_Networked.__init__(network)

class Checkin(_Networked):
	"""A checkin."""

	id = None
	created = None
	display = None
	venue = None
	shout = None
	user = None

	def __init__(self, network):
		_Networked.__init__(network)
