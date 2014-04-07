#	This file is part of python-flac.
#
#	Copyright (c) 2014 Christian Schmitz <tynn.dev@gmail.com>
#
#	python-flac is free software: you can redistribute it and/or modify
#	it under the terms of the GNU Lesser General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	python-flac is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU Lesser General Public License for more details.
#
#	You should have received a copy of the GNU Lesser General Public License
#	along with python-flac.  If not, see <http://www.gnu.org/licenses/>.

""" Unit tests for the flac package """

import unittest

def load_tests(loader, tests, pattern):
	from . import test_flac_format
	modules = [
		test_flac_format,
	]
	tests = unittest.TestSuite(tests)
	for module in modules :
		tests.addTests(loader.loadTestsFromModule(module))
	return tests

