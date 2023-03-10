import pandas as pd
import numpy as np


def drop_loanamt_if_null(df):
    """ param @ df
        drops LoanAmount column is NaN
         return df """
    df.dropna(subset=['LoanAmount'], inplace=True)
    return df


def impute_values(df):
    """ param @ df
        impute missing values in the following:
        fill Loan_amount_Term with median of training data,
        fill Married, Gender, Self-Employed with the mode of training data,
        fill children with 0
        return df
        """
    median_term = df.Loan_Amount_Term.median()
    df.Loan_Amount_Term = df['Loan_Amount_Term'].fillna(median_term)

    mode_married = df.Married.mode()[0]
    df.Married = df.Married.fillna(mode_married)

    mode_gender = df.Gender.mode()[0] 
    df.Gender = df.Gender.fillna(mode_gender)

    df.Dependents = df.Dependents.fillna('0')

    mode_employed = df.Self_Employed.mode()[0] 
    df.Self_Employed = df.Self_Employed.fillna(mode_employed)
    df = df.dropna(subset=['Credit_History'])
    return df



def label_encoding(df: pd.DataFrame):
    """param @ df
        label encodes 'Married', 'Gender','Self_Employed', 'Credit_History', 'Loan_Status'
        drops original categorical columns
        returns modified df    """
    
    # select columns to encode
    from sklearn.preprocessing import LabelEncoder
    cols_to_encode = df['Married', 'Gender','Self_Employed', 'Credit_History', 'Loan_Status']

    # apply LabelEncoder to selected columns
    le = LabelEncoder()
    for col in cols_to_encode:
        df[col] = le.fit_transform(df[col])

    return df




def reverse_label_encoding(column):
    """ param @ column of df
        returns a label encoded version of the column, with the 1 and 0 values reversed """
    
    # Create an instance of the LabelEncoder
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()

    encoded_column = le.fit_transform(column)
    encoded_column = 1 - encoded_column

    return encoded_column



def one_hot_encoding(df: pd.DataFrame):
    """ param @ df
        one-hot encodes 'Property_Area', 'Dependents'
        drops original categorical columns
        returns modified df    """

    from sklearn.preprocessing import OneHotEncoder

    # One-hot encode the 'Property_Area' and 'Dependents' columns
    df_encoded = pd.get_dummies(df [['Property_Area', 'Dependents']] )

    # Concatenate the one-hot encoded columns with the original dataframe
    df = pd.concat( [df, df_encoded], axis=1)

    # Drop the original 'Property_Area' and 'Dependents' columns
    df.drop(columns = ['Property_Area', 'Dependents'], inplace=True)

    return df



def total_logged_income(df: pd.DataFrame):
    """ take a dataframe and return the logged total income as a new column named 'TotalIncome_log' """

    # First, need to change all 0s to 0.1 to do log transform
    df['ApplicantIncome'] = df['ApplicantIncome'].apply(lambda x: 0.1 if x == 0 else x)
    df['CoapplicantIncome'] = df['CoapplicantIncome'].apply(lambda x: 0.1 if x == 0 else x)

    # Combine both incomes as total income 
    df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']

    # log transform total_income
    df['TotalIncome_log'] = np.log(df['TotalIncome'])

    return df



def select_Xy_cols(df: pd.DataFrame):
    """ param @ df
        select columns to include in model
        select y column
        return features df and y    """
    
    cols_to_inc = ('Gender', 'Married', 'Education', 'Self_Employed', 'LoanAmount', \
                'Loan_Amount_Term', 'Credit_History', 'Property_Area_Rural', \
                'Property_Area_Semiurban', 'Property_Area_Urban', 'Dependents_0', \
                'Dependents_1', 'Dependents_2', 'Dependents_3+', 'TotalIncome_log')
        
    X = df[list(cols_to_inc)]
    y = df['Loan_Status']
    
    return X, y

