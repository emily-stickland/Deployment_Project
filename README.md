# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
-Implement cleaning, EDA and modeling processes learnt in the mid-term project by myself.
-Test models with different parameters and different pre-processing (eg. scaled or unscaled), attempt to make pre-processing steps modular for use in a pipeline.

## Hypothesis
- Income, loan amount and credit history would be greatest predictors for approval.

## EDA 
While doing EDA I discovered: 
- Lots of co-applicants had zero income.
- Most applicants were mail. 
- Income was not normally distributed. 
- Most applicants were college graduates. 
- Income and loan amount countained outliers. 
- Most variables were categorical. 


## Process
- I did EDA and cleaning iteratively. First dealt with Nans, checked for duplicates, dropped Loan_ID column, imputed averages for missing values, label and one hot encoded, dropped outliers, took log of total income, decided not to take log of loan amount.
- Built various models including logistic regression, XGBoost, Random Forrest, Naive Bayes. Explored whether scaling affected the results for any of these which it did not. 
- Tried to search for best paramators for all models simultaneously but it took too long. 
- Grid Searched to tune parametors on Random Forrest and XGBoost.
- Attempted to redo cleaning steps in pipeline using imported functions from an externial .py file with 50% success. 
- Built flask API. 

## Challanges 
- Getting pipeline to work. 
- Time. 
- Following LHL instructions process (you will see that I have separate notebooks for cleaning, EDA and Pipelines which I then tried to shoehorn into the instructions notebook with limited success)

## Future Goals
-Explore tuning paramators to see if they make a difference to the individual models or if the models do this automatically (tuning these didnt seem to impact model results)
- Explore why one hot encoding didn't work in my pipeline (see pipeline notebook)
- Publish on AWS (AWS instance was not working)