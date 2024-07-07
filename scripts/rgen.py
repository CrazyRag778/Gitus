import random
import string

def gen(length=16):
    '''
    Generate a unique identification key.
    
    Parameters:
        length (int): Length of the generated key. Default is 16.
        
    Returns:
        str: A unique identification key.
    '''
    # Define the characters to use in the key
    characters = string.ascii_letters + string.digits
    # Generate the key
    key = ''.join(random.choice(characters) for _ in range(length))
    return key

# Example usage:
if __name__=="__main__":
    unique_key = generate_unique_key(16)
    print(unique_key)
