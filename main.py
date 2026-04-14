from modules import user_input
from modules.scrapers import mercado_libre_scraper
from modules.scrapers import exito_scraper
from modules import data_processing
from modules import utils
from modules import results
from rich.console import Console
import asyncio

console = Console()

def main():
    product_name = user_input.get_product_name()
    product_name_mercado_libre = utils.format_product_name(product_name)
    product_name_exito = utils.format_product_name(product_name, "+")

    products_mercado_libre = asyncio.run(mercado_libre_scraper.manage_flow(product_name_mercado_libre))
    products_exito = asyncio.run(exito_scraper.manage_flow(product_name_exito))
    top_products = data_processing.process_data(products_mercado_libre, products_exito, product_name)

    console.print("\n")
    console.rule("[bold white]Productos encontrados")
    console.print("\n")
    results.display_results(top_products)

main()
