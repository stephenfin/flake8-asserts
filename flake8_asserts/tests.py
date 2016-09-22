# Copyright (c) 2016, Stephen Finucane <stephenfinucane@hotmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from flake8_asserts import checks


class TestCase(unittest.TestCase):

    def assertCheck(self, check_func, logical_line):
        if not list(check_func(logical_line, False)):
            raise AssertionError('Check %s did not fail.' %
                                 check_func.__name__)

    def assertNoqa(self, check_func, logical_line):
        if list(check_func(logical_line, True)):
            raise AssertionError('Check %s did not skip #noqa.' %
                                 check_func.__name__)

    def test_assert_true(self):
        for value in [
                'self.assertEqual(x, True)',
                'self.assertEqual(True, x)',
                'self.assertNotEqual(x, False)',
                'self.assertNotEqual(False, x)',
                'self.assertEqual(x, False)',
                'self.assertEqual(False, x)',
                'self.assertNotEqual(x, True)',
                'self.assertNotEqual(False, x)']:
            self.assertCheck(checks.assert_true, value)

        self.assertNoqa(checks.assert_true, 'self.assertEqual(x, True)')

    def test_assert_equal(self):
        for value in [
                'self.assertTrue(x == "test")',
                'self.assertTrue(x != "xyz")',
                'self.assertFalse(x != "test")',
                'self.assertFalse(x == "xyz")']:
            self.assertCheck(checks.assert_equal, value)

        self.assertNoqa(checks.assert_equal, 'self.assertFalse(x == "xyz")')

    def test_assert_in(self):
        for value in [
                'self.assertTrue(1 in x)',
                'self.assertFalse(6 in x)',
                'self.assertTrue(6 not in x)',
                'self.assertFalse(1 not in x)']:
            self.assertCheck(checks.assert_in, value)

        self.assertNoqa(checks.assert_true, 'self.assertFalse(1 not in x)')

    def test_assert_is(self):
        for value in [
                'self.assertTrue(a is b)',
                'self.assertTrue(a is not b)',
                'self.assertFalse(a is b)',
                'self.assertFalse(a is not b)']:
            self.assertCheck(checks.assert_is, value)

        self.assertNoqa(checks.assert_true, 'self.assertFalse(a is not b)')

    def test_assert_is_none(self):
        for value in [
                'self.assertIs(x, None)',
                'self.assertIs(None, x)',
                'self.assertIsNot(x, None)',
                'self.assertIsNot(None, x)']:
            self.assertCheck(checks.assert_is_none, value)

        self.assertNoqa(checks.assert_true, 'self.assertIsNot(None, x)')

    def test_assert_is_instance(self):
        for value in [
                'self.assertTrue(isinstance(x, int))',
                'self.assertFalse(isinstance(x, bool))']:
            self.assertCheck(checks.assert_is_instance, value)

        self.assertNoqa(checks.assert_true,
                        'self.assertFalse(isinstance(x, bool))')
