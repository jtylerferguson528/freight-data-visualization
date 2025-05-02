import streamlit as st
from datetime import datetime
from app.utils.weight_calculations import calculate_net_weight, validate_weight_limits
from app.utils.data_manager import save_entry

# Add centered title at the top
st.markdown('<h1 style="text-align: center; padding: 0rem 0; margin-top: 0; margin-bottom: 2rem;">Freight Data Entry</h1>', unsafe_allow_html=True)

# Add some explanatory text
st.markdown("""
<div style="background-color: rgba(35, 55, 75, 0.5); padding: 1rem; border-radius: 0.5rem; margin-bottom: 1.5rem;">
Use this form to enter new freight transportation data. Fields marked with * are required.
</div>
""", unsafe_allow_html=True)

with st.form("truck_data", border=False):
    # Create two main columns
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        # Use custom styling for subheaders
        st.markdown('<h3 class="subheader">Vehicle Information</h3>', unsafe_allow_html=True)
        
        # Add a bit more spacing between inputs
        vehicle_id = st.text_input("License Plate Number*", placeholder="Enter vehicle license plate")
        st.write("")  # Add space
        
        dot_number = st.text_input("DOT Number", placeholder="Enter DOT identification number")
        st.write("")  # Add space
        
        carrier_name = st.text_input("Carrier Name*", placeholder="Enter carrier/company name")
        
        st.markdown('<h3 class="subheader">Weight Information (in pounds)</h3>', unsafe_allow_html=True)
        
        # Improved number inputs with placeholders
        gross_weight = st.number_input("Gross Vehicle Weight*", 
                                     min_value=0, 
                                     max_value=200000, 
                                     help="Total weight of the loaded vehicle")
        
        tare_weight = st.number_input("Empty Truck Weight (Tare)*", 
                                    min_value=0, 
                                    max_value=100000,
                                    help="Weight of the vehicle without cargo")
        
    with col2:
        st.markdown('<h3 class="subheader">Cargo Details</h3>', unsafe_allow_html=True)
        
        # Improved selectbox
        commodity_options = ["Crude Oil", "Gasoline", "Diesel", "Natural Gas", 
                           "Jet Fuel", "Chemicals", "Lubricants", "Propane", "Other"]
        commodity_type = st.selectbox(
            "Commodity Type*",
            commodity_options,
            help="Select the type of material being transported"
        )
        
        if commodity_type == "Other":
            commodity_type = st.text_input("Specify Commodity Type", placeholder="Enter specific commodity")
            
        hazmat_class = st.selectbox(
            "Hazmat Classification",
            ["Class 1: Explosives", "Class 2: Gases", "Class 3: Flammable Liquids", 
             "Class 4: Flammable Solids", "Class 5: Oxidizing Substances", 
             "Class 6: Toxic Substances", "Class 7: Radioactive Materials",
             "Class 8: Corrosive Substances", "Class 9: Miscellaneous", "Not Applicable"],
            help="Required hazardous materials classification"
        )
        
        bol_number = st.text_input("Bill of Lading (BOL) Number", 
                                 placeholder="Enter shipping document number",
                                 help="Shipping document identifier")
        
        st.markdown('<h3 class="subheader">Driver Information</h3>', unsafe_allow_html=True)
        
        driver_name = st.text_input("Driver Name", placeholder="Enter full name of driver")
        st.write("")  # Add space
        
        driver_license = st.text_input("Driver License Number", 
                                     placeholder="Enter driver's license ID",
                                     help="State-issued driver's license ID")
    
    # Additional details section - full width
    st.markdown('<h3 class="subheader">Route & Additional Details</h3>', unsafe_allow_html=True)
    
    # Split into two columns for route information
    col3, col4 = st.columns(2)
    
    with col3:
        origin = st.text_input("Origin Location", 
                             placeholder="City, State",
                             help="Starting point of shipment")
        
        destination = st.text_input("Destination Location", 
                                  placeholder="City, State",
                                  help="Final delivery location")
        
    with col4:
        timestamp = st.date_input("Date of Weighing*", 
                                datetime.now(),
                                help="Date when weight was recorded")
        
        # Make notes field more prominent
        notes = st.text_area("Additional Notes", 
                           placeholder="Enter any special instructions or remarks about this shipment",
                           height=120)
        
    # Submit and clear buttons layout
    
    # Use a two-column layout with the submit button taking more space
    submit_col1, submit_col2 = st.columns([3, 1])
    
    with submit_col1:
        submitted = st.form_submit_button("SUBMIT SHIPMENT DATA", use_container_width=True, type="primary")
    
    with submit_col2:
        clear_form = st.form_submit_button("Clear", use_container_width=True, type="secondary")
    
    if submitted:
        # Validate inputs first
        if not vehicle_id or not carrier_name:
            st.error("Please enter all required fields (marked with *).")
        else:
            # Calculate net weight
            net_weight = calculate_net_weight(gross_weight, tare_weight)
            
            # Validate against weight limits
            weight_status, message = validate_weight_limits(gross_weight)
            
            # Create entry data
            entry = {
                "timestamp": timestamp.strftime("%Y-%m-%d"),
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
            
            # Save entry
            save_entry(entry)
            
            # Show success message with details
            st.success(f"Data submitted successfully! Net weight: {net_weight} lbs. {message}")
            st.balloons()
            
            # Add link to view data
            st.page_link("app/pages/view_data.py", label="View all data", icon="📊") 