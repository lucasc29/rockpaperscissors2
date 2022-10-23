import streamlit as st
from numpy import random

st.title('The Rock Paper Scissors Game')

player = st.text_input("Select Rock, Paper, or Scissor :").lower()


if st.button("Begin Game"):
    def check_user_input(player):
        try:
            # Convert it into integer
            val = str(input)
            st.write("Input Accepted...", val)
        except ValueError:
            try:
                # Convert it into float
                val = float(input)
                st.write("Input is a float  number. Number = ", val)
            except ValueError:
                st.write("No.. input is not number. It's a string")

check_user_input(player)


    if player == "rock" or player == "paper" or  player == "scissors":
        computer = random.choice(["Rock", "Paper", "Scissor"]).lower()
        st.write("Computer selected: ", computer)
        if player == "rock" and computer == "paper":
            st.write("Computer Won")
        elif player == "paper" and computer == "scissor":
            st.write("Computer Won")
        elif player == "scissor" and computer == "rock":
            st.write("Computer Won")
        elif player == computer:
            st.write("Tie")
        else:
            st.write("You Won")
    else:
        st.write("Please enter rock, paper or scissors...")
else:
    st.write("Please type your chosen weapon and then click the begin game button")
