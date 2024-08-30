Drug Price Comparison Tool
Overview

The Drug Price Comparison Tool is a web-based application that helps users find the most optimal price for medications available across four major online pharmacies in Georgia: Aversi, PSP, GPC, and Pharmadepot. By entering the name of a drug in the search field, users can instantly compare prices and other relevant details, such as the country of origin and available images, all on a single page.
Features

    Search Functionality: Simply enter the name of the drug you are looking for, and the tool will fetch and display results from the four supported pharmacies.

    Price Comparison: The results are automatically sorted by price, allowing users to quickly identify the most affordable option.

    Detailed Information: Along with the price, the tool displays the drug's name, country of origin, and a photo (if available) for each result.

    Direct Links: Each result includes a link that takes users directly to the pharmacy's page for the drug, making it easy to make a purchase.

Supported Pharmacies

    Aversi
    PSP
    GPC
    Pharmadepot

How It Works

    Scraping: The tool uses web scraping techniques to gather data from the online pharmacies' websites.
    Data Aggregation: Once the data is collected, it is aggregated into a single view and sorted by price.
    Display: The results are displayed in a user-friendly format, with all relevant information easily accessible.

Technologies Used

    Python: For the backend logic and web scraping tasks.
    Flask: As the web framework to handle user requests and display results.
    Selenium: For web scraping and interacting with JavaScript-heavy websites.
    HTML/CSS: For the frontend interface.

Installation

    Clone the repository:
      git clone https://github.com/yourusername/drug-price-comparison-tool.git
    
    Navigate to the project directory:
      cd drug-price-comparison-tool
    
    Install the required dependencies:
      pip install -r requirements.txt
    
    Run the application:
      python app.py
    
    Open your browser and navigate to http://localhost:5000 to use the tool.
    
Future Improvements

  Support for Additional Pharmacies: Expanding the tool to include more pharmacies for a more comprehensive comparison.
  User Accounts: Allowing users to save searches and set price alerts.
  Mobile Optimization: Improving the user experience on mobile devices.
