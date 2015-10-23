__author__ = 'yellow'
__license__ = 'GPLv2'
__date__ = '2014'

from PyQt4.QtCore import QSize, pyqtSignal, Qt
from PyQt4.QtGui import QComboBox
from .base_maps_model import BaseMapsModel


class DropdownBaseMapSelector(QComboBox):

    basemap_selected = pyqtSignal(object)

    def __init__(self, base_maps_list, parent=None, thumb_size=64):
        QComboBox.__init__(self, parent)
        self._parent = parent
        self.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.set_thumb_size(thumb_size)
        self.currentIndexChanged[int].connect(self.on_index_changed)

    def set_base_maps_list(self, base_maps_list):
        if not base_maps_list:
            return
        self._model = BaseMapsModel(base_maps_list, self._parent)
        self.setModel(self._model)

    def set_thumb_size(self, size):
        self.setIconSize(QSize(size, size))
        self.setMinimumHeight(size)
        self.setMaximumHeight(size)

    def set_current_basemap(self, basemap_id):
        index = self.findData(basemap_id)
        if index >= 0:
            self.setCurrentIndex(index)
        else:
            raise IndexError('Basemap with id "%s" not found!' % str(basemap_id))

    def current_basemap(self):
        return self.itemData(self.currentIndex())

    #def resizeEvent(self, e):
    #    self.setIconSize(QSize(self.size().width()/2, self.size().height()-10))
    #    QComboBox.resizeEvent(self, e)

    def on_index_changed(self, ind):
        self.basemap_selected.emit(self.itemData(ind))
