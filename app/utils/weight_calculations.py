"""
Weight calculation and validation utilities for the logistics loader application.
"""

def calculate_net_weight(gross_weight, tare_weight):
    """
    Calculate the net weight of cargo.
    
    Args:
        gross_weight (float): The gross weight of the loaded truck in pounds
        tare_weight (float): The empty weight of the truck in pounds
        
    Returns:
        float: The calculated net weight in pounds
    """
    if gross_weight < tare_weight:
        return 0  # Prevent negative weights
    return gross_weight - tare_weight

def validate_weight_limits(gross_weight):
    """
    Validate if the gross weight is within legal limits.
    Standard US legal limit is 80,000 lbs for interstate highways.
    
    Args:
        gross_weight (float): The gross weight of the loaded truck in pounds
        
    Returns:
        tuple: (status, message) where status is a string ('COMPLIANT', 'OVERWEIGHT')
               and message is a description
    """
    LEGAL_LIMIT = 80000  # Standard US legal weight limit in pounds
    
    if gross_weight <= LEGAL_LIMIT:
        return "COMPLIANT", "Weight is within legal limits."
    else:
        overweight = gross_weight - LEGAL_LIMIT
        return "OVERWEIGHT", f"Warning: Exceeds legal limit by {overweight} lbs."

def calculate_axle_distribution(gross_weight, axle_count):
    """
    Estimate weight distribution across axles.
    
    Args:
        gross_weight (float): The gross weight of the loaded truck in pounds
        axle_count (int): Number of axles
        
    Returns:
        dict: Estimated weight per axle and compliance status
    """
    if axle_count <= 0:
        return {"error": "Invalid axle count"}
    
    # Standard axle weight limits (simplified)
    SINGLE_AXLE_LIMIT = 20000  # lbs
    TANDEM_AXLE_LIMIT = 34000  # lbs
    
    # Simple estimation model - more sophisticated models would account for 
    # load distribution, specific axle configurations, etc.
    avg_weight_per_axle = gross_weight / axle_count
    
    result = {
        "average_weight_per_axle": avg_weight_per_axle,
        "axle_count": axle_count,
        "compliance": {}
    }
    
    # Simplified compliance check
    if axle_count == 1:
        result["compliance"]["status"] = "COMPLIANT" if avg_weight_per_axle <= SINGLE_AXLE_LIMIT else "OVERWEIGHT"
        result["compliance"]["limit"] = SINGLE_AXLE_LIMIT
    else:
        # Assume tandems for simplicity 
        result["compliance"]["status"] = "COMPLIANT" if avg_weight_per_axle <= TANDEM_AXLE_LIMIT else "OVERWEIGHT"
        result["compliance"]["limit"] = TANDEM_AXLE_LIMIT
    
    return result 