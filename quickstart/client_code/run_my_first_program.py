from nada_dsl import *

def nada_main():
    # Initialize parties
    party1 = Party(name="Party1")

    # Define input integers
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    my_int3 = SecretInteger(Input(name="my_int3", party=party1))
    my_int4 = SecretInteger(Input(name="my_int4", party=party1))

    # Perform arithmetic operations
    # Addition
    add_result = my_int1 + my_int2 + my_int3 + my_int4
    
    # Subtraction
    sub_result = my_int1 - my_int2 - my_int3 - my_int4
    
    # Multiplication
    mul_result = my_int1 * my_int2 * my_int3 * my_int4
    
    # Division
    div_result = my_int1 / my_int2 / my_int3 / my_int4  # Secure division in NADA
    
    # Modulus
    mod_result = my_int1 % my_int2 % my_int3 % my_int4  # Secure modulus operation in NADA
    
   

    # Output the results
    return [
        Output(add_result, "add_output", party1),
        Output(sub_result, "sub_output", party1),
        Output(mul_result, "mul_output", party1),
        Output(div_result, "div_output", party1),
        Output(mod_result, "mod_output", party1)
        
    ]

if __name__ == "__main__":
    nada_main()




