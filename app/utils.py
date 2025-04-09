def clean_data(df):
    df = df.dropna(axis = 1, thresh = len(df)*0.6)
    return df


def generate_summary(df):
    return df.describe(include = 'all').to_string()