import yfinance
import json
from collections import Counter

def main():
    print("Hello from money-maker!")


if __name__ == "__main__":
    main()
    help(yfinance)
    with open('snp_500.json', 'r') as f:
        data = json.load(f)
    print('Preview S&P JSON Data')
    for k, l in data.items():
        print(k, l[:3])
    print()
    print('Sector Counts')
    sector_counts = Counter(data['sectors'])
    for sector, count in sector_counts.items():
        print(sector, count)
    

