# 📈 Stock Market Analysis Dashboard

A Python-based stock market analysis tool that fetches real-time financial data, calculates key metrics, and generates professional visualizations for investment analysis. Built with yfinance, Pandas, and Matplotlib.

## Features

- 📊 **Real-Time Data Fetching** - Downloads historical stock data from Yahoo Finance
- 📈 **Statistical Analysis** - Calculates returns, volatility, and moving averages
- 🎨 **6 Professional Visualizations** - Comprehensive charts for market analysis
- 💹 **Performance Metrics** - Total returns, risk analysis, and comparative performance
- 🔍 **Multi-Stock Comparison** - Analyze multiple stocks simultaneously
- 📉 **Risk Assessment** - Volatility and risk-return analysis

## Visualizations Generated

1. **Individual Stock Prices** - Price trends over time for each stock
2. **Normalized Comparison** - All stocks compared on a single chart (base 100)
3. **Trading Volume** - Volume analysis showing market activity
4. **Moving Averages** - 50-day and 200-day moving average overlays
5. **Returns Distribution** - Histogram showing daily return patterns
6. **Risk vs Return** - Scatter plot mapping volatility against returns

## Installation

### Prerequisites
- Python 3.7+

### Setup
```bash
git clone https://github.com/medistopia/stock-market-analysis.git
cd stock-market-analysis
```

### Install Dependencies
```bash
pip install yfinance pandas matplotlib seaborn
```

## Usage

### Run the Analysis
```bash
python stock_analysis.py
```

The script will:
1. Download 1 year of historical data for 5 tech stocks (AAPL, TSLA, GOOGL, MSFT, NVDA)
2. Calculate financial metrics (returns, volatility, moving averages)
3. Generate 6 visualization files
4. Display a comprehensive analysis summary

### Customize Stocks and Time Period

Edit `main()` function in `stock_analysis.py`:
```python
# Change these values:
tickers = ['AAPL', 'TSLA', 'GOOGL', 'MSFT', 'NVDA']  # Your stock choices
start_date = '2023-01-01'  # Start date
end_date = '2024-12-31'    # End date
```

## Sample Output

### Console Summary
```
📊 STOCK MARKET ANALYSIS DASHBOARD
==================================================

📈 Analyzing: AAPL, TSLA, GOOGL, MSFT, NVDA
📅 Period: 2024-01-01 to 2024-12-29

📥 Fetching stock data...
==================================================
Downloading AAPL... ✓ (249 days)
Downloading TSLA... ✓ (249 days)
Downloading GOOGL... ✓ (249 days)
Downloading MSFT... ✓ (249 days)
Downloading NVDA... ✓ (249 days)

📊 Performance Summary:
--------------------------------------------------

GOOGL:
  Total Return:        +64.58%
  Volatility:           1.85%
  Avg Daily Return:     0.21%
  Best Day:            +8.45%
  Worst Day:           -6.23%

🏆 Best Performer:  GOOGL (+64.58%)
📉 Worst Performer: AAPL (+8.90%)
⚠️  Most Volatile:   TSLA (3.12% daily volatility)
```

### Generated Files
- `1_individual_prices.png` - Individual stock price charts
- `2_comparison_normalized.png` - Multi-stock comparison
- `3_trading_volume.png` - Volume analysis
- `4_moving_averages.png` - Technical indicators
- `5_returns_distribution.png` - Statistical distributions
- `6_risk_return.png` - Risk-return scatter plot

## Metrics Explained

### Daily Return
Percentage change in stock price from one day to the next:
```
Daily Return = ((Close Today - Close Yesterday) / Close Yesterday) × 100
```

### Cumulative Return
Total percentage gain or loss since the start date:
```
Cumulative Return = ((Current Price - Start Price) / Start Price) × 100
```

### Volatility
Standard deviation of daily returns - measures risk:
- **Low volatility** (<2%): More stable, less risky
- **Medium volatility** (2-3%): Moderate risk
- **High volatility** (>3%): More risky, potential for larger swings

### Moving Averages
- **50-day MA**: Short-term trend indicator
- **200-day MA**: Long-term trend indicator
- **Golden Cross**: When 50-day crosses above 200-day (bullish signal)
- **Death Cross**: When 50-day crosses below 200-day (bearish signal)

## Project Structure

```
stock-market-analysis/
├── stock_analysis.py          # Main analysis script
├── 1_individual_prices.png    # Generated visualization
├── 2_comparison_normalized.png # Generated visualization
├── 3_trading_volume.png       # Generated visualization
├── 4_moving_averages.png      # Generated visualization
├── 5_returns_distribution.png # Generated visualization
├── 6_risk_return.png          # Generated visualization
├── README.md                  # This file
└── LICENSE                    # MIT License
```

## Technical Implementation

### Data Fetching
- Uses `yfinance` library to download historical stock data from Yahoo Finance
- Retrieves OHLCV data (Open, High, Low, Close, Volume)
- Handles multiple tickers with error handling

### Calculations
- **Returns**: Calculated using pandas `.pct_change()` method
- **Moving Averages**: Calculated using `.rolling()` window functions
- **Volatility**: Standard deviation of daily returns using `.std()`

### Visualizations
- Built with `matplotlib` and `seaborn`
- High-resolution output (300 DPI)
- Professional color schemes and formatting
- Multiple subplot layouts for comprehensive analysis

## Technologies Used

- **Python 3** - Core programming language
- **yfinance** - Yahoo Finance API for stock data
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical visualization
- **NumPy** - Numerical computations

## Use Cases

- 📊 **Investment Research** - Analyze potential investments
- 📈 **Portfolio Tracking** - Monitor your holdings
- 🎓 **Educational** - Learn about stock market analysis
- 💼 **Professional Analysis** - Generate reports for presentations
- 🔍 **Technical Analysis** - Study price trends and patterns

## Future Enhancements

- [ ] CLI arguments for custom stock selection
- [ ] Additional technical indicators (RSI, MACD, Bollinger Bands)
- [ ] Portfolio simulation and backtesting
- [ ] PDF report generation
- [ ] Real-time streaming data
- [ ] Correlation matrix and heatmap
- [ ] Sector analysis and comparison
- [ ] News sentiment integration

## Limitations

- Data source is Yahoo Finance (historical data only, 15-min delay for real-time)
- Requires internet connection to fetch data
- Analysis is purely technical (no fundamental analysis)
- Past performance does not guarantee future results

## License

This project is open source and available under the MIT License.

## Author

**Joshua V.**  
University of North Georgia - Computer Science  
[LinkedIn](https://www.linkedin.com/in/jevene/) | [GitHub](https://github.com/medistopia)

## Acknowledgments

- Built as part of a machine learning engineer career roadmap
- Data provided by Yahoo Finance via yfinance library
- Inspired by quantitative analysis and algorithmic trading concepts

---

**Disclaimer**: This tool is for educational and research purposes only. Not financial advice. Always do your own research and consult with financial professionals before making investment decisions.

**⚠️ Investment Warning**: Stock trading involves risk. Past performance is not indicative of future results.
