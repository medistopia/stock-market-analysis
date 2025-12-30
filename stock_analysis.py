"""
Stock Market Analysis Dashboard
Analyze historical stock data with visualizations and statistics

Requirements:
    pip install yfinance pandas matplotlib seaborn

Usage:
    python stock_analysis.py
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')  # Suppress warnings for cleaner output

class StockAnalyzer:
    def __init__(self, tickers, start_date, end_date):
        """
        Initialize the Stock Analyzer
        
        Args:
            tickers: List of stock symbols (e.g., ['AAPL', 'TSLA'])
            start_date: Start date for analysis (YYYY-MM-DD)
            end_date: End date for analysis (YYYY-MM-DD)
        """
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.stock_data = {}
        self.analysis_results = {}
    
    def fetch_data(self):
        """Download historical stock data from Yahoo Finance"""
        print("\n📥 Fetching stock data...")
        print("=" * 50)
        
        for ticker in self.tickers:
            try:
                print(f"Downloading {ticker}...", end=" ")
                data = yf.download(ticker, start=self.start_date, end=self.end_date, progress=False)
                
                if not data.empty:
                    self.stock_data[ticker] = data
                    print(f"✓ ({len(data)} days)")
                else:
                    print(f"✗ No data found")
                    
            except Exception as e:
                print(f"✗ Error: {e}")
        
        print(f"\n✓ Successfully fetched data for {len(self.stock_data)} stocks")
    
    def calculate_metrics(self):
        """Calculate key financial metrics for each stock"""
        print("\n📊 Calculating metrics...")
        print("=" * 50)
        
        for ticker, data in self.stock_data.items():
            # Calculate daily returns (percentage change day-to-day)
            data['Daily_Return'] = data['Close'].pct_change() * 100
            
            # Calculate cumulative returns (total % gain/loss from start)
            data['Cumulative_Return'] = (1 + data['Daily_Return'] / 100).cumprod() - 1
            
            # Calculate moving averages (common trading indicators)
            data['MA_50'] = data['Close'].rolling(window=50).mean()  # 50-day average
            data['MA_200'] = data['Close'].rolling(window=200).mean()  # 200-day average
            
            # Store calculated data back
            self.stock_data[ticker] = data
            
            # Store summary metrics in analysis_results
            self.analysis_results[ticker] = {
                'total_return': data['Cumulative_Return'].iloc[-1] * 100,  # Final return %
                'volatility': data['Daily_Return'].std(),  # Risk measure
                'avg_daily_return': data['Daily_Return'].mean(),
                'best_day': data['Daily_Return'].max(),
                'worst_day': data['Daily_Return'].min(),
                'current_price': float(data['Close'].iloc[-1]),  # Convert to float
                'start_price': float(data['Close'].iloc[0])  # Convert to float
            }
            
            print(f"✓ {ticker}: {self.analysis_results[ticker]['total_return']:.2f}% return")
        
        print(f"\n✓ Metrics calculated for {len(self.stock_data)} stocks")
    
    def generate_visualizations(self):
        """Create all visualizations"""
        print("\n📈 Generating visualizations...")
        print("=" * 50)
        
        # Set style for better-looking charts
        plt.style.use('seaborn-v0_8-darkgrid')
        sns.set_palette("husl")
        
        # 1. Stock Prices Over Time (Individual)
        print("Creating price charts...", end=" ")
        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
        fig.suptitle('Stock Prices Over Time', fontsize=16, fontweight='bold')
        
        for idx, (ticker, data) in enumerate(self.stock_data.items()):
            row = idx // 3
            col = idx % 3
            ax = axes[row, col]
            
            ax.plot(data.index, data['Close'], linewidth=2, label=ticker)
            ax.set_title(f'{ticker} Stock Price', fontweight='bold')
            ax.set_xlabel('Date')
            ax.set_ylabel('Price ($)')
            ax.grid(True, alpha=0.3)
            ax.legend()
            
        plt.tight_layout()
        plt.savefig('1_individual_prices.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓")
        
        # 2. All Stocks Comparison (Normalized to 100)
        print("Creating comparison chart...", end=" ")
        plt.figure(figsize=(14, 8))
        
        for ticker, data in self.stock_data.items():
            # Normalize to 100 (percentage change from start)
            normalized = (data['Close'] / data['Close'].iloc[0]) * 100
            plt.plot(data.index, normalized, linewidth=2.5, label=ticker)
        
        plt.title('Stock Performance Comparison (Normalized to 100)', 
                 fontsize=14, fontweight='bold', pad=20)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Normalized Price (Start = 100)', fontsize=12)
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('2_comparison_normalized.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓")
        
        # 3. Trading Volume Analysis
        print("Creating volume chart...", end=" ")
        fig, axes = plt.subplots(len(self.stock_data), 1, 
                                figsize=(14, 3*len(self.stock_data)))
        fig.suptitle('Trading Volume Over Time', fontsize=16, fontweight='bold')
        
        # Handle single vs multiple subplots
        if len(self.stock_data) == 1:
            axes = [axes]
        
        for idx, (ticker, data) in enumerate(self.stock_data.items()):
            ax = axes[idx]
            # Flatten volume data properly
            volume_data = data['Volume'].squeeze()  # Remove extra dimensions
            x_data = range(len(volume_data))
            
            ax.fill_between(x_data, volume_data, alpha=0.5, color='steelblue')
            ax.plot(x_data, volume_data, linewidth=1, color='darkblue', alpha=0.8)
            ax.set_title(f'{ticker} Trading Volume', fontweight='bold')
            ax.set_ylabel('Volume')
            ax.set_xlabel('Days')
            ax.grid(True, alpha=0.3, axis='y')
            # Format y-axis for large numbers
            ax.ticklabel_format(style='plain', axis='y')
            
        plt.tight_layout()
        plt.savefig('3_trading_volume.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓")
        
        # 4. Moving Averages (for first 3 stocks)
        print("Creating moving averages...", end=" ")
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))
        fig.suptitle('Price with Moving Averages (50-day & 200-day)', 
                    fontsize=14, fontweight='bold')
        
        for idx, (ticker, data) in enumerate(list(self.stock_data.items())[:3]):
            ax = axes[idx]
            ax.plot(data.index, data['Close'], linewidth=2, label='Close Price', alpha=0.8)
            ax.plot(data.index, data['MA_50'], linewidth=1.5, 
                   label='50-day MA', linestyle='--', alpha=0.7)
            ax.plot(data.index, data['MA_200'], linewidth=1.5, 
                   label='200-day MA', linestyle='--', alpha=0.7)
            ax.set_title(f'{ticker}', fontweight='bold')
            ax.set_xlabel('Date')
            ax.set_ylabel('Price ($)')
            ax.legend()
            ax.grid(True, alpha=0.3)
            
        plt.tight_layout()
        plt.savefig('4_moving_averages.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓")
        
        # 5. Daily Returns Distribution
        print("Creating returns distribution...", end=" ")
        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
        fig.suptitle('Daily Returns Distribution', fontsize=16, fontweight='bold')
        
        for idx, (ticker, data) in enumerate(self.stock_data.items()):
            row = idx // 3
            col = idx % 3
            ax = axes[row, col]
            
            returns = data['Daily_Return'].dropna()
            ax.hist(returns, bins=50, alpha=0.7, color='steelblue', edgecolor='black')
            ax.axvline(returns.mean(), color='red', linestyle='--', 
                      linewidth=2, label=f'Mean: {returns.mean():.2f}%')
            ax.set_title(f'{ticker} Daily Returns', fontweight='bold')
            ax.set_xlabel('Daily Return (%)')
            ax.set_ylabel('Frequency')
            ax.legend()
            ax.grid(True, alpha=0.3)
            
        plt.tight_layout()
        plt.savefig('5_returns_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓")
        
        # 6. Risk vs Return Scatter Plot
        print("Creating risk-return analysis...", end=" ")
        plt.figure(figsize=(12, 8))
        
        tickers_list = []
        returns_list = []
        volatility_list = []
        
        for ticker, results in self.analysis_results.items():
            tickers_list.append(ticker)
            returns_list.append(results['total_return'])
            volatility_list.append(results['volatility'])
        
        plt.scatter(volatility_list, returns_list, s=500, alpha=0.6, 
                   c=range(len(tickers_list)), cmap='viridis')
        
        for i, ticker in enumerate(tickers_list):
            plt.annotate(ticker, (volatility_list[i], returns_list[i]),
                        fontsize=12, fontweight='bold', ha='center', va='center')
        
        plt.title('Risk vs Return Analysis', fontsize=14, fontweight='bold', pad=20)
        plt.xlabel('Risk (Volatility - Daily Std Dev %)', fontsize=12)
        plt.ylabel('Return (%)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.tight_layout()
        plt.savefig('6_risk_return.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓")
        
        print(f"\n✓ Generated 6 visualizations")
        print("\n📁 Saved files:")
        print("  • 1_individual_prices.png")
        print("  • 2_comparison_normalized.png")
        print("  • 3_trading_volume.png")
        print("  • 4_moving_averages.png")
        print("  • 5_returns_distribution.png")
        print("  • 6_risk_return.png")
    
    def print_summary(self):
        """Print analysis summary to console"""
        print("\n" + "=" * 50)
        print("📈 STOCK MARKET ANALYSIS SUMMARY")
        print("=" * 50)
        
        print(f"\n📅 Analysis Period: {self.start_date} to {self.end_date}")
        print(f"📊 Stocks Analyzed: {', '.join(self.tickers)}")
        
        # Performance metrics for each stock
        print("\n📊 Performance Summary:")
        print("-" * 50)
        for ticker in self.tickers:
            if ticker in self.analysis_results:
                results = self.analysis_results[ticker]
                print(f"\n{ticker}:")
                print(f"  Total Return:     {results['total_return']:>8.2f}%")
                print(f"  Volatility:       {results['volatility']:>8.2f}%")
                print(f"  Avg Daily Return: {results['avg_daily_return']:>8.2f}%")
                print(f"  Best Day:         {results['best_day']:>8.2f}%")
                print(f"  Worst Day:        {results['worst_day']:>8.2f}%")
                print(f"  Start Price:      ${results['start_price']:>8.2f}")
                print(f"  Current Price:    ${results['current_price']:>8.2f}")
        
        # Find best and worst performers
        if self.analysis_results:
            best_stock = max(self.analysis_results.items(), 
                           key=lambda x: x[1]['total_return'])
            worst_stock = min(self.analysis_results.items(), 
                            key=lambda x: x[1]['total_return'])
            most_volatile = max(self.analysis_results.items(),
                               key=lambda x: x[1]['volatility'])
            
            print("\n🏆 Best Performer:  " + 
                  f"{best_stock[0]} (+{best_stock[1]['total_return']:.2f}%)")
            print(f"📉 Worst Performer: " + 
                  f"{worst_stock[0]} ({worst_stock[1]['total_return']:.2f}%)")
            print(f"⚠️  Most Volatile:   " + 
                  f"{most_volatile[0]} ({most_volatile[1]['volatility']:.2f}% daily volatility)")
    
    def run_analysis(self):
        """Run complete analysis pipeline"""
        print("\n🚀 Starting Stock Market Analysis")
        print("=" * 50)
        
        # Step 1: Fetch data
        self.fetch_data()
        
        if not self.stock_data:
            print("\n❌ No data fetched. Exiting.")
            return
        
        # Step 2: Calculate metrics
        self.calculate_metrics()
        
        # Step 3: Generate visualizations
        self.generate_visualizations()
        
        # Step 4: Print summary
        self.print_summary()
        
        print("\n✓ Analysis complete!")


def main():
    """Main execution function"""
    
    # Configuration
    tickers = ['AAPL', 'TSLA', 'GOOGL', 'MSFT', 'NVDA']  # Stocks to analyze
    end_date = datetime.now().strftime('%Y-%m-%d')  # Today
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')  # 1 year ago
    
    print("\n" + "=" * 50)
    print("📊 STOCK MARKET ANALYSIS DASHBOARD")
    print("=" * 50)
    print(f"\n📈 Analyzing: {', '.join(tickers)}")
    print(f"📅 Period: {start_date} to {end_date}")
    
    # Create analyzer and run
    analyzer = StockAnalyzer(tickers, start_date, end_date)
    analyzer.run_analysis()


if __name__ == "__main__":
    main()