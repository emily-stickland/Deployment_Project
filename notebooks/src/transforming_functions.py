def total_logged_income(column1, column2):
    """ take 2 columns as imput and return the sum of the logged values  """

    # First, need to change all 0s to 0.1 to do log transform
    column1 = column1.apply(lambda x: 0.1 if x == 0 else x)
    column2 = column2.apply(lambda x: 0.1 if x == 0 else x)

    # Combine both incomes as total income 
    total_income = column1 + column2

    # log transform total_income
    total_income_log = np.log(total_income)

    return total_income_log