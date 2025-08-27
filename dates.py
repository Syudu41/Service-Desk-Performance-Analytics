# Date Range Analysis - Check what's happening with the date coverage

import pandas as pd
import numpy as np
from datetime import datetime

print("🔍 DATE RANGE ANALYSIS")
print("=" * 30)

# Load your dataset
try:
    df = pd.read_csv('Gov-NYC-311_ServiceDesk.csv')
    print(f"✅ Loaded {len(df):,} records")
    
    # Convert created_date to datetime
    df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')
    
    print("\n📅 DATE COVERAGE ANALYSIS:")
    print("=" * 30)
    
    # Basic date info
    min_date = df['created_date'].min()
    max_date = df['created_date'].max()
    date_range = max_date - min_date
    
    print(f"📅 Earliest Record: {min_date}")
    print(f"📅 Latest Record: {max_date}")
    print(f"📊 Total Date Range: {date_range.days} days")
    print()
    
    # Count unique dates
    unique_dates = df['created_date'].dt.date.nunique()
    print(f"📊 Unique Dates with Data: {unique_dates}")
    
    # Show all unique dates
    date_counts = df['created_date'].dt.date.value_counts().sort_index()
    print(f"\n📋 DAILY RECORD COUNTS:")
    print("Date       | Records")
    print("-" * 20)
    for date, count in date_counts.items():
        print(f"{date} | {count:,}")
    
    print()
    
    # Check for missing dates in expected range
    if min_date.year >= 2024:
        print("🤔 ISSUE IDENTIFIED:")
        print(f"   • Your data only starts from {min_date.strftime('%Y-%m-%d')}")
        print("   • Expected: Jan 1, 2024 - Present")
        print("   • Actual: Only 8 days in August 2025")
        print()
        
        print("💡 POSSIBLE REASONS:")
        print("   1. CSV contains only recent sample data (not full historical)")
        print("   2. API query was limited by default parameters")
        print("   3. Dataset filtering removed older records")
        print("   4. Original data source only had recent data")
        print()
    
    # Check monthly distribution
    monthly_counts = df.groupby([df['created_date'].dt.year, df['created_date'].dt.month]).size()
    print("📊 MONTHLY DISTRIBUTION:")
    for (year, month), count in monthly_counts.items():
        print(f"   {year}-{month:02d}: {count:,} records")
    
    print()
    
    # Check if we need to re-fetch data
    if unique_dates < 30:  # Less than a month of data
        print("🚨 RECOMMENDATION:")
        print("   Your dataset only covers a few days - this limits analysis quality")
        print("   Consider:")
        print("   1. Re-download with broader date range")
        print("   2. Use different API parameters")
        print("   3. Get a larger dataset from NYC Open Data")
        print()
    
except Exception as e:
    print(f"❌ Error: {e}")

print("=" * 50)