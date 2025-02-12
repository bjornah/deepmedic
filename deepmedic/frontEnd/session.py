# Copyright (c) 2016, Konstantinos Kamnitsas
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the BSD license. See the accompanying LICENSE file
# or read the terms at https://opensource.org/licenses/BSD-3-Clause.

from __future__ import absolute_import, print_function, division

from deepmedic.logging import loggers
import os

class Session(object):
    
    def __init__(self, cfg):
        
        self._cfg = cfg
        self._session_name = self._make_session_name()
        self._main_out_folder_abs = None # Filled by make_output_folders(self)
        self._out_folder_logs = None
        self._log = None
        
        
    ######## SETTING UP ##########
        
    def _make_session_name(self):
        session_name = self._cfg[self._cfg.SESSION_NAME] if self._cfg[self._cfg.SESSION_NAME] is not None else "Session"
        return session_name
    
    # Override
    def make_output_folders(self):
        # Overrides must set: self._main_out_folder_abs
        raise NotImplementedError("Not implemented virtual function.")
    
    # Call only after calling make_output_folders()
    def setup_logger(self):
        log_filepath = os.path.join(self._out_folder_logs,self._session_name + ".txt")
        # Create logger.
        self._log = loggers.Logger(log_filepath)
    
    def get_logger(self):
        return self._log
    
    def override_file_cfg_with_cmd_line_cfg(self, args):
        self._cfg.override_file_cfg_with_cmd_line_cfg( self._log, args )
        
    def compile_session_params_from_cfg(self, *args):
        raise NotImplementedError("Not implemented virtual function.")
    
    
    ########### API ###########
    
    def get_abs_path_to_cfg(self):
        return self._cfg.get_abs_path_to_cfg()
    
    def run_session(self, *args):
        raise NotImplementedError("Not implemented virtual function.")

