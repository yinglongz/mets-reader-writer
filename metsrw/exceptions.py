# -*- coding: utf-8 -*-
"""
Exceptions for metsrw.

All exceptions generated by this library will descend from MetsError.
"""


class MetsError(Exception):
    """ Base Exception for this module. """


class ParseError(MetsError):
    """ Error parsing a METS file. """


class SerializeError(MetsError):
    """ Error serializing a METS file. """
