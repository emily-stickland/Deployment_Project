def drop_if_null_col(df, column):
    """ param @ df
        drops LoanAmount column is NaN
         return df """
    df.dropna(subset=[column], inplace=True)
    return df


def impute_values_col(df, column):
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