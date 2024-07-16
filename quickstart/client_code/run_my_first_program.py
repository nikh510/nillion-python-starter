from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")

    input_string = Input(name="input_string", party=party1)

    
    unique_chars = []
    result_string = ""

    
    for char in input_string:
        if char not in unique_chars:
            unique_chars.append(char)
            # Modify this line to add a specific word next to each unique character
            result_string += f"{char}word "  # Replace 'word' with your desired word

    return [Output(result_string, "output_string", party1)]

if __name__ == "__main__":
    nada_main()

