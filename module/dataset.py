from module.config import *

# Function that drops duplicate rows and replaces any NA-values with the mean of the column if the column contains numerical data
def basic_cleaning(dataset):
    dataset_no_dups = dataset.drop_duplicates()
    numerical_cols = dataset_no_dups.select_dtypes(include=['number'])
    dataset_no_dups.loc[:, numerical_cols.columns] = numerical_cols.fillna(numerical_cols.mean())
    return dataset_no_dups

# Find columns in train dataset where all rows contain the same value (excluding the dropout columnn) and then drops them from the train and predict sets
def remove_single_value_columns(dataset_train, dataset_pred):
    single_value_columns = [col for col in dataset_train.columns if dataset_train[col].nunique() == 1]
    dataset_train = dataset_train.drop(columns=single_value_columns, errors='ignore')
    dataset_pred = dataset_pred.drop(columns=single_value_columns, errors='ignore')
    return dataset_train, dataset_pred

# Function that searches for and prints duplicate students
def show_duplicates_student (dataset_train, dataset_pred):
    duplicates_train = dataset_train[dataset_train.duplicated(studentnumber_column, keep=False)]
    print('Students with duplicates in train dataset:')
    print(duplicates_train)
    duplicates_pred = dataset_pred[dataset_pred.duplicated(studentnumber_column, keep=False)]
    print('Students with duplicates in predict dataset:')
    print(duplicates_pred)
    return


