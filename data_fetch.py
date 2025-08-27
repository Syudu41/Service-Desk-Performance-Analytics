# NYC 311 Service Requests - Data Fetch & Initial Exploration
# Step 1: Import libraries and fetch data

import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

print("🎯 NYC 311 Service Request Analytics - Data Fetch")
print("="*50)

total_records = 20000
# Your API endpoint (let's start with 5000 records for testing)
api_url = f"""https://data.cityofnewyork.us/resource/erm2-nwe9.json?$query=SELECT
  `unique_key`,
  `created_date`,
  `closed_date`,
  `agency`,
  `agency_name`,
  `complaint_type`,
  `descriptor`,
  `location_type`,
  `status`,
  `borough`
WHERE
  `created_date`
    BETWEEN "2024-01-01T00:00:00" :: floating_timestamp
    AND "2025-08-27T16:44:11" :: floating_timestamp
ORDER BY `created_date` DESC NULL FIRST
LIMIT {total_records}"""

# Clean up the URL (remove line breaks and spaces)
clean_url = api_url.replace('\n', '%0A').replace(' ', '%20')

print(f"📡 Fetching data from NYC Open Data API...")
print(f"📊 Date Range: Jan 1, 2024 - Aug 27, 2025")
print(f"🔢 Sample Size: {total_records} records")
print()

try:
    # Fetch the data
    response = requests.get(clean_url)
    
    if response.status_code == 200:
        # Convert to DataFrame
        data = response.json()
        df = pd.DataFrame(data)
        
        print(f"✅ SUCCESS! Downloaded {len(df)} records")
        print(f"📋 Columns: {len(df.columns)}")
        print()
        
        # Basic info about the dataset
        print("📊 DATASET OVERVIEW:")
        print(f"   • Shape: {df.shape}")
        print(f"   • Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        print()
        
        # Show column names
        print("📋 AVAILABLE COLUMNS:")
        for i, col in enumerate(df.columns, 1):
            print(f"   {i:2d}. {col}")
            
        print()
        print("🔍 FIRST 3 RECORDS:")
        print(df.head(3))
        df.to_csv("Gov-NYC-311_ServiceDesk.csv", index=False)
    else:
        print(f"❌ ERROR: HTTP {response.status_code}")
        print(f"Response: {response.text[:200]}...")
        
except Exception as e:
    print(f"❌ ERROR: {e}")
    print("🔧 Let's try a simpler approach...")