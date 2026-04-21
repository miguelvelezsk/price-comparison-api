from modules.scrapers import mercado_libre_scraper
from modules.scrapers import exito_scraper
from modules import data_processing
from modules import utils
import asyncio

async def orchestrator(product_name: str) -> list[dict[str, int | str]]:
    """
    Orchestrates the data flow.

    Args:
        product_name (str): The name of the product to search for.

    Returns:
        list[dict[str, int | str]]: A list of products sorted by price.
    """
    products_mercado_libre, products_exito = await run_scrapping(product_name)
    return data_processing.process_data(products_mercado_libre, products_exito, product_name)

async def run_scrapping(product_name: str) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """
    Runs the scrapping process for the given product name.

    Args:
        product_name (str): The name of the product to search for.

    Returns:
        tuple[list[dict[str, str]], list[dict[str, str]]]: A tuple containing the products found in Mercado Libre and Exito.
    """
    product_name_mercado_libre = utils.format_product_name(product_name)
    product_name_exito = utils.format_product_name(product_name, "+")

    products_mercado_libre, products_exito = await asyncio.gather(
        mercado_libre_scraper.manage_flow(product_name_mercado_libre),
        exito_scraper.manage_flow(product_name_exito)
    )

    return products_mercado_libre, products_exito
