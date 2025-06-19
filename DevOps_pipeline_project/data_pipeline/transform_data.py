import pandas as pd

def transform():
    df = pd.read_csv('raw_customers.csv')
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    df['signup_year'] = df['signup_date'].dt.year
    df.to_csv('transformed_customers.csv', index=False)
    print("Data transformed and saved to transformed_customers.csv")
    # this is just commnet code which i have done on this project

if __name__ == "__main__":
    transform()
