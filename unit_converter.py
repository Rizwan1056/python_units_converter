import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
        "centimeters_meters": 0.01,
        "meters_centimeters": 100,
        "millimeters_meters": 0.001,
        "meters_millimeters": 1000,
        "pounds_kilograms": 0.453592,
        "kilograms_pounds": 2.20462
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        return round(value * conversions[key], 4)
    else:
        return "Conversion not supported"

st.title("🔢 Unit Converter")

st.markdown("### Convert between different units easily.")

value = st.number_input("Enter the value:", min_value=0.0, format="%.2f")
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms", "centimeters", "millimeters", "pounds"])
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms", "centimeters", "millimeters", "pounds"])

if st.button("Convert"):
    if unit_from == unit_to:
        st.warning("⚠️ Please select different units for conversion.")
    else:
        result = convert_units(value, unit_from, unit_to)
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"✅ The  converted value is **{result} {unit_to}**")
