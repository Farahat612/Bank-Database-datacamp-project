# 1.Read in the "bank_marketing.csv" file as a pandas DataFrame:
import pandas as pd
data = pd.read_csv("bank_marketing.csv")



# 2.Split the data into three DataFrames based on the desired tables:
client = data[["client_id", "age", "job", "marital", "education", "credit_default", "housing", "loan"]]
campaign = data[["client_id", "campaign", "duration", "pdays", "previous", "poutcome", "y", "day", "month"]]
economics = data[["client_id", "emp_var_rate", "cons_price_idx", "euribor3m", "nr_employed"]]



# 3.Rename the columns in each DataFrame:
client.rename(columns={"client_id": "id"}, inplace=True)
campaign.rename(columns={"duration": "contact_duration", "previous": "previous_campaign_contacts", "y": "campaign_outcome", "poutcome": "previous_outcome", "campaign": "number_contacts"}, inplace=True)
economics.rename(columns={"euribor3m": "euribor_three_months", "nr_employed": "number_employed"}, inplace=True)



# 4.Clean the "education" column:
import numpy as np
client["education"].replace(".", "_", inplace=True)
client["education"].replace("unknown", np.nan, inplace=True)



# 5.Remove periods from the "job" column:
client["job"] = client["job"].str.replace(".", "")



# 6.Convert values in the "previous_outcome" and "campaign_outcome" columns to binary:
campaign["previous_outcome"].replace({"success": 1, "failure": 0, "nonexistent": np.nan}, inplace=True)
campaign["campaign_outcome"].replace({"yes": 1, "no": 0}, inplace=True)



# 7.Add a column called "campaign_id" in campaign:
campaign["campaign_id"] = 1



# 8.Create a datetime column called "last_contact_date":
campaign["last_contact_date"] = pd.to_datetime("2022-" + campaign["month"].astype(str) + "-" + campaign["day"].astype(str))



# 9.Save the DataFrames to CSV files without an index:
client.to_csv("client.csv", index=False)
campaign.to_csv("campaign.csv", index=False)
economics.to_csv("economics.csv", index=False)



# 10.Create SQL code for creating tables and copying data:
client_table = """
CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    age INTEGER,
    job TEXT,
    marital TEXT,
    education TEXT,
    credit_default BOOLEAN,
    housing BOOLEAN,
    loan BOOLEAN
);

\copy client FROM 'client.csv' DELIMITER ',' CSV HEADER;
"""

campaign_table = """
CREATE TABLE campaign (
    campaign_id SERIAL PRIMARY KEY,
    client_id SERIAL REFERENCES client (id),
    number_contacts INTEGER,
    contact_duration INTEGER,
    pdays INTEGER,
    previous_campaign_contacts INTEGER,
    previous_outcome BOOLEAN,
    campaign_outcome BOOLEAN,
    last_contact_date DATE
);

\copy campaign FROM 'campaign.csv' DELIMITER ',' CSV HEADER;
"""

economics_table = """
CREATE TABLE economics (
    client_id SERIAL REFERENCES client (id),
    emp_var_rate FLOAT,
    cons_price_idx FLOAT,
    euribor_three_months FLOAT,
    number_employed FLOAT
);

\copy economics FROM 'economics.csv' DELIMITER ',' CSV HEADER;
"""