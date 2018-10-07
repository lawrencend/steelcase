import pandas as pd
from pathlib import Path
from datetime import datetime


def add_test(test_df):

    with open(".steelcase_path", "r") as file:
        # Read the current path
        current_output_path = file.read()

    summary_path = Path(f'{current_output_path}/{datetime.now().date()}.csv')
    test_path = Path(f'{current_output_path}/{datetime.now()}.csv')

    test_df.to_csv(test_path)

    if summary_path.is_file():

        summary_df = pd.read_csv(summary_path)
        
        print(summary_df, test_df)

        summary_df = pd.concat([summary_df, test_df.tail(1)])

    else:
        summary_df = test_df

    summary_df.to_csv(summary_path, index=False)


if __name__ == '__main__':

    o = DataManagement()