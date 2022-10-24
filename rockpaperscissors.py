import streamlit as st
from numpy import random

st.title('The Rock Paper Scissors Game')
st.caption('This is single round Rock Paper Scissors game.')

player = st.text_input("Type Rock, Paper, or Scissor :").lower()

if st.button("Begin Game"):
    try:
        scraped_data = urllib.request.urlopen(title)
    except ValueError:
        st.error(‘Please enter a valid input’)

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
        st.write("Input Error : Please enter only rock, paper or scissors...")
else:
    st.write("Please type your chosen item and then click the begin game button")
