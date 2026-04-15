# Technical Design Document (TDD)

## Overview

This script takes a product entered by the user and scrapes two e-commerce: Exito and Mercado Libre, then interacts with Playwright  and returns to the user the information with specific attributes from the best 3 products  from each e-commerce sorted from best to worst based on product’s price and a minimum product rating of 4 out of 5 stars. This information is displayed in cards shape presented in the CLI in spanish language.

## Architecture

### User input

This module requests the product name from the user and clean the product name.

### Mercado Libre scraper

This module searches the products on https://listado.mercadolibre.com.co/, and extract the necessary product data.

### Exito scraper

This module searches the products on https://www.exito.com/, and extract the necessary product data.

### Data processing and data cleaning

This module processes and cleans the data with different methods to facilitate data analysis, then the data is sorted and filtered based on metrics such as pricing and product rating

### Results presentation

This module displays the data in Spanish, in a card format to make it more clear for the user.

### Utils

This module contains helper functions and shared constants.

### Error handler

A centralized module that manages user-facing exceptions and system alerts. It uses the Rich library to standardize the visual style of errors in the CLI and supports dynamic string formatting for contextual feedback.

## Tech Stack

- Python 3.10
- Playwright 1.58.0
- Rich 15.0.0
- Numpy 2.4.4

## Data Flow

1. The user enters the product name in the console.
2. The scraper modules receive the product name from the input.
3. The scraper modules  interacts with the page and extract attributes from each web page.
4. If a request fails, the Scraper invokes the Error Handler.
5. The Error Handler displays a formatted message. If the error is recoverable (e.g., a retry), the scraper continues; if it is critical (e.g., no network), the handler terminates the execution or returns control to the main loop.
6. The attributes passes to the next module called processing.
7. The processing and cleaning modules filter and normalize the data based on the pricing and the product rating.
8. If no product meets the minimum rating threshold, the system displays a message and shows the best available products.
9. The data is sent to the module in charge of presenting the data.
10. The results are displayed as cards on the CLI in Spanish language. 

## Error Handling Strategy

- If no product meets the minimum rating threshold, the system displays a message *“No sé encontraron productos con calificación mayor a 4 estrellas, te mostramos los mejores disponibles.”* and shows the best available products.
- If no product is found on the e-commerce, the system displays a message *“No se encontró el producto {nombre de producto} en el e-commerce {nombre de e-commerce, reintentando (1 de 3)…}”*, retries up to 3 times and continues with the next e-commerce or sends the available data to the preprocessing and cleaning module.
- If the user enters an empty value or an invalid name with non alphabetic characters, the system displays a message “*No se ingresó un nombre válido, inténtalo de nuevo.*” and allows the user to try again.
- If the user doesn’t have network, the system displays a message “*No hay una red disponible, revisa tu conexión a internet”*  and terminates the execution.
- If the product doesn’t have a rating value, the system assigns a value of “NE” (No exists).
- If occurs a unexpected error, the system displays a message *“Ocurrió un error inesperado, finalizando ejecución”* and terminates the execution.

## Folder Structure

- /scraping_price_comparison
    - main.py
    - requirements.txt
    - README.md
    - modules/
        - __init__.py
        - user_input.py
        - data_processing.py
        - results.py
        - helpers.py
        - error_handler.py
        - scrapers/
            - __init__.py
            - mercado_libre_scraper.py
            - exito_scraper.py
        - tests/
            - test_scrapers.py