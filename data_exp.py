# NYC 311 Service Requests - Data Exploration
# Step 2: Understanding our "departments", "incident types", and data quality

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

df = pd.read_csv("Gov-NYC-311_ServiceDesk.csv")

print("🔍 NYC 311 Data Exploration - Business Intelligence Focus")
print("="*60)

# Set display options for better readability
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Assuming your df is already loaded from Step 1
# If not, uncomment and run the API fetch again:
# [Previous API fetch code here]

print("📊 DATA QUALITY ASSESSMENT:")
print("="*30)

# Check data types and missing values
print("🔍 Column Data Types:")
print(df.dtypes)
print()

print("❌ Missing Values Analysis:")
missing_data = df.isnull().sum()
missing_percent = (missing_data / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing Count': missing_data,
    'Missing %': missing_percent.round(2)
}).sort_values('Missing Count', ascending=False)
print(missing_df)
print()

# Convert dates to proper datetime format
print("📅 Converting Dates...")
df['created_date'] = pd.to_datetime(df['created_date'])
df['closed_date'] = pd.to_datetime(df['closed_date'])

# Calculate resolution time (our key metric like Gowtham's project)
df['resolution_days'] = (df['closed_date'] - df['created_date']).dt.days

print("✅ Dates converted successfully!")
print()

print("🏢 AGENCY ANALYSIS (Our 'IT Departments'):")
print("="*45)

# Top agencies by volume (like Gowtham's department analysis)
agency_volume = df['agency_name'].value_counts().head(10)
print("📈 Top 10 Agencies by Service Request Volume:")
for i, (agency, count) in enumerate(agency_volume.items(), 1):
    percentage = (count / len(df)) * 100
    print(f"   {i:2d}. {agency[:40]:40s} | {count:,} requests ({percentage:.1f}%)")
print()

print("🎫 SERVICE REQUEST TYPES (Our 'Incident Categories'):")
print("="*55)

# Top complaint types (like IT incident categories)
complaint_volume = df['complaint_type'].value_counts().head(10)
print("📋 Top 10 Complaint Types:")
for i, (complaint, count) in enumerate(complaint_volume.items(), 1):
    percentage = (count / len(df)) * 100
    print(f"   {i:2d}. {complaint[:35]:35s} | {count:,} requests ({percentage:.1f}%)")
print()

print("📈 STATUS DISTRIBUTION (Open vs Closed Tickets):")
print("="*50)
status_dist = df['status'].value_counts()
print("🔘 Current Status Breakdown:")
for status, count in status_dist.items():
    percentage = (count / len(df)) * 100
    print(f"   • {status:15s} | {count:,} requests ({percentage:.1f}%)")
print()

print("🗽 GEOGRAPHIC DISTRIBUTION (Regional Performance):")
print("="*50)
borough_dist = df['borough'].value_counts()
print("📍 Requests by Borough:")
for borough, count in borough_dist.items():
    percentage = (count / len(df)) * 100
    if pd.notna(borough):  # Skip NaN boroughs
        print(f"   • {borough:15s} | {count:,} requests ({percentage:.1f}%)")
print()

print("⏱️ TEMPORAL ANALYSIS:")
print("="*25)

# Extract time components for analysis
df['month'] = df['created_date'].dt.month
df['quarter'] = df['created_date'].dt.quarter
df['year'] = df['created_date'].dt.year
df['hour'] = df['created_date'].dt.hour
df['day_of_week'] = df['created_date'].dt.day_name()

# Monthly trends
monthly_volume = df.groupby(['year', 'month']).size().reset_index(name='requests')
print("📅 Monthly Request Volume:")
for _, row in monthly_volume.head(10).iterrows():
    print(f"   • {int(row['year'])}-{int(row['month']):02d}: {row['requests']:,} requests")
print()

print("🎯 RESOLUTION TIME ANALYSIS (Key Performance Metric):")
print("="*55)

# Resolution time statistics (like Gowtham's efficiency metrics)
closed_tickets = df[df['status'] == 'Closed'].copy()
if len(closed_tickets) > 0:
    resolution_stats = closed_tickets['resolution_days'].describe()
    print("⚡ Resolution Time Statistics (Days):")
    print(f"   • Average Resolution Time: {resolution_stats['mean']:.1f} days")
    print(f"   • Median Resolution Time:  {resolution_stats['50%']:.1f} days")
    print(f"   • Fastest Resolution:      {resolution_stats['min']:.1f} days")
    print(f"   • Slowest Resolution:      {resolution_stats['max']:.1f} days")
    print(f"   • 75th Percentile:         {resolution_stats['75%']:.1f} days")
else:
    print("ℹ️  No closed tickets in sample for resolution analysis")
print()

print("🏆 TOP PERFORMING AGENCIES (Resolution Speed):")
print("="*45)

if len(closed_tickets) > 0:
    agency_performance = closed_tickets.groupby('agency_name')['resolution_days'].agg(['mean', 'count']).reset_index()
    agency_performance = agency_performance[agency_performance['count'] >= 10]  # Only agencies with 10+ tickets
    agency_performance = agency_performance.sort_values('mean').head(5)
    
    print("⚡ Fastest Resolving Agencies (Min 10 tickets):")
    for _, row in agency_performance.iterrows():
        print(f"   • {row['agency_name'][:35]:35s} | Avg: {row['mean']:.1f} days | Tickets: {int(row['count'])}")
else:
    print("ℹ️  Insufficient closed tickets for agency performance analysis")

print()
print("✅ DATA EXPLORATION COMPLETE!")
print("📊 Ready for business metrics calculation and Power BI dashboard creation!")
print("="*60)