# -*- coding:utf-8 -*-

# GlUiD module for Blender
# Copyright (C) 2018 Legigan Jeremy AKA Pistiwique
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# <pep8 compliant>


class GlCoordonates:
    @property
    def x(self):
        """
        Return the x coordonate.
        :return: int
        """
        return self._x

    def setX(self, x):
        """
        Set the x coordonate of the given x coordonate.
        :param x: int
        """
        self._x = max(0, x)

    @property
    def y(self):
        """
        Return the y coordonate.
        :return: int
        """
        return self._y

    def setY(self, y):
        """
        Set the y coordonate of the given y coordonate.
        :param y: int
        """
        self._y = max(0, y)


class GlSize:
    @property
    def height(self):
        """
        Return the height.
        :return: int
        """
        return self._height

    def setHeight(self, h):
        """
        Set the height to the given height.
        :param h: int
        """
        self._height = max(0, h)

    @property
    def width(self):
        """
        Return the width.
        :return: int
        """
        return self._width

    def setWidth(self, w):
        """
        Set the width of the given width.
        :param w: int
        """
        self._width = max(0, w)

    def resize(self, w, h):
        """
        Change the size with the given width and height.
        :param w: int
        :param h: int
        """
        self.setWidth(w)
        self.setHeight(h)

    def transpose(self):
        """
        Swap the width and the height values.
        """
        self._width, self._height = self._height, self._width


class GlObject(GlCoordonates, GlSize):

    def move(self, x, y):
        self.setX(x)
        self.setY(y)

    def setGeometry(self, x, y, w, h):
        """
        Set the coordonates with the given x and y coordonates.
        Set the size with the given width and height.
        :param x: int
        :param y: int
        :param w: int
        :param h: int
        """
        self.setX(x)
        self.setY(y)
        self.resize(w, h)