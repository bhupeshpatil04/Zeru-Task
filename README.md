# Zeru-Task
# Wallet Credit Scoring System

## Overview
This project aims to develop a machine learning model that assigns a credit score between 0 and 1000 to wallets interacting with the Aave V2 protocol. The score reflects the reliability and responsibility of wallet usage based on historical transaction behavior.

## Features Engineered
The following features were engineered from the transaction data:
- **Transaction Count**: Total number of transactions per wallet.
- **Deposit Frequency**: Number of deposit actions performed.
- **Borrow Frequency**: Number of borrow actions performed.
- **Repay Frequency**: Number of repay actions performed.
- **Average Transaction Amount**: Average amount involved in transactions.
- **Wallet Age**: Duration since the wallet was created.
- **Time Between Transactions**: Average time interval between consecutive transactions.

## Model Development
A Random Forest Regressor was chosen for this task due to its robustness and ability to handle non-linear relationships. The model was trained on a portion of the dataset and validated on a separate test set.

