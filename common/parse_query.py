import io
from typing import Optional

import pandas as pd


def make_list_from_string(symbols: Optional[str], char_type: str = "str") -> Optional[list]:
    """
    Get list of parameters from URL query (csv - comma separated).
    """
    if symbols:
        tickers_io = io.StringIO(symbols)
        df = pd.read_csv(tickers_io, header=None, dtype=char_type)
        result = df.iloc[0, :].to_list()
    else:
        result = None
    return result


def get_marketCap(market_cap: int) -> str:
    """
    Convert marketCap to string.
    """
    if market_cap == "N/A":
        return market_cap
    elif market_cap < 1000000000:
        return f"{round(market_cap / 1000000, 1)}M"
    elif market_cap >= 1000000000:
        return f"{round(market_cap / 1000000000, 1)}B"
    else:
        return "N/A"
