import os;
import sys;

class ModelEvaluationException(Exception):
    def __init__(self, error:Exception, sys:sys):
        super().__init__(error)
        # exc_tb holds the execution traceback
        _, _, exc_tb = sys.exc_info();

        # loop to the actual line
        while exc_tb.tb_next:
            exc_tb = exc_tb.tb_next;

        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        print(f"Model Evaluation Error: filename: {file_name}, line_number:{line_number}: {error}");