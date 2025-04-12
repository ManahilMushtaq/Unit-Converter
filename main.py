import streamlit as st

def unit_converter():
    st.title("📏 Simple Unit Converter")
    st.subheader("Convert between Meters and Feet")

    options = ["Meters to Feet", "Feet to Meters"]
    choice = st.selectbox("Choose conversion type:", options)

    value = st.number_input("Enter the value to convert:", format="%.4f")

    if st.button("Convert"):
        if choice == "Meters to Feet":
            result = value * 3.28084
            st.success(f"{value} meters is equal to {result:.2f} feet")
        elif choice == "Feet to Meters":
            result = value / 3.28084
            st.success(f"{value} feet is equal to {result:.2f} meters")

if __name__ == "__main__":
    unit_converter()

