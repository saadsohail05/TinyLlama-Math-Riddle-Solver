import streamlit as st
import requests

# Replace with your actual ngrok URL printed in Colab
API_URL = "https://aa2c-34-16-237-195.ngrok-free.app/"  

st.title("Math Riddle Solver 🤖")
st.write("Enter a math riddle, and I'll solve it for you!")

# Example riddles
example_riddles = {
    "Select an example riddle": "",
    "Simple Addition": "What is five plus three?",
    "Basic Multiplication": "If you have 4 groups of 2 apples, how many apples do you have in total?",
    "Easy Subtraction": "I have 10 candies and eat 3 of them. How many do I have left?",
    "Double Numbers": "What is double the number 6?",
    "Simple Division": "If you share 8 cookies equally between 2 friends, how many cookies does each friend get?",
}

# Example riddle selection
selected_example = st.selectbox("Try an example riddle:", list(example_riddles.keys()))

# Set the initial riddle text
riddle = st.text_area("Enter your math riddle:", value=example_riddles[selected_example], height=100)

if st.button("Solve Riddle"):
    if riddle:
        try:
            with st.spinner("Thinking..."):
                response = requests.post(f"{API_URL}/generate", json={"riddle": riddle})  # Fixed endpoint

                if response.status_code == 200:
                    solution = response.json().get("solution", "No solution found")
                    st.success("### Solution:")
                    st.write(solution)
                else:
                    st.error(f"API Error: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("⚠️ Please enter a riddle first!")
