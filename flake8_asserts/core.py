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

from flake8_asserts import __version__


def flake8ext(_func):
    """Decorate flake8_asserts functions"""
    _func.name = r'flake8_asserts'
    _func.version = __version__
    _func.code = _func.__name__.upper()

    return _func