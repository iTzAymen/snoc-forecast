import pandas as pd
from pmdarima import auto_arima

data = {
    'transactions': [
        ["2023-01-01", 100],
        ["2023-01-02", 100],
        ["2023-01-03", 100],
        ["2023-01-04", 100],
        ["2023-01-05", 100],
        ["2023-01-06", 100]
    ],
    'start_date': "2023-01-01",
    'end_date': "2023-01-06",
    'predictions': 2
}

START_DATE = data['start_date']
END_DATE = data['end_date']
DATE_RANGE = pd.date_range(START_DATE, END_DATE)

transactions = pd.DataFrame(data['transactions'], columns=['date', 'transactions'])
transactions = pd.DataFrame(data['transactions'], columns=['date', 'transactions'])
transactions['date'] = pd.to_datetime(transactions['date'])
transactions = transactions[transactions['date'] >= START_DATE][transactions['date'] <= END_DATE]
transactions.set_index('date', inplace=True)

empty_rows = pd.DataFrame(0,index=DATE_RANGE, columns=['transactions'])
empty_rows.loc[transactions.index] = transactions

model = auto_arima(y=transactions, m=7)
preds = pd.Series(model.predict(n_periods=data['predictions']))

print(preds)