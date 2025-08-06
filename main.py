from data.loader import get_stock_data
from analysis.indicators import add_technical_indicators
from visualization.plot_chart import plot_candlestick_volume

ticker = "VIC"
df = get_stock_data(ticker, "2023-01-01", "2025-08-01")
df = add_technical_indicators(df)

plot_candlestick_volume(df, ticker)
