import streamlit as st

# Title
st.markdown("<h1 style='text-align:center; color:#4B8BBE;'>🔄 Universal Unit Converter</h1>", unsafe_allow_html=True)

# Updated category with clearer emojis
categories = {
    "📐 Length": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
    "⏱ Time": ["Seconds", "Minutes", "Hours", "Days", "Months"],
    "🏋️‍♂️ Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "🌡 Temperature": ["Celsius", "Fahrenheit", "Kelvin"],

}

# Category selection
selected_category = st.radio("🔍 Choose a Category", list(categories.keys()), horizontal=True)

# Unit selection
from_unit = st.selectbox("🔄 Convert from", categories[selected_category])
to_unit = st.selectbox("➡️ Convert to", categories[selected_category])

# Input value
value = st.number_input("🔢 Enter Value", min_value=0.0, format="%.2f")

# Conversion function
def convert(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": {"Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084, "Inches": 39.3701},
        "Kilometers": {"Meters": 1000, "Miles": 0.621371, "Feet": 3280.84, "Inches": 39370.1},
        "Miles": {"Meters": 1609.34, "Kilometers": 1.60934, "Feet": 5280, "Inches": 63360},
        "Feet": {"Meters": 0.3048, "Kilometers": 0.0003048, "Miles": 0.000189394, "Inches": 12},
        "Inches": {"Meters": 0.0254, "Kilometers": 0.0000254, "Miles": 0.000015783, "Feet": 0.0833333},

        "Kilograms": {"Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274},
        "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
        "Pounds": {"Kilograms": 0.453592, "Grams": 453.592, "Ounces": 16},
        "Ounces": {"Kilograms": 0.0283495, "Grams": 28.3495, "Pounds": 0.0625},

        "Celsius": {"Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15},
        "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5/9, "Kelvin": lambda f: (f - 32) * 5/9 + 273.15},
        "Kelvin": {"Celsius": lambda k: k - 273.15, "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32},

                "Seconds": {"Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400, "Months": 1/2629743.83},
        "Minutes": {"Seconds": 60, "Hours": 1/60, "Days": 1/1440, "Months": 1/43829.1},
        "Hours": {"Seconds": 3600, "Minutes": 60, "Days": 1/24, "Months": 1/730.484},
        "Days": {"Seconds": 86400, "Minutes": 1440, "Hours": 24, "Months": 1/30.44},
        "Months": {"Seconds": 2629743.83, "Minutes": 43829.1, "Hours": 730.484, "Days": 30.44}

    }

    if from_unit == to_unit:
        return value
    elif callable(conversion_factors.get(from_unit, {}).get(to_unit)):
        return conversion_factors[from_unit][to_unit](value)
    else:
        return value * conversion_factors.get(from_unit, {}).get(to_unit, 1)

# Convert button
if st.button("🚀 Convert Now"):
    result = convert(value, from_unit, to_unit)
    st.markdown(
        f"<div style='padding: 10px; background-color: #f0f2f6; border-radius: 10px; text-align: center; color: #333;'>"
        f"<h3>{value} {from_unit} = <span style='color:#007ACC;'>{result:.6f} {to_unit}</span></h3>"
        "</div>",
        unsafe_allow_html=True
    )

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>🛠️ Crafted with ❤️ by <strong>Dureshehwar Siddiqui</strong></p>", unsafe_allow_html=True)
