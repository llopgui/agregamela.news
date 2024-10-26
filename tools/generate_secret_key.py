# tools/generate_secret_key.py

import secrets

def generate_secret_key(length: int = 50) -> str:
    """
    Genera una clave secreta segura para Django.

    Args:
        length (int): La longitud de la clave secreta.

    Returns:
        str: La clave secreta generada.
    """
    return ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for _ in range(length))

if __name__ == "__main__":
    print(generate_secret_key())

