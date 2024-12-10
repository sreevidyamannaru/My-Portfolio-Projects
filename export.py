
def export_data(df, output_path):
    df.write.csv(output_path, mode="overwrite", header=True)
            