# coding=utf-8
__author__ = 'yellow'
__license__ = 'GPLv2'
__date__ = '2014'

from sys import argv
from PyQt4.QtGui import QApplication, QListWidget
from PyQt4.QtCore import QSize

from base_map_info import BaseMapInfo
from thumbnails import Thumbnails, ThumbnailsPaths
from dropdown_basemap_selector import DropdownBaseMapSelector
from vlist_basemap_selector import VListBaseMapSelector


def main(args):
    app = QApplication(args)

    #create and show debug console
    console = QListWidget()
    console.setWindowTitle('Console')
    console.show()
    #slot for pass 'named' messages
    print_info = lambda control_name: lambda message: console.addItem('%s: %s' % (control_name, message))

    #create list of base maps
    base_maps = [
        BaseMapInfo(id='osm',       label=u'Карта улиц',    thumb_path=Thumbnails.Paths.OSM),
        BaseMapInfo(id='satellite', label=u'Спутник',       thumb_path=Thumbnails.Paths.Imagery),
        BaseMapInfo(id='hybrid',    label=u'Гибрид',        thumb_path=ThumbnailsPaths.Hybrid)
    ]

    #create and show vertical list
    vlist_control = VListBaseMapSelector(base_maps)
    vlist_control.basemap_selected.connect(print_info('Vertical List'))     # connect to change signal
    vlist_control.set_current_basemap('satellite')                          # select map
    vlist_control.set_thumb_size(128)                                       # set size of icons

    vlist_control.resize(QSize(200, 500))
    vlist_control.setWindowTitle('Vertical list selector')
    vlist_control.show()

    #create and show dropdown list
    ddlist_control = DropdownBaseMapSelector(base_maps)
    ddlist_control.basemap_selected.connect(print_info('DropDown List'))    # connect to change signal
    ddlist_control.set_current_basemap('hybrid')                            # select map

    ddlist_control.setWindowTitle('Drop down list selector')
    ddlist_control.show()

    return app.exec_()


if __name__ == '__main__':
    main(argv)