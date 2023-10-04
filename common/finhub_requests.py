import finnhub
import common.settings as settings

# Set up the client
finnhub_client = finnhub.Client(api_key="cjj5101r01qirue62vigcjj5101r01qirue62vj0")


# Function to get the list of symbols
def get_symbols():
    exchanges = settings.exchanges_available
    display_symbols = [item["displaySymbol"] for item in finnhub_client.stock_symbols(exchanges)]

    finnhub_client.company_peers('AAPL')
    return display_symbols


def get_annual_financials(symbol: str):
    financials = finnhub_client.financials_reported(symbol=symbol, freq='annual')
    return financials


def get_earnings(symbol: str):
    financials = get_annual_financials(symbol)
    # TODO

