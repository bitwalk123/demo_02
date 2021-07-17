import pandas as pd
import platform
import subprocess


# -----------------------------------------------------------------------------
#  get_app_launcher
#  get name of application launcher
#
#  argument
#    (none)
#
#  return
#    name of application launcher - str
# -----------------------------------------------------------------------------
def get_app_launcher() -> str:
    if platform.system() == 'Linux':
        return 'xdg-open'
    else:
        # Windows Explorer can cover all cases to start application with file
        return 'explorer'


# -----------------------------------------------------------------------------
#  open_file_with_default_app
#  open file with default application
#
#  note
#    This method is tested on Linux (RHEL) and Windows.
#
#  argument
#    path: str - path of file to open
#
#  return
#    (none)
# -----------------------------------------------------------------------------
def open_file_with_default_app(path: str):
    app_open: str = get_app_launcher()

    # open file with default application
    subprocess.Popen([app_open, path])


# -----------------------------------------------------------------------------
#  read_csv
#  read CSV file
#
#  argument
#    name_file: str - filename to read
#
#  return
#    pandas dataframe
# -----------------------------------------------------------------------------
def read_csv(name_file: str) -> pd.DataFrame:
    return pd.read_csv(name_file)
