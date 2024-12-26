# Midterm 4.3
# Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, 
# create an application that displays the number of millimeters that the ocean will have risen each year for the next 10 years.  


# Define the annual rise rate in millimeters
rise_rate_per_year = 1.6

# Display the ocean level rise for the next 10 years
print("Year\tRise (mm)")
print("----------------")

for year in range(1, 11):  # Loop through the next 10 years
    rise = year * rise_rate_per_year
    print(f"{year}\t{rise:.1f}")
