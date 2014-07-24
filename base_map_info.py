__author__ = 'yellow'
__license__ = 'GPLv2'
__date__ = '2014'


class BaseMapInfo():

    def __init__(self, id=None, label=None, thumb_path=None, uri=None, linked_obj=None):
        self.id = id
        self.label = label
        self.thumb_path = thumb_path
        self.uri = uri
        self.linked_obj = linked_obj
