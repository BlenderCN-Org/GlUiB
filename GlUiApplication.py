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


import bpy

from . import GlUiWidgets

from .gl import GPU_Quad


class GlWindow(GlUiWidgets.GlWidget):

    def __init__(self, context):
        super(GlWindow, self).__init__()
        self._childrens = []
        self._context = context
        self._close = False

        self._header = GPU_Quad(self)
        self._header_height = 30
        self._window_body = GPU_Quad(self)

    def add_widget(self, widget):
        self._childrens.append(widget)

    def draw(self):
        panel_color = bpy.context.preferences.themes['Default'].view_3d.space.panelcolors
        self._header.vertices = (
            (self.x, self.y+self.height-self._header_height),
            (self.x + self.width, self.y+self.height-self._header_height),
            (self.x, self.y+self.height),
            (self.x + self.width, self.y+self.height)
            )
        self._header.color = panel_color.header

        self._window_body.vertices = (
            (self.x, self.y),
            (self.x+self.width, self.y),
            (self.x, self.y+self.height-self._header_height),
            (self.x+self.width, self.y+self.height-self._header_height)
            )
        self._window_body.color = panel_color.back

        self._header.draw()
        self._window_body.draw()

    @property
    def is_closed(self):
        return self._close

    def close(self):
        self._close = True