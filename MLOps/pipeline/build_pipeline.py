import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URI

# Step 1: Extract
def extract(filepath):
    print("Extracting data...")
    return pd.read_csv(filepath)

# Step 2: Transform
def transform(df):
    print("Transforming data...")
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Example cleaning:
    df.dropna(subset=['age'], inplace=True)
    df['age'] = df['age'].astype(int)

    # Example feature: high_screen_time flag
    if 'screen_time' in df.columns:
        df['high_screen_time'] = df['screen_time'] > 6

    return df
# Step 3: Load
def load(df, table_name='digital_diet_data'):
    print("Loading data...")
    engine = create_engine(DATABASE_URI)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data loaded to table: {table_name}")

# Run the pipeline
if __name__ == "__main__":
    df = extract("../digital_diet_mental_health.csv")
    df_transformed = transform(df)
    load(df_transformed)