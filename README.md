# Python Crypto Tracker

A lightweight command-line tool to fetch live cryptocurrency prices using the CoinGecko API and log them to a CSV file.

## Features
- Fetches real-time price data for any coin supported by CoinGecko (Bitcoin, Ethereum, Solana, etc.)
- Supports multiple fiat currencies (USD, EUR, GBP)
- Logs each price check to `crypto_history.csv` with a timestamp, and writes column headers automatically on first run
- Handles network errors and API rate limits gracefully

## Usage
```bash
python crypto_price_track_v1.py
```
You'll be prompted for a coin and a currency.

## Project structure
- `crypto_price_track_v1.py` — current version
- `archive/` — earlier iterations of this project, kept to show progression

