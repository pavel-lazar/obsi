#!/usr/bin/env python
#
# Copyright (c) 2015 Pavel Lazar pavel.lazar (at) gmail.com
#
# The Software is provided WITHOUT ANY WARRANTY, EXPRESS OR IMPLIED.
#####################################################################

"""
A configuration and definitions file used by the EE runner server and client
"""
from click_control_client import ClickControlClient

ENGINES = {'click': (ClickControlClient, {})}


class RestServer:
    PORT = 9002
    DEBUG = True

    class Endpoints:
        ENGINES = '/control/engines'
        CONNECT = '/control/connect'
        CLOSE = '/control/close'
        ENGINE_VERSION = '/control/engine_version'
        LOADED_PACKAGES = '/control/loaded_packages'
        SUPPORTED_ELEMENTS = '/control/supported_elements'
        CONFIG = '/control/config'
        LIST_ELEMENTS = '/control/elements'
        SEQUENCE = '/control/elements/sequence'
        IS_READABLE = '/control/elements/(.*)/(.*)/is_read'
        IS_WRITEABLE = '/control/elements/(.*)/(.*)/is_write'
        HANDLER_PATTERN = '/control/elements/{element}/{handler}'
        HANDLER = HANDLER_PATTERN.format(element='(.*)', handler='(.*)')
        LIST_HANDLERS = '/control/elements/(.*)'
