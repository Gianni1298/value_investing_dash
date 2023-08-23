import pandas as pd
# import okama as ok

from common import cache
from common.finhub_requests import get_symbols as get_finnhub_symbols


@cache.memoize(timeout=2592000)
def get_symbols() -> list:
    """
    Get all available symbols (tickers) from assets namespaces.
    """
    list_of_symbols = get_finnhub_symbols()
    return list_of_symbols


# def get_symbols_names() -> dict:
#     """
#     Get a dictionary of long_name + symbol values.
#     """
#     namespaces = ok.assets_namespaces
#     list_of_symbols = [ok.symbols_in_namespace(ns).loc[:, ["symbol", "name"]] for ns in namespaces]
#     classifier_df = pd.concat(list_of_symbols, axis=0, join="outer", copy="false", ignore_index=True)
#     classifier_df["long_name"] = classifier_df.symbol + " : " + classifier_df.name
#     return classifier_df.loc[:, ["long_name", "symbol"]].to_dict("records")
#

# def get_currency_list():
#     inflation_list = ok.symbols_in_namespace("INFL").symbol.tolist()
#     return [x.split(".", 1)[0] for x in inflation_list]