import pandas as pd
from pathlib import Path
from datetime import datetime
import os


def add_test(test_df):

    with open(".steelcase_path", "r") as file:
        # Read the current path
        current_output_path = file.read()

    day_summary_path = Path(str(current_output_path) + '/' + str(datetime.now().date()))
    
    if os.path.isdir(day_summary_path) == False:
         os.mkdir(day_summary_path)   
    else:
        pass
    
    summary_path = Path(str(day_summary_path) + r'/summary.csv')
    test_path = Path(str(current_output_path) + '/' + str(datetime.now()) + '.csv')

    test_df.to_csv(test_path, index=False)

    if summary_path.is_file():

        summary_df = pd.read_csv(summary_path)

        summary_df = pd.concat([summary_df, test_df.tail(1)])

    else:
        summary_df = test_df.tail(1)

    summary_df.to_csv(summary_path, index=False)


if __name__ == '__main__':

    o = DataManagement()