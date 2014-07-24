__author__ = 'yellow'
__license__ = 'GPLv2'
__date__ = '2014'

from PyQt4.QtCore import QSize, pyqtSignal, Qt
from PyQt4.QtGui import QListView
from base_maps_model import BaseMapsModel


class VListBaseMapSelector(QListView):

    basemap_selected = pyqtSignal(object)

    def __init__(self, base_maps_list, parent=None, thumb_size=64):
        QListView.__init__(self, parent)
        self._model = BaseMapsModel(base_maps_list, parent)
        self.setModel(self._model)

        self.setEditTriggers(QListView.NoEditTriggers)
        self.setViewMode(QListView.IconMode)
        self.setMovement(QListView.Static)
        self.setResizeMode(QListView.Adjust)
        #self.setFlow(QListView.TopToBottom)
        #self.setWrapping(True)
        #self.setSpacing(0)
        self.set_thumb_size(thumb_size)

    def set_thumb_size(self, size):
        self.setIconSize(QSize(size, size))

    def set_current_basemap(self, basemap_id):
        index = self._search_item(self.model(), basemap_id)
        if index:
            self.setCurrentIndex(index)
        else:
            raise IndexError('Basemap with id "%s" not found!' % str(basemap_id))

    def _search_item(self, model, user_data):
        root_item = model.invisibleRootItem()
        for i in range(model.rowCount(root_item.index())):
            if model.item(i, 0).data(Qt.UserRole).toPyObject() == user_data:
                return model.item(i, 0).index()


    def resizeEvent(self, e):
        new_grid_size = QSize(self.maximumViewportSize().width(), self.iconSize().height()+self.fontMetrics().height())
        if self.verticalScrollBar().isVisible():
            new_grid_size.setWidth(new_grid_size.width() - self.verticalScrollBar().width())
        self.setGridSize(new_grid_size)
        return QListView.resizeEvent(self, e)


    def currentChanged(self, curr, prev):
        self.basemap_selected.emit(curr.data(Qt.UserRole).toPyObject())
        return QListView.currentChanged(self, curr, prev)






