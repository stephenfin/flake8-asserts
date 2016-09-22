# Copyright (c) 2012, Cloudscaling
# Copyright (c) 2016, Stephen Finucane <stephenfinucane@hotmail.com>
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import re

from flake8_asserts import core


@core.flake8ext
def assert_true(logical_line, noqa):
    """Enforce use of assertTrue/assertFalse.

    Prevent use of assertEqual(A, True|False), assertEqual(True|False, A),
    assertNotEqual(A, True|False), and assertNotEqual(True|False, A)

    A101
    """
    _re_start = re.compile(r'assert(Not)?Equal\((True|False),')
    _re_end = re.compile(r'assert(Not)?Equal\(.*,\s+(True|False)\)$')

    if noqa:
        return

    if _re_start.search(logical_line) or _re_end.search(logical_line):
        yield (6, "A101: assertEqual(A, True|False), "
               "assertEqual(True|False, A), assertNotEqual(A, True|False), "
               "or assertEqual(True|False, A) must not be used. Use "
               "assertTrue(A) or assertFalse(A) instead")


@core.flake8ext
def assert_equal(logical_line, noqa):
    """Enforce use of assertEqual/assertNotEqual.

    Prevent use of assertTrue(A ==|!= B) and assertFalse(A ==|!= B)

    A102
    """
    _re = re.compile(r'assert(True|False)\(.+\s+(==|!=)\s+.+\)$')

    if noqa:
        return

    if _re.search(logical_line):
        yield (0, "A102: assertTrue(A ==|!= B) or assertFalse(A ==|!= B) "
               "must not be used. Use assertEqual(A, B) or "
               "assertNotEqual(A, B) instead")


@core.flake8ext
def assert_in(logical_line, noqa):
    """Enforce use of assertIn/assertNotIn.

    Prevent use of assertTrue(A in|not in B), assertFalse(A in|not in B),
    assertTrue(A in|not in B, message) and assertFalse(A in|not in B, message)

    A103
    """
    _re_no_spaces = re.compile(
        r"assert(True|False)\("
        r"(\w|[][.'\"])+( not)? in (\w|[][.'\",])+(, .*)?\)")
    _re_spaces = re.compile(
        r"assert(True|False)"
        r"\((\w|[][.'\"])+( not)? in [\[|'|\"](\w|[][.'\", ])+"
        r"[\[|'|\"](, .*)?\)")

    if noqa:
        return

    if _re_no_spaces.search(logical_line) or _re_spaces.search(logical_line):
        yield (6, "A103: assertTrue(A in|not in B) and "
               "assertFalse(A in|not in B) must not be used. Use "
               "assertIn(A, B) or assertNotIn(A, B) instead.")


@core.flake8ext
def assert_is(logical_line, noqa):
    """Enforce use of assertIs/assertIsNot.

    Prevent use of assertTrue(A is|is not B) and assertFalse(A is|is not B)

    A104
    """
    _re = re.compile(r'assert(True|False)\(.+\s+is\s+(not\s+)?.+\)$')

    if noqa:
        return

    if _re.search(logical_line):
        yield (0, "A104: assertTrue(A is|is not B) or "
               "assertFalse(A is|is not B) must not be used. Use "
               "assertIs(A, B) or assertIsNot(A, B) instead")


@core.flake8ext
def assert_is_none(logical_line, noqa):
    """Enforce use of assertIsNone/assertIsNotNone.

    Prevent use of assertIsNot(A, None) or assertIsNot(None, A)

    A105
    """
    _re_start_1 = re.compile(r'assertIs(Not)?\(None,')
    _re_end_1 = re.compile(r'assertIs(Not)?\(.*,\s+None\)$')
    _re_start_2 = re.compile(r'assertEqual\(None,')
    _re_end_2 = re.compile(r'assertEqual\(.*,\s+None\)$')

    if noqa:
        return

    if (_re_start_1.search(logical_line) or _re_end_1.search(logical_line) or
            _re_start_2.search(logical_line) or
            _re_end_2.search(logical_line)):
        yield (0, "A105: assertIsNot(A, None), assertIsNot(None, A), "
               "assertEqual(A, None) or assertNotEqual(A, None) must "
               "not be used. Use assertIsNone(A) or assertIsNotNone(A) "
               "instead.")


@core.flake8ext
def assert_is_instance(logical_line, noqa):
    """Enforce use of assertIsInstance/assertNotIsInstance.

    Prevent use of assertTrue(isinstance(A, B)) or
    assertFalse(isinstance(A, B)).

    A106
    """
    _re = re.compile(r'(.)*assert(True|False)\(isinstance\(')

    if noqa:
        return

    if _re.match(logical_line):
        yield (0, "A106: assertTrue(isinstance(A, B)) or "
               "assertFalse(isinstance(a, b) must not be used. Use "
               "assertIsInstance(A, B) or assertNotIsInstance(A, B) instead.")
