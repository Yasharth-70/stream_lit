import pandas as pd

# Function to calculate carbon footprint based on activity
def calculate_footprint(activity, quantity):
    # Example factors (in kg CO2e per unit)
    factors = {
        "Driving (per mile)": 0.411,
        "Electricity (per kWh)": 0.233,
        "Gas (per therm)": 0.0053
    }
    return factors.get(activity, 0) * quantity

# Main function
def main():
    # Input for family member names
    family_members_input = input("Enter family member names (comma-separated): ")
    family_members = [name.strip() for name in family_members_input.split(',') if name.strip()]

    # Dictionary to hold data
    data = {"Name": [], "Activity": [], "Quantity": [], "Footprint (kg CO2e)": []}

    # Loop to collect data
    for member in family_members:
        print(f"\nData for {member}")
        
        activity = input(f"Select activity for {member} (options: Driving (per mile), Electricity (per kWh), Gas (per therm)): ")
        quantity = float(input(f"Quantity for {member}'s {activity}: "))
        
        footprint = calculate_footprint(activity, quantity)
        data["Name"].append(member)
        data["Activity"].append(activity)
        data["Quantity"].append(quantity)
        data["Footprint (kg CO2e)"].append(footprint)
        print(f"{member}'s carbon footprint for {activity}: {footprint:.2f} kg CO2e")
    
    # Display data
    if data["Name"]:
        print("\nSummary of Carbon Footprints")
        df = pd.DataFrame(data)
        print(df.to_string(index=False))

        # Save data to CSV
        csv_filename = "carbon_footprints.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Data has been saved to {csv_filename}")

# Run the main function
if __name__ == "__main__":
    main()
