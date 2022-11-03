import sys 

def error_message_detail(error_message, error_detail):
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    full_error_message = "Error occured in python script name [{0}], line number [{1}], error message [{2}]".format(
        file_name, exc_tb.tb_lineno, error_message)

    return full_error_message

class SensorException(Exception):
    def __init__(self, error_message, error_detail):
        """_summary_

        Args:
            error_message (string): Error message generated
            error_detail (sys): sys variable containing 
        """

        self.error_message = error_message_detail(
            error_message, error_detail
        )

    def __str__(self):
        return self.error_message