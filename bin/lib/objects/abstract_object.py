# -*-coding:UTF-8 -*
"""
Base Class for AIL Objects
"""

##################################
# Import External packages
##################################
import os
import sys
from abc import ABC, abstractmethod

#from flask import url_for

sys.path.append(os.environ['AIL_BIN'])
##################################
# Import Project packages
##################################
from packages import Tag
from lib.Investigations import is_object_investigated, get_obj_investigations
from lib.Tracker import is_obj_tracked, get_obj_all_trackers

# # TODO: ADD CORRELATION ENGINE

class AbstractObject(ABC):
    """
    Abstract Object
    """

    # first seen last/seen ??
    # # TODO: - tags
    #         - handle + refactor coorelations
    #         - creates others objects

    def __init__(self, obj_type, id, subtype=None):
        """ Abstract for all the AIL object

        :param obj_type: object type (item, ...)
        :param id: Object ID
        """
        self.id = id
        self.type = obj_type
        self.subtype = subtype

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_subtype(self, r_str=False):
        if not self.subtype:
            if r_str:
                return ''
        return self.subtype

    def get_default_meta(self, tags=False):
        dict_meta = {'id': self.get_id(),
                     'type': self.get_type(),
                     'subtype': self.get_subtype()}
        if tags:
            dict_meta['tags'] = self.get_tags()
        return dict_meta

    ## Tags ##
    def get_tags(self, r_set=False):
        tags = Tag.get_obj_tag(self.id)
        if r_set:
            tags = set(tags)
        return tags

    ## ADD TAGS ????
    #def add_tags(self):

    #- Tags -#

    ## Investigations ##
    # # TODO: unregister =====

    def is_investigated(self):
        if not self.subtype:
            is_investigated = is_object_investigated(self.id, self.type)
        else:
            is_investigated = is_object_investigated(self.id, self.type, self.subtype)
        return is_investigated

    def get_investigations(self):
        if not self.subtype:
            investigations = get_obj_investigations(self.id, self.type)
        else:
            investigations = get_obj_investigations(self.id, self.type, self.subtype)
        return investigations
    #- Investigations -#

    ## Trackers ##

    def is_tracked(self):
        return is_obj_tracked(self.type, self.subtype, self.id)

    def get_trackers(self):
        return get_obj_all_trackers(self.type, self.subtype, self.id)

    #- Investigations -#

    def _delete(self):
        # DELETE TAGS
        Tag.delete_obj_all_tags(self.id, self.type)
        # # TODO: remove from investigations

    @abstractmethod
    def delete(self):
        """
        Delete Object: used for the Data Retention
        """
        pass

    # @abstractmethod
    # def get_meta(self):
    #     """
    #     get Object metadata
    #     """
    #     pass

    @abstractmethod
    def get_svg_icon(self):
        """
        Get object svg icon
        """
        pass

    @abstractmethod
    def get_link(self, flask_context=False):
        pass

    # # TODO:
    # @abstractmethod
    # def get_correlations(self, message):
    #     """
    #     Get object correlations
    #     """
    #     pass


    # # TODO: get favicon
    # # TODO: get url
    # # TODO: get metadata
