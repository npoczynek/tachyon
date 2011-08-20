# Tachyon - Fast Multi-Threaded Web Discovery Tool
# Copyright (c) 2011 Gabriel Tremblay - initnull hat gmail.com
#
# GNU General Public Licence (GPL)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA
#

from core import conf, database, utils

def add_generated_path(char):
    """ Add path to database """
    current_template = dict(conf.path_template)
    current_template['description'] = 'Computer generated path'
    current_template['url'] = '/' + chr(char)
    if current_template not in database.paths:
        if conf.debug:
            utils.output_debug(' - PathGenerator Plugin Generated: ' + str(current_template))
        database.paths.append(current_template)


def execute():
    """ Generate common simple paths (a-z, 0-9) """
    added = 0
    for char in range(ord('a'), ord('z')):
        add_generated_path(char)
        added += 1

    for char in range(ord('0'), ord('9')):
        add_generated_path(char)
        added += 1

    utils.output_info(' - PathGenerator Plugin: added ' + str(added) + ' computer generated path.')

