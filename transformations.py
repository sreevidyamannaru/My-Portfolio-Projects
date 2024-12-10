
def transform_data(df):
    transformed_df = df.withColumnRenamed("old_column", "new_column")
    return transformed_df
            