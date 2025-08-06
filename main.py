import pandas as pd
from vnstock import stock_historical_data
import talib

def get_technical_analysis(symbol):
    df = stock_historical_data(symbol, "2024-01-01", "2025-08-01", resolution="1D")
    df['RSI'] = talib.RSI(df['close'], timeperiod=14)
    df['MACD'], _, _ = talib.MACD(df['close'])
    latest_close = df['close'].iloc[-1]
    latest_rsi = df['RSI'].dropna().iloc[-1]
    latest_macd = df['MACD'].dropna().iloc[-1]
    return latest_close, latest_rsi, latest_macd

def rule_based_analysis(rsi, macd):
    rsi_signal = "quá mua" if rsi > 70 else "quá bán" if rsi < 30 else "trung tính"
    macd_signal = "tăng" if macd > 0 else "giảm" if macd < 0 else "trung tính"
    return f"- RSI: {rsi:.2f} ({rsi_signal})
- MACD: {macd:.2f} (xu hướng {macd_signal})"

def run_chatbot():
    print("📊 Chatbot Phân Tích Cổ Phiếu Đơn Giản (Không dùng AI)")
    while True:
        symbol = input("\nNhập mã cổ phiếu (VD: VIC, VNM, SSI): ").strip().upper()
        if not symbol:
            continue
        try:
            close, rsi, macd = get_technical_analysis(symbol)
            print(f"\n✅ Giá hiện tại của {symbol} là: {close:.2f}")
            print(rule_based_analysis(rsi, macd))
        except Exception as e:
            print("❌ Lỗi khi phân tích:", e)

if __name__ == "__main__":
    run_chatbot()
