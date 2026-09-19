import joblib
import pandas as pd

# Load trained model
model = joblib.load("insightpilot_revenue_model.pkl")


def predict_next_month_revenue(time_index, month_number, previous_month_revenue):
    input_data = pd.DataFrame({
        "Time_Index": [time_index],
        "Month_Number": [month_number],
        "Previous_Month_Revenue": [previous_month_revenue]
    })

    prediction = model.predict(input_data)[0]

    return round(prediction, 2)