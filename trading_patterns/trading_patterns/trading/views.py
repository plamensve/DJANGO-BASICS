import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render
import pandas_ta as ta
import requests
import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def get_crypto_data(request, crypto_id):
    # Извличане на историческите данни за криптовалутата от CoinGecko API
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart?vs_currency=usd&days=30'
    response = requests.get(url)
    data = response.json()

    # Проверка дали ключът 'prices' съществува в отговора
    if 'prices' not in data:
        return JsonResponse({'error': 'Prices data not found'}, status=404)

    # Обработка на данните (извличане на цените на затваряне)
    prices = [item[1] for item in data['prices']]
    df = pd.DataFrame(prices, columns=['close'])

    # Изчисляване на RSI с pandas-ta
    df['RSI'] = ta.rsi(df['close'], length=14)

    # Филтриране на NaN стойности в колона RSI
    df = df.dropna(subset=['RSI'])

    # Връщане на резултатите като JSON
    return JsonResponse(df.to_dict(orient='records'), safe=False)


def plot_graph(request):
    # Данни (пример)
    data = [
        {"close": 64189.237324505426, "RSI": 52.28128127828418},
        {"close": 64179.32668855927, "RSI": 51.73830794641301},
        # Добавете вашите данни тук
    ]

    # Извличане на цените на затваряне и RSI стойностите
    close_prices = [item["close"] for item in data]
    rsi_values = [item["RSI"] for item in data]

    # Създаване на графиката
    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Close Price', color=color)
    ax1.plot(close_prices, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('RSI', color=color)
    ax2.plot(rsi_values, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('Close Price and RSI Indicator')

    # Записване на графиката в паметта
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    context = {
        'buf': buf
    }

    # Връщане на графиката като отговор
    return render(request, 'graph.html', context)