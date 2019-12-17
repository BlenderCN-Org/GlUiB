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


from .GlUiCore import GlObject


class GlWidget(GlObject):
    def __init__(self):
        self._x = 0
        self._y = 0
        self._width = 300
        self._height = 100