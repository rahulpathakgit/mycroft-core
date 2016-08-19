# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


import os
from os.path import join, expanduser, isdir
from shutil import copyfile

__author__ = 'jdorleans'


class FileSystemAccess(object):
    """
    A class for providing access to the mycroft FS sandbox. Intended to be
    attached to skills
    at initialization time to provide a skill-specific namespace.
    """
    def __init__(self, path):
        self.path = self.__init_path(path)

    @staticmethod
    def __init_path(path):
        if not isinstance(path, str) or len(path) == 0:
            raise ValueError("path must be initialized as a non empty string")
        path = join(expanduser('~'), '.mycroft', path)

        if not isdir(path):
            os.makedirs(path)
        return path

    def open(self, filename, mode):
        """
        Get a handle to a file (with the provided mode) within the
        skill-specific namespace.

        :param filename: a str representing a path relative to the namespace.
            subdirs not currently supported.

        :param mode: a file handle mode

        :return: an open file handle.
        """
        file_path = join(self.path, filename)
        return open(file_path, mode)

    def exists(self, filename):
        return os.path.exists(join(self.path, filename))

    def copy(self, filename, source_path, dest_path):
        try:
            copyfile(self.source_path + '/' + self.file_source, self.dest_path + '/' + self.file_dest)
            print self.name + " Success -- file copy from: " + self.file_source + " to: " + self.file_dest

        except:
            print self.name + " Failed -- file copy from: " + self.file_source + " to: " + self.file_dest
        return 1
