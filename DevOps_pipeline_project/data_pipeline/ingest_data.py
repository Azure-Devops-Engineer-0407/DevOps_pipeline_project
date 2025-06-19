import pandas as pd

def ingest_data():
    data = {
        'customer_id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'signup_date': ['2023-01-01', '2023-01-02', '2023-01-03']
    }
    df = pd.DataFrame(data)
    df.to_csv('raw_customers.csv', index=False)
    print("Data ingested and saved to raw_customers.csv")

if __name__ == "__main__":
    ingest_data()   
