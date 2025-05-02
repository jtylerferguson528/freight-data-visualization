"""
Tests for the weight_calculations module.
"""

import pytest
from app.utils.weight_calculations import calculate_net_weight, validate_weight_limits, calculate_axle_distribution

class TestWeightCalculations:
    """Test cases for weight calculation functions."""
    
    def test_calculate_net_weight_positive(self):
        """Test that net weight calculation returns the expected value for valid inputs."""
        gross_weight = 80000
        tare_weight = 30000
        expected = 50000
        
        result = calculate_net_weight(gross_weight, tare_weight)
        
        assert result == expected
    
    def test_calculate_net_weight_negative_case(self):
        """Test that net weight calculation returns 0 when gross weight < tare weight."""
        gross_weight = 20000
        tare_weight = 30000
        expected = 0
        
        result = calculate_net_weight(gross_weight, tare_weight)
        
        assert result == expected
    
    def test_validate_weight_limits_compliant(self):
        """Test that weight validation returns compliant for legal weights."""
        gross_weight = 75000
        
        status, message = validate_weight_limits(gross_weight)
        
        assert status == "COMPLIANT"
        assert "within legal limits" in message
    
    def test_validate_weight_limits_overweight(self):
        """Test that weight validation returns overweight for illegal weights."""
        gross_weight = 85000
        overweight = gross_weight - 80000
        
        status, message = validate_weight_limits(gross_weight)
        
        assert status == "OVERWEIGHT"
        assert f"Exceeds legal limit by {overweight}" in message
    
    def test_calculate_axle_distribution_single_axle(self):
        """Test axle distribution for single axle."""
        gross_weight = 18000
        axle_count = 1
        
        result = calculate_axle_distribution(gross_weight, axle_count)
        
        assert result["average_weight_per_axle"] == 18000
        assert result["compliance"]["status"] == "COMPLIANT"
    
    def test_calculate_axle_distribution_multiple_axles(self):
        """Test axle distribution for multiple axles."""
        gross_weight = 80000
        axle_count = 5
        expected_avg = 16000
        
        result = calculate_axle_distribution(gross_weight, axle_count)
        
        assert result["average_weight_per_axle"] == expected_avg
        assert result["compliance"]["status"] == "COMPLIANT"
    
    def test_calculate_axle_distribution_invalid_axle_count(self):
        """Test axle distribution with invalid axle count."""
        gross_weight = 80000
        axle_count = 0
        
        result = calculate_axle_distribution(gross_weight, axle_count)
        
        assert "error" in result 