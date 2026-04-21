"""
This module contains a function in charge of handling errors.
"""
from fastapi import HTTPException

error_messages = {
    'no_minimum_rating': 'No se encontraron productos con calificación mayor a 4 estrellas, te mostramos los mejores disponibles.',
    'no_products_found': 'No se encontró el producto {} en el e-commerce {}, reintentando ({}/3)...',
    'no_products_found_after_attempts': 'No se encontró el producto {} en el e-commerce {}, saltando paso',
    'no_valid_product_name': 'No se ingresó un nombre válido, inténtalo de nuevo.',
    'no_network_connection': 'No hay conexión a la red, revisa tu conexión a internet.',
    'no_data_found': 'No se encontró la información del e-commerce {}',
    'unexpected_error': 'Ocurrió un error inesperado en el e-commerce {}'
}

status_codes = {
    'no_minimum_rating': 400,
    'no_products_found': 404,
    'no_products_found_after_attempts': 404,
    'no_valid_product_name': 400,
    'no_network_connection': 503,
    'no_data_found': 404,
    'unexpected_error': 500
}

def handle_error(error_type: str, product_name: str = "", e_commerce: str = "", counter: int = 0) -> None:
    """
    Handles errors by printing the appropriate error message.

    Args:
        error_type (str): The type of error to handle.
        product_name (str, optional): The name of the product. Defaults to "".
        e_commerce (str, optional): The name of the e-commerce. Defaults to "".
        counter (int, optional): The counter of the attempts. Defaults to 0.
    """
    if error_type in error_messages:
        raise HTTPException(status_code=status_codes[error_type], detail=error_messages[error_type].format(product_name, e_commerce, counter))
    raise HTTPException(status_code=status_codes['unexpected_error'], detail=error_messages['unexpected_error'])

def print_message(error_type: str, product_name: str, e_commerce: str, counter: int) -> None:
    """
    Prints the error message.
    
    Args:
        error_type (str): The type of error to print.
        product_name (str): The name of the product.
        e_commerce (str): The name of the e-commerce.
        counter (int): The counter of the attempts.
    """
    print(error_messages[error_type].format(product_name, e_commerce, counter))