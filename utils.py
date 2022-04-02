import sys
import currency_rates_update


if __name__ == '__main__':
    if len(sys.argv) > 1:
        currency_rates_update.currency_rates(sys.argv[1])
