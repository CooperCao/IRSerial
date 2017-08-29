#!/usr/bin/env python
#
# This is a wrapper module for different platform implementations
#
# This file is part of IRSerial. https://github.com/pyserial/pyserial
# (C) 2017-2017 Cooper Cao <caopeng89@foxmail.com>
#
# SPDX-License-Identifier:    BSD-3-Clause

import sys
import importlib

from irserial.irserial import IRserial

__version__ = '0.1'

VERSION = __version__
