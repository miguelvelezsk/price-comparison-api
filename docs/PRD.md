# Product Requirements Document

## Problem Statement

Online shopping is increasingly common. In Colombia, in 2025 more than 19 million people bought products online. 

Mercado Libre is the leading company in Colombia, as it offers a good web application, and a good reputation, but sometimes, sellers on Mercado Libre take advantage of price volatility, making options like Exito very useful. 

However, comparing products across platforms manually is time-consuming and error prone, so this script provides a tool that helps users to choose the best product in online e-shops such as: Mercado Libre, and Exito, by comparing metrics like price and product rating.

## Target User

Frequent online shoppers in Colombia who purchase products at least twice a month across multiple platforms, value time efficiency when shopping online, struggle to determine which platform offers the best value for money and user experience, and feels comfortable with the Command-Line Interface (CLI). 

## Requirements

### Functional requirements

- **FR1:** Allow users to input a search term.
- **FR2:** Scrape and compare exactly 3 top-rated products per platform.
- **FR3:** Sort products primarily by price and secondarily by rating.
- **FR4:** Display product name, price, shipping cost, URL, and stock status.
- **FR5:** Fallback mechanism: if no 4-star products exist, show the highest-rated alternatives.

### Non-functional requirements

- **Performance:** Total execution time under 20 seconds.
- **Compliance:** Code must strictly follow PEP 8 and PEP 257 (docstrings).
- **Localization:** All CLI output must be in Spanish.
- **Error handling:** The system shall provide a centralized error reporting mechanism to ensure UI consistency.

## Out of Scope

- This version will not be available for other countries, only Colombia.
- This version will not support other languages, only Spanish.
- This version will not save comparisons.
- This version will not include an user interface.
- This version will not include an API service.