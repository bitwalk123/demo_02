import pandas as pd

# local python file
import demo_common as cm


class FileParser:
    filename: str = None
    df: pd.DataFrame = None

    def __init__(self, filename: str):
        self.filename = filename
        self.parser()

    # -----------------------------------------------------------------------------
    #  get_data
    #  get contents of file
    #
    #  argument
    #    (none)
    #
    #  return
    #    pd.DataFrame - contents of file
    # -----------------------------------------------------------------------------
    def get_data(self) -> pd.DataFrame:
        return self.df

    # -----------------------------------------------------------------------------
    #  get_filename
    #  get filename of file
    #
    #  argument
    #    (none)
    #
    #  return
    #    str - filename of file
    # -----------------------------------------------------------------------------
    def get_filename(self) -> str:
        return self.filename

    # -----------------------------------------------------------------------------
    #  parser
    #  file parser to convert dataframe used for this application
    #  [CAUTION]
    #  This is demonstration and the file is supposed to have simple CSV format.
    #
    #  argument
    #    (none)
    #
    #  return
    #    (none)
    # -----------------------------------------------------------------------------
    def parser(self):
        # This is demonstration,
        # using simple CSV file reader
        self.df = cm.read_csv(self.filename)
