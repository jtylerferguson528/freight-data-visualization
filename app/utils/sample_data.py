"""
Sample data generator for testing the logistics loader application.
Provides a variety of realistic truck and cargo data entries.
"""

from datetime import datetime, timedelta
import random

def generate_sample_data():
    """
    Generate 40 diverse sample data entries for testing.
    
    Returns:
        list: List of sample data entries as dictionaries
    """
    # Base date for entries (today minus 40 days)
    base_date = datetime.now() - timedelta(days=40)
    
    # Fictional carriers in the logistics industry
    carriers = [
        "NorthStar Logistics",
        "Blue Ridge Transport",
        "Golden Valley Hauling",
        "Sunset Freight Systems",
        "Mountain Peak Carriers",
        "Eagle Express Logistics",
        "Silver Arrow Transport",
        "Horizon Hauling Co.",
        "Pinnacle Shipping Ltd.",
        "Evergreen Freight Lines",
        "Atlas Cargo Solutions",
        "RedRock Transport",
        "Harbor Freight Systems",
        "Summit Logistics Group",
        "Falcon Tankers Inc.",
        "Vista Shipping Services",
        "Cascade Transport Co.",
        "Delta Logistics Corp.",
        "Voyager Freight Network",
        "Meridian Shipping LLC"
    ]
    
    # Weight carriers so some appear more frequently than others
    carrier_weights = {}
    # Major carriers (appear more frequently)
    for carrier in carriers[:5]:
        carrier_weights[carrier] = 0.15  # 15% chance each
    # Medium carriers
    for carrier in carriers[5:10]:
        carrier_weights[carrier] = 0.08  # 8% chance each
    # Smaller carriers
    for carrier in carriers[10:]:
        carrier_weights[carrier] = 0.03  # 3% chance each
    
    # Normalize weights to ensure they sum to 1
    total_weight = sum(carrier_weights.values())
    carrier_items = list(carrier_weights.items())
    carrier_names = [item[0] for item in carrier_items]
    carrier_probabilities = [item[1]/total_weight for item in carrier_items]
    
    # Commodity types for oil and gas
    commodities = [
        "Crude Oil",
        "Gasoline",
        "Diesel",
        "Natural Gas",
        "Jet Fuel",
        "Lubricants",
        "Propane",
        "Chemicals",
        "Drilling Fluids",
        "Asphalt",
        "Ethanol",
        "Biodiesel",
        "Kerosene",
        "Petroleum Jelly",
        "Mineral Oil"
    ]
    
    # Weight commodities so some appear more frequently
    commodity_weights = {
        "Crude Oil": 0.2,
        "Gasoline": 0.18,
        "Diesel": 0.15,
        "Natural Gas": 0.12,
        "Chemicals": 0.1
    }
    # Add lower weights for remaining commodities
    for commodity in commodities:
        if commodity not in commodity_weights:
            commodity_weights[commodity] = 0.025
    
    # Normalize weights
    total_commodity_weight = sum(commodity_weights.values())
    commodity_items = list(commodity_weights.items())
    commodity_names = [item[0] for item in commodity_items]
    commodity_probabilities = [item[1]/total_commodity_weight for item in commodity_items]
    
    # Hazmat classifications
    hazmat_classes = [
        "Class 1: Explosives",
        "Class 2: Gases",
        "Class 3: Flammable Liquids",
        "Class 4: Flammable Solids",
        "Class 5: Oxidizing Substances",
        "Class 6: Toxic Substances",
        "Class 7: Radioactive Materials",
        "Class 8: Corrosive Substances",
        "Class 9: Miscellaneous",
        "Not Applicable"
    ]
    
    # Common origins for oil products
    origins = [
        "Houston, TX",
        "Midland, TX",
        "Odessa, TX",
        "Bakersfield, CA",
        "Cushing, OK",
        "Williston, ND",
        "New Orleans, LA",
        "Anchorage, AK",
        "Calgary, AB",
        "Corpus Christi, TX",
        "San Antonio, TX",
        "Tulsa, OK",
        "Casper, WY",
        "Baton Rouge, LA",
        "Edmonton, AB"
    ]
    
    # Common destinations
    destinations = [
        "Los Angeles, CA",
        "Chicago, IL",
        "New York, NY",
        "Seattle, WA",
        "Denver, CO",
        "Phoenix, AZ",
        "Philadelphia, PA",
        "Kansas City, MO",
        "Dallas, TX",
        "Atlanta, GA",
        "Portland, OR",
        "Miami, FL",
        "Boston, MA",
        "Minneapolis, MN",
        "Salt Lake City, UT"
    ]
    
    # Generate 40 diverse entries
    entries = []
    
    # Create a schedule to make some dates have multiple entries
    # This will create clusters of entries on certain dates
    date_multiplier = {}
    busy_days = random.sample(range(40), 10)  # 10 random busy days
    for day in busy_days:
        date_multiplier[day] = random.randint(2, 3)  # 2-3 entries on busy days
    
    entry_count = 0
    day_index = 0
    
    while entry_count < 40:
        # Get number of entries for this day
        entries_for_today = date_multiplier.get(day_index, 1)
        
        for _ in range(entries_for_today):
            if entry_count >= 40:
                break
                
            # Create date
            entry_date = base_date + timedelta(days=day_index)
            entry_date_str = entry_date.strftime("%Y-%m-%d")
            
            # Generate vehicle info
            vehicle_id = f"{random.choice('ABCDEFGH')}{random.choice('ABCDEFGH')}{random.randint(100, 999)}"
            dot_number = f"{random.randint(10000, 99999)}"
            
            # Use weighted random selection for carriers
            carrier_name = random.choices(carrier_names, weights=carrier_probabilities)[0]
            
            # Generate weight info (lbs)
            tare_weight = random.randint(25000, 35000)  # Empty truck weight
            
            # Mix of compliant and overweight trucks
            if random.random() < 0.15:  # 15% chance of being overweight
                gross_weight = random.randint(80001, 90000)  # Overweight
            else:
                gross_weight = random.randint(tare_weight + 10000, 80000)  # Legal weight
                
            net_weight = gross_weight - tare_weight
            
            # Generate cargo info - use weighted random selection
            commodity_type = random.choices(commodity_names, weights=commodity_probabilities)[0]
            
            # Assign appropriate hazmat class based on commodity
            if commodity_type in ["Crude Oil", "Gasoline", "Diesel", "Jet Fuel"]:
                hazmat_class = "Class 3: Flammable Liquids"
            elif commodity_type == "Natural Gas" or commodity_type == "Propane":
                hazmat_class = "Class 2: Gases"
            elif commodity_type == "Chemicals":
                hazmat_class = random.choice(["Class 6: Toxic Substances", "Class 8: Corrosive Substances"])
            else:
                hazmat_class = random.choice(hazmat_classes)
                
            bol_number = f"BOL-{random.randint(100000, 999999)}"
            
            # Generate driver info (with recognizable patterns)
            first_names = ["John", "James", "Robert", "Michael", "William", "David", "Richard", "Charles", "Joseph", "Thomas",
                          "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen",
                          "Daniel", "Matthew", "Anthony", "Mark", "Steven", "Paul", "Andrew", "Kenneth", "Joshua", "Kevin",
                          "Lisa", "Nancy", "Margaret", "Sandra", "Ashley", "Emily", "Donna", "Michelle", "Amanda", "Stephanie"]
            last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
                         "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
                         "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King",
                         "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter"]
            
            driver_name = f"{random.choice(first_names)} {random.choice(last_names)}"
            driver_license = f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(10000000, 99999999)}"
            
            # Generate route info
            origin = random.choice(origins)
            destination = random.choice(destinations)
            
            # Generate additional info
            weight_status = "OVERWEIGHT" if gross_weight > 80000 else "COMPLIANT"
            notes = ""
            
            # Add some specific notes for certain conditions
            if weight_status == "OVERWEIGHT":
                notes = "Requires overweight permit. Driver notified of compliance issue."
            elif "Chemicals" in commodity_type:
                notes = "Requires special handling. Safety data sheet verified."
            elif random.random() < 0.3:  # 30% chance of a random note
                random_notes = [
                    "Driver requested scale ticket.",
                    "Truck inspected before weighing.",
                    "Delayed due to equipment issues.",
                    "Second weigh required for verification.",
                    "New driver, provided additional instruction.",
                    "Routine inspection completed.",
                    "Bypass lane used for weigh-in.",
                    "Driver reported faulty fuel gauge.",
                    "Pre-trip inspection passed.",
                    "Load secured with additional straps."
                ]
                notes = random.choice(random_notes)
            
            # Create the entry
            entry = {
                "timestamp": entry_date_str,
                "vehicle_id": vehicle_id,
                "dot_number": dot_number,
                "carrier_name": carrier_name,
                "gross_weight": gross_weight,
                "tare_weight": tare_weight,
                "net_weight": net_weight,
                "commodity_type": commodity_type,
                "hazmat_class": hazmat_class,
                "bol_number": bol_number,
                "driver_name": driver_name,
                "driver_license": driver_license,
                "origin": origin,
                "destination": destination,
                "weight_status": weight_status,
                "notes": notes
            }
            
            entries.append(entry)
            entry_count += 1
        
        day_index += 1
    
    return entries

def load_sample_data():
    """
    Load sample data into the application's data store.
    First clears any existing data to ensure a fresh dataset with only fictional companies.
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        from app.utils.data_manager import save_entry, DATA_FILE, ensure_dirs
        import json
        
        # Clear existing data first
        ensure_dirs()
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
        
        # Generate sample entries
        entries = generate_sample_data()
        
        # Save each entry
        for entry in entries:
            save_entry(entry)
            
        return True
    except Exception as e:
        print(f"Error loading sample data: {e}")
        return False

if __name__ == "__main__":
    # When run directly, print sample data for testing
    from pprint import pprint
    
    sample_data = generate_sample_data()
    print(f"Generated {len(sample_data)} sample entries:")
    pprint(sample_data[0])  # Print the first entry as an example 