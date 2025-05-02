import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import json
import os
from app.utils.data_manager import load_entries, export_data
from app.utils.sample_data import load_sample_data

# Add centered title with more top padding to better center it
st.markdown('<h1 style="text-align: center; padding: 0rem 0; margin-top: 2.5rem; margin-bottom: 2.5rem;">Freight Data Visualization</h1>', unsafe_allow_html=True)

# Load saved entries
entries = load_entries()

if not entries:
    st.info("No data available yet. Submit your first entry using the form or load sample data.")
    
    # Sample data button
    if st.button("Load Sample Data (20 Entries)"):
        load_sample_data()
        st.success("✅ Sample data loaded successfully!")
        st.rerun()
else:
    # Convert to DataFrame for display and analysis
    df = pd.DataFrame(entries)
    
    # Add utility buttons in the sidebar
 
    st.sidebar.markdown("### Utilities")
    
    # Export options
    export_expander = st.sidebar.expander("Export")
    with export_expander:
        export_col1, export_col2 = st.columns(2)
        with export_col1:
            if st.button("CSV", use_container_width=True):
                export_path = export_data(df, format="csv")
                st.success(f"Data exported to {export_path}")
        with export_col2:
            if st.button("Excel", use_container_width=True):
                export_path = export_data(df, format="excel")
                st.success(f"Data exported to {export_path}")
    
    # Data management options
    manage_expander = st.sidebar.expander("Data")
    with manage_expander:
      
        
        manage_col1, manage_col2 = st.columns(2)
        with manage_col1:
            if st.button("🗑️", use_container_width=True):
                if st.session_state.get("confirm_clear", False):
                    # Create empty file to clear data
                    from app.utils.data_manager import DATA_FILE, ensure_dirs
                    ensure_dirs()
                    with open(DATA_FILE, 'w') as f:
                        json.dump([], f)
                    st.session_state["confirm_clear"] = False
                    st.success("All data has been cleared!")
                    st.rerun()
                else:
                    st.session_state["confirm_clear"] = True
                    st.warning("⚠️ Are you sure? Click again to confirm.")
        
        with manage_col2:
            if st.button("🔄", use_container_width=True):
                load_sample_data()
                st.success("✅ Data replaced with fresh sample data!")
                st.rerun()
    
    # Move filters to sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Filters")
    
    # Filter by carrier
    carrier_filter = "All"
    if "carrier_name" in df.columns:
        carriers = ["All"] + sorted(df["carrier_name"].unique().tolist())
        carrier_filter = st.sidebar.selectbox("Carrier Name", carriers)
    
    # Filter by weight status - make dynamic
    status_filter = "All"
    if "weight_status" in df.columns:
        status_options = ["All"] + sorted(df["weight_status"].unique().tolist())
        status_filter = st.sidebar.selectbox("Weight Status", status_options)
    
    # Filter by commodity
    commodity_filter = "All"
    if "commodity_type" in df.columns:
        commodities = ["All"] + sorted(df["commodity_type"].unique().tolist())
        commodity_filter = st.sidebar.selectbox("Commodity Type", commodities)
    
    # Add hazmat class filter
    hazmat_filter = "All"
    if "hazmat_class" in df.columns:
        hazmat_options = ["All"] + sorted(df["hazmat_class"].unique().tolist())
        hazmat_filter = st.sidebar.selectbox("Hazmat Classification", hazmat_options)
    
    # Origin filter
    origin_filter = "All"
    if "origin" in df.columns:
        origin_options = ["All"] + sorted(df["origin"].unique().tolist())
        origin_filter = st.sidebar.selectbox("Origin", origin_options)
    
    # Date range filter
    date_range = [datetime.now() - timedelta(days=30), datetime.now()]
    if "timestamp" in df.columns:
        date_range = st.sidebar.date_input(
            "Date Range",
            value=[
                df["timestamp"].min() if len(df) > 0 else datetime.now() - timedelta(days=30),
                df["timestamp"].max() if len(df) > 0 else datetime.now()
            ],
            key="date_range"
        )
    
    # Free text search
    search_text = st.sidebar.text_input("Search in all fields", "")
    
    # Apply filters to DataFrame
    filtered_df = df.copy()
    
    # Carrier filter
    if "carrier_name" in df.columns and carrier_filter != "All":
        filtered_df = filtered_df[filtered_df["carrier_name"] == carrier_filter]
    
    # Weight status filter
    if "weight_status" in df.columns and status_filter != "All":
        filtered_df = filtered_df[filtered_df["weight_status"] == status_filter]
    
    # Commodity filter
    if "commodity_type" in df.columns and commodity_filter != "All":
        filtered_df = filtered_df[filtered_df["commodity_type"] == commodity_filter]
    
    # Hazmat filter
    if "hazmat_class" in df.columns and hazmat_filter != "All":
        filtered_df = filtered_df[filtered_df["hazmat_class"] == hazmat_filter]
    
    # Origin filter
    if "origin" in df.columns and origin_filter != "All":
        filtered_df = filtered_df[filtered_df["origin"] == origin_filter]
    
    # Date range filter
    if "timestamp" in df.columns and len(date_range) == 2:
        filtered_df = filtered_df[
            (filtered_df["timestamp"] >= date_range[0].strftime("%Y-%m-%d")) &
            (filtered_df["timestamp"] <= date_range[1].strftime("%Y-%m-%d"))
        ]
    
    # Text search
    if search_text:
        text_match = False
        for col in filtered_df.columns:
            if filtered_df[col].astype(str).str.contains(search_text, case=False).any():
                text_match = True
                filtered_df = filtered_df[filtered_df[col].astype(str).str.contains(search_text, case=False)]
                break
    
    # Data visualizations
    if len(filtered_df) > 0:
        
        tab1, tab2, tab3 = st.tabs(["Weight Analysis", "Carrier Analysis", "Time Trends"])
        
        with tab1:
            # Weight distribution by commodity type
            container1 = st.container()
            with container1:
                fig1 = px.box(filtered_df, x="commodity_type", y="gross_weight", 
                             title="Gross Weight Distribution by Commodity Type",
                             color="commodity_type",
                             labels={"commodity_type": "Commodity Type", "gross_weight": "Gross Weight (lbs)"},
                             color_discrete_sequence=px.colors.qualitative.Bold)
                fig1.update_layout(showlegend=False)  # Hide legend as it's redundant
                st.plotly_chart(fig1, use_container_width=True)

            # Net Weight Histogram
            container_hist = st.container()
            with container_hist:
                fig_hist = px.histogram(filtered_df, x="net_weight", 
                                        title="Distribution of Net Weights",
                                        labels={"net_weight": "Net Weight (lbs)", "count": "Frequency"},
                                        color_discrete_sequence=["#2E86C1"])  # Blue color
                fig_hist.update_traces(marker_line_color="white", marker_line_width=0.5)
                fig_hist.update_layout(bargap=0.1)  # Add gaps between bars
                st.plotly_chart(fig_hist, use_container_width=True)

            # Weight status pie chart
            container2 = st.container()
            with container2:
                status_counts = filtered_df["weight_status"].value_counts().reset_index()
                status_counts.columns = ["Status", "Count"]
                # Custom colors: Green for compliant, Red for overweight
                status_colors = {"COMPLIANT": "#27AE60", "OVERWEIGHT": "#E74C3C"}
                color_map = [status_colors.get(status, "#3498DB") for status in status_counts["Status"]]
                fig_pie = px.pie(status_counts, values="Count", names="Status", 
                               title="Weight Compliance Distribution",
                               color_discrete_sequence=color_map)
                fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                fig_pie.update_layout(legend_title_text="Status")
                st.plotly_chart(fig_pie, use_container_width=True)
        
        with tab2:
            # Number of trips by carrier
            container3 = st.container()
            with container3:
                carrier_counts = filtered_df["carrier_name"].value_counts().reset_index()
                carrier_counts.columns = ["Carrier", "Count"]
                fig2 = px.bar(carrier_counts, x="Carrier", y="Count", 
                             title="Number of Trips by Carrier",
                             labels={"Count": "Number of Trips"},
                             color="Carrier",
                             color_discrete_sequence=px.colors.qualitative.Pastel)
                fig2.update_layout(showlegend=False)  # Hide legend as it's redundant
                st.plotly_chart(fig2, use_container_width=True)
            
            # Average weight by carrier
            container4 = st.container()
            with container4:
                carrier_weights = filtered_df.groupby("carrier_name")["gross_weight"].mean().reset_index()
                carrier_weights.columns = ["Carrier", "Average Weight (lbs)"]
                fig_avg = px.bar(carrier_weights, x="Carrier", y="Average Weight (lbs)",
                               title="Average Gross Weight by Carrier",
                               color="Carrier",
                               color_discrete_sequence=px.colors.sequential.Viridis)
                fig_avg.update_layout(showlegend=False)  # Hide legend as it's redundant
                st.plotly_chart(fig_avg, use_container_width=True)
        
        with tab3:
            # Timeline of weights
            if len(filtered_df) > 1:
                container5 = st.container()
                with container5:
                    df_time = filtered_df.copy()
                    df_time['timestamp'] = pd.to_datetime(df_time['timestamp'])
                    df_time = df_time.sort_values('timestamp')
                    fig3 = px.line(df_time, x="timestamp", y="gross_weight", 
                                  title="Gross Weight Over Time",
                                  markers=True,  # Add markers to line
                                  labels={"timestamp": "Date", "gross_weight": "Gross Weight (lbs)"},
                                  color_discrete_sequence=["#1E88E5"])  # Dark blue
                    fig3.update_traces(line=dict(width=3))  # Make line thicker
                    fig3.update_layout(xaxis_title="Date", yaxis_title="Gross Weight (lbs)")
                    st.plotly_chart(fig3, use_container_width=True)
                
                # Trips over time
                container6 = st.container()
                with container6:
                    trips_by_date = df_time.groupby('timestamp').size().reset_index()
                    trips_by_date.columns = ['Date', 'Number of Trips']
                    fig_trips = px.bar(trips_by_date, x='Date', y='Number of Trips',
                                      title='Number of Trips by Date',
                                      color_discrete_sequence=["#FF9800"])  # Orange
                    fig_trips.update_layout(xaxis_title="Date", yaxis_title="Trip Count")
                    st.plotly_chart(fig_trips, use_container_width=True)
    
    # Show filtered data
    st.markdown('<h3 class="subheader">All Records</h3>', unsafe_allow_html=True)
    
    # Create a copy of the dataframe with human-readable column names
    display_df = filtered_df.copy()
    
    # Define human-readable column names mapping
    column_mapping = {
        "timestamp": "Date",
        "vehicle_id": "Vehicle ID",
        "dot_number": "DOT Number",
        "carrier_name": "Carrier Name",
        "gross_weight": "Gross Weight (lbs)",
        "tare_weight": "Tare Weight (lbs)",
        "net_weight": "Net Weight (lbs)",
        "commodity_type": "Commodity Type",
        "hazmat_class": "Hazmat Classification",
        "bol_number": "Bill of Lading Number",
        "driver_name": "Driver Name",
        "driver_license": "Driver License",
        "origin": "Origin",
        "destination": "Destination",
        "weight_status": "Weight Status",
        "notes": "Notes"
    }
    
    # Rename the columns
    display_df.rename(columns=column_mapping, inplace=True)
    
    # Display the dataframe with human-readable column names
    st.dataframe(display_df)
    st.write(f"Showing {len(filtered_df)} of {len(df)} records") 