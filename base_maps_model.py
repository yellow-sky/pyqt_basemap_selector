__author__ = 'yellow'
__license__ = 'GPLv2'
__date__ = '2014'

from PyQt4.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt4.QtCore import Qt


class BaseMapsModel(QStandardItemModel):

    def __init__(self, base_maps_list, parent=None):
        QStandardItemModel.__init__(self, parent)
        self._base_map_list = None
        self.set_maps_list(base_maps_list)

    def set_maps_list(self, base_maps_list):
        self._base_map_list = base_maps_list
        self._fill_model()

    def _fill_model(self):
        self.clear()
        root_item = self.invisibleRootItem()
        for base_map in self._base_map_list:
            item = QStandardItem()
            item.setData(base_map.label, Qt.DisplayRole)
            item.setData(base_map.id, Qt.UserRole)
            item.setData(QIcon(base_map.thumb_path), Qt.DecorationRole)
            root_item.appendRow(item)
