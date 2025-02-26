import numpy as np
import pandas as pd


def clean_data(dir):
    """_summary_

    Args:
        dir (_csv_): the path of a csv data set you would like to be cleaned

    Returns:
        _pandas.df_: returns the cleaned dataset in a pandas dataframe
    """ 
    # Read in data set
    df = pd.read_csv(dir)

    # Assign valid parameter ranges based on csv description to each column
    valid_school = ['GP', 'MS']
    valid_sex = ['F', 'M']
    valid_address = ['U', 'R']
    valid_famsize = ['GT3', 'LE3']
    valid_pstatus = ['T', 'A']
    valid_reason = ['home', 'reputation', 'course', 'other']
    valid_yes_no = ['yes', 'no']
    valid_4scale = np.arange(5)
    valid_5scale = np.arange(6)
    valid_grade = np.arange(21)

    minpass_grade = 12

    # Ensure columns are properly formatted

    upper_columns = ['school', 'sex', 'address', 'famsize', 'Pstatus']
    lower_columns = ['reason', 'guardian', 'schoolsup', 'famsup', 'paid',
                    'activities', 'nursery', 'higher', 'internet', 'romantic']

    for col in upper_columns:
        df[col] = df[col].str.upper()

    for col in lower_columns:
        df[col] = df[col].str.lower()


    # Remove null and invalid data
    df = df[df['school'].isin(valid_school)]
    df = df[df['sex'].isin(valid_sex)]
    df = df[df['address'].isin(valid_address)]
    df = df[df['famsize'].isin(valid_famsize)]
    df = df[df['Pstatus'].isin(valid_pstatus)]
    df = df[df['reason'].isin(valid_reason)]
    df = df[df['Grade'].isin(valid_grade)]

    scale4 = ['Medu', 'Fedu', 'traveltime', 'studytime']
    scale5 = ['famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health']
    yes_no = ['schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher',
            'internet', 'romantic']

    for col in scale4:
        df = df[df[col].isin(valid_4scale)]

    for col in scale5:
        df = df[df[col].isin(valid_5scale)]

    for col in yes_no:
        df = df[df[col].isin(valid_yes_no)]

    # Create a pass/fail column utilsing Grades
    df['result'] = np.where(df['Grade'] >= minpass_grade, 'pass', 'fail')

    # Save dataset
    #df.to_csv('data/formatted_data.csv')
    return df
