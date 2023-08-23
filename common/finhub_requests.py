import finnhub
import common.settings as settings

# Set up the client
finnhub_client = finnhub.Client(api_key="cjj5101r01qirue62vigcjj5101r01qirue62vj0")


# Function to get the list of symbols
def get_symbols():
    exchanges = settings.exchanges_available
    display_symbols = [item["displaySymbol"] for item in finnhub_client.stock_symbols(exchanges)]

    return display_symbols


