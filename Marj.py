def decode_message(cipher_text):
    """Decodes a cipher text using a simple substitution cipher.

    Args:
        cipher_text: The encrypted text.

    Returns:
        The decoded message.
    """

    cipher_dict = {
        '1234567890': 'A',
        '11234567890': 'B',
        '12345678901': 'C',
        # ... and so on for the rest of the alphabet
    }

    decoded_message = ''
    for i in range(0, len(cipher_text), 10):
        cipher_chunk = cipher_text[i:i+10]
        decoded_message += cipher_dict[cipher_chunk]

    return decoded_message

# Example usage:
cipher_text = "123456789012345678901234567890N1234567890012345678901234567890A1234567890N1234567890112345678901234567890L1234567890A1234567890N1234567890D123456789012345678901234567890"
decoded_message = decode_message(cipher_text)
print(f'"{decoded_message}"')
