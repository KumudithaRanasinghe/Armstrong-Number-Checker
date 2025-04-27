import streamlit as st

# Title
st.title("Armstrong Number Checker")

# User input
number = st.number_input("Enter a number:", min_value=1, step=1, format="%d")

# When button is clicked
if st.button("Check Armstrong Number"):
    length = len(str(number))
    temp = number
    sum = 0
    steps = ""
    
    while temp > 0:
        digit = temp % 10
        sum += digit ** length
        steps += f"Digit: {digit}^{length} = {digit ** length}\n"
        temp = temp // 10
    
    # Show calculation steps
    st.text_area("Calculation Steps", steps.strip(), height=200)
    
    # Show result
    st.write(f"### Number is {number} and sum is {sum}")
    
    # Final result
    if sum == number:
        st.success(f"✅ {number} is an Armstrong Number!")
    else:
        st.error(f"❌ {number} is NOT an Armstrong Number.")