from rich.console import Console
from rich.panel import Panel

console = Console()

def display_results(products: list[dict[str, str]]) -> None:
    """
    Displays the product information in format of panels

    Args:
        products: A list of products.
    
    Returns:
        None
    """
    for index, product in enumerate(products):
        console.print(Panel.fit(f"Precio: {product['price']}\nEnvio: {product['shipping']}\n"
        f'Rating: {product['rating']}\nLink: {product['link']}\nE-commerce: {product['source']}', 
        title=f'Producto {index + 1}', subtitle=f'{product['title']}'))