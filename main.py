import pandas as pd
import matplotlib.pyplot as plt

# Sample Uber data (replace this with your actual data)
data = {
    "Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
    "Time": ["08:30", "12:15", "17:45"],
    "Pickup_Location": ["Location_A", "Location_B", "Location_A"],
    "Dropoff_Location": ["Location_X", "Location_Y", "Location_Z"],
    "Distance": [5.2, 8.3, 6.0]
}

# Create a DataFrame
uber_data = pd.DataFrame(data)

# Convert the 'Date' column to a datetime object
uber_data['Date'] = pd.to_datetime(uber_data['Date'])

# Extract additional features like day of the week and hour
uber_data['Day_of_Week'] = uber_data['Date'].dt.day_name()

# Explicitly specify the time format to avoid the warning
uber_data['Hour'] = pd.to_datetime(uber_data['Time'], format='%H:%M').dt.hour

# Analyze the most common days and hours for rides
popular_days = uber_data['Day_of_Week'].value_counts()

# Reorder days to emphasize Wednesday having more rides than Monday
ordered_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
popular_days = popular_days.reindex(ordered_days)

# Plotting the results
plt.figure(figsize=(12, 6))

# Plot the most popular days
plt.subplot(2, 1, 1)
popular_days.plot(kind='bar', color='skyblue')
plt.title('Most Popular Days for Uber Rides')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Rides')

# Plot the most popular hours
plt.subplot(2, 1, 2)
popular_hours = uber_data['Hour'].value_counts().sort_index()
popular_hours.plot(kind='bar', color='salmon')
plt.title('Most Popular Hours for Uber Rides')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Rides')

# Adjust layout for better presentation
plt.tight_layout()

# Show the plots
plt.show()
