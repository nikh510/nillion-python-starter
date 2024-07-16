from nada_dsl import *

def transfer_transaction(sender_party, receiver_party, transfer_amount):
    # Define parties
    sender = Party(name=sender_party)
    receiver = Party(name=receiver_party)
    
    # Define wallet balances (initial amounts)
    sender_balance = SecretInteger(Input(name="sender_balance", party=sender))
    receiver_balance = SecretInteger(Input(name="receiver_balance", party=receiver))
    
    # Perform secure computation for the transaction
    new_sender_balance = sender_balance - transfer_amount
    new_receiver_balance = receiver_balance + transfer_amount
    
    # Output the new balances securely
    return [
        Output(new_sender_balance, "new_sender_balance", sender),
        Output(new_receiver_balance, "new_receiver_balance", receiver)
    ]

if __name__ == "__main__":
    # Simulate a transaction between two parties
    sender_party = "Party1"
    receiver_party = "Party2"
    transfer_amount = SecretInteger(Input(name="transfer_amount", party=sender_party))  # Use Input for the transfer amount
    
    transaction_result = transfer_transaction(sender_party, receiver_party, transfer_amount)
    print("Transaction result:", transaction_result)


