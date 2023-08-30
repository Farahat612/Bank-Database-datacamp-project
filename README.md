# Designing a Bank Marketing Database

## Project Description

This is a design of a bank marketing database, a project that was a part of DataCamp Data Engineering learning path.
In this project, we leverage data engineering skills to clean and structure data for designing a PostgreSQL database to store information about marketing campaigns conducted by a bank. The goal is to create an efficient database that's expandable for future campaigns.


## Project Requirements

Personal loans are a major revenue source for banks, generating substantial interest. Our task is to clean and store data from a recent marketing campaign promoting personal loans. The data will be organized in a PostgreSQL database, with the schema designed for future campaign data.

## Database Tables

### `client` Table

| Column           | Data Type | Description                             |
|------------------|-----------|-----------------------------------------|
| `id`             | `serial`  | Client ID (Primary Key)                 |
| `age`            | `integer` | Client's age in years                   |
| `job`            | `text`    | Client's job                            |
| `marital`        | `text`    | Marital status                          |
| `education`      | `text`    | Education level                         |
| `credit_default` | `boolean` | Defaulted on credit                     |
| `housing`        | `boolean` | Has housing loan                        |
| `loan`           | `boolean` | Has personal loan                       |

### `campaign` Table

| Column                     | Data Type | Description                             |
|----------------------------|-----------|-----------------------------------------|
| `campaign_id`              | `serial`  | Campaign ID (Primary Key)               |
| `client_id`                | `serial`  | Client ID (Foreign Key)                 |
| `number_contacts`          | `integer` | Number of contact attempts             |
| `contact_duration`         | `integer` | Last contact duration                   |
| `pdays`                    | `integer` | Days since contact in previous campaign|
| `previous_campaign_contacts`| `integer` | Contact attempts in previous campaign  |
| `previous_outcome`         | `boolean` | Outcome of previous campaign            |
| `campaign_outcome`         | `boolean` | Outcome of current campaign             |
| `last_contact_date`        | `date`    | Last contact date                       |

### `economics` Table

| Column               | Data Type | Description                             |
|----------------------|-----------|-----------------------------------------|
| `client_id`          | `serial`  | Client ID (Foreign Key)                 |
| `emp_var_rate`       | `float`   | Employment variation rate              |
| `cons_price_idx`     | `float`   | Consumer price index                    |
| `euribor_three_months`| `float`  | Euro Interbank Offered Rate (euribor)   |
| `number_employed`    | `float`   | Number of employees                     |

## Instructions and Steps

1. Read `bank_marketing.csv` using pandas.
2. Split data into `client`, `campaign`, and `economics` DataFrames.
3. Clean data and rename columns as per requirements.
4. Create datetime columns and remove redundant data.
5. Save cleaned DataFrames as CSVs: `client.csv`, `campaign.csv`, and `economics.csv`.
6. Use SQL template to create table scripts for each table.
7. Share SQL scripts with bank for database setup.

## Project Code

To see detailed implementation, refer to the Python notebook `bank_marketing_database.ipynb` or `bank_marketing_database.py` in this repository.

## Known Issues or Limitations

Currently, there are no known issues or limitations with this project.

## License

This project is licensed under the [MIT License](LICENSE).


