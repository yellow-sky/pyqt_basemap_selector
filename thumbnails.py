__author__ = 'yellow'
__license__ = 'GPLv2'
__date__ = '2014'

from os import path
import sys
#from PyQt4.QtGui import QIcon


_fs_encoding = sys.getfilesystemencoding()
_current_path = unicode(path.abspath(path.dirname(__file__)), _fs_encoding)
_thumbs_dir_path = path.join(_current_path, u'thumbs')


class ThumbnailsPaths():
    OSM = path.join(_thumbs_dir_path, 'osm.png')
    Imagery = path.join(_thumbs_dir_path, 'imagery.jpg')
    Hybrid = path.join(_thumbs_dir_path, 'imagery_with_labels.png')


# class ThumbnailsIcons():
#     OSM = QIcon(ThumbnailsPaths.OSM)
#     Imagery = QIcon(ThumbnailsPaths.Imagery)
#     Hybrid = QIcon(ThumbnailsPaths.Hybrid)


class Thumbnails():
    Paths = ThumbnailsPaths()
    # Icons = ThumbnailsIcons()