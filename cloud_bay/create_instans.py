#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2017, Vitaliy Zhydchenko <>
#
# This file is part of AWS Spot Daemon
#
# AWS Spot Daemon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AWS Spot Daemon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AWS Spot Daemon.  If not, see <http://www.gnu.org/licenses/>.

########################################################

import sys

sys.path.append("%s/aws-daemon" % (sys.path[0]))

print(
    sys.path
)
# sys.path.append("%s/AWS_create_ins_daemon" % (sys.path[0]))
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import aws-daemon

# print aws.create_instans()

# sys.exit(0)
