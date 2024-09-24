import pandas_ta as ta
import pandas as pd

# Създаване на примерни данни
data = {
    'close': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}
df = pd.DataFrame(data)

# Изчисляване на RSI (Relative Strength Index) с по-кратък период (например 5)
rsi = ta.rsi(df['close'], length=5)
print(rsi)
