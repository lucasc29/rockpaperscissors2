import streamlit as st
import numpy as random
st.title('Rock Paper Scissor Game...')

player = st.text_input("Select Rock, Paper, or Scissor :").lower()

if st.button("Begin Game"):
    computer = random.choice(["Rock 🪨", "Paper 📄", "Scissor ✄"]).lower()
    st.write("Computer selected: ", computer)
    if player == "rock" and computer == "paper":
        st.write("Computer Won... 📄 beats 🪨")
    elif player == "paper" and computer == "scissor":
        st.write("Computer Won... ✄ beats 📄")
    elif player == "scissor" and computer == "rock":
        st.write("Computer Won... 🪨 beats✄")
    elif player == computer:
        st.write("You both chose the same item")
    else:
        st.write("You beat the computer")
else:
    st.write("After typing your choice, hit enter and then the \'begin game\' button")
