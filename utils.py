import json
import requests
from config import keys


class ConversionException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты: {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту "{quote}"')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту "{base}"')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество "{amount}"')

        r = requests.get(
            f'https://v6.exchangerate-api.com/v6/1e97ad7fcd88f4a1d40e85c2/pair/{quote_ticker}/{base_ticker}')
        total_base = float(json.loads(r.content)['conversion_rate']) * amount
        return total_base
