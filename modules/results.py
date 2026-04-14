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
        console.print(Panel(f"Precio: {product['price']}\nEnvio: {product['shipping']}\n"
        f'Rating: {product['rating']}\nLink: {product['link']}\nE-commerce: {product['source']}', 
        title=f'[bold cyan]{product['title']}[/bold cyan]', subtitle=f'Producto {index + 1}', expand=True, padding=(0, 2), style="bright_white on grey11", border_style="cyan"))
        console.print("\n")