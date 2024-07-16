from nada_dsl import *

def nada_main():
    # Initialize the parties involved
    party1 = Party(name="Party1")
    
    # Define the secret integers with input from party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform computation using my_int1 and my_int2
    # For example, let's add the two integers
    result = my_int1 + my_int2
    
    # Output the result
    return [Output(result, "my_output", party1)]

if __name__ == "__main__":
    nada_main()
