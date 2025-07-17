
import pandas as pd
import json

# Load the JSON file
with open('user-wallet-transactions.json') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Feature engineering
# Example features
df['transaction_count'] = df.groupby('wallet_id')['transaction_id'].transform('count')
df['deposit_count'] = df[df['action'] == 'deposit'].groupby('wallet_id')['transaction_id'].transform('count')
df['borrow_count'] = df[df['action'] == 'borrow'].groupby('wallet_id')['transaction_id'].transform('count')
df['repay_count'] = df[df['action'] == 'repay'].groupby('wallet_id')['transaction_id'].transform('count')
df['average_transaction_amount'] = df.groupby('wallet_id')['amount'].transform('mean')
df['wallet_age'] = (pd.to_datetime('now') - pd.to_datetime(df['timestamp'])).dt.days

# Placeholder for scoring logic
def calculate_credit_score(row):
    score = 0
    # Example scoring logic based on features
    score += row['transaction_count'] * 2  # More transactions = higher score
    score += row['deposit_count'] * 5      # More deposits = higher score
    score -= row['borrow_count'] * 3       # More borrowing = lower score
    score -= row['repay_count'] * 2        # More repayments = higher score
    score += row['average_transaction_amount'] / 10  # Higher amounts = higher score
    score += max(0, 1000 - row['wallet_age']) / 10  # Newer wallets get higher scores

    # Ensure score is between 0 and 1000
    return min(max(score, 0), 1000)

# Apply scoring function
df['credit_score'] = df.apply(calculate_credit_score, axis=1)

# Save the results to CSV
df[['wallet_id', 'credit_score']].to_csv('wallet_scores.csv', index=False)

print("Wallet scores have been calculated and saved to 'wallet_scores.csv'.")
