# -*- coding: utf-8 -*-
import logging

from .controllers import controllers
from .layouts import MainWindow
from .logger import ABHandler

logger = logging.getLogger('ab_logs')
log = ABHandler.setup_with_logger(logger, __name__)


class Application(object):
    def __init__(self):
        self.main_window = MainWindow(self)

        # Provide the log file path, so it is available for the Activity-Browser
        # debug window/text box
        log.info("The Activity-Browser log file can be found at {}".format(log.log_file_path()))
        # Instantiate all the controllers.
        # -> Ensure all controller instances have access to the MainWindow
        # object, this propagates the 'AB' icon to all controller-handled
        # dialogs and wizards.
        for attr, controller in controllers.items():
            setattr(self, attr, controller(self.main_window))

    def show(self):
        self.main_window.showMaximized()

    def close(self):
        self.plugin_controller.close_plugins()
        self.main_window.close()

    def deleteLater(self):
        self.main_window.deleteLater()
