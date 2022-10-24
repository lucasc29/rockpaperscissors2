#allows for use of streamlit API
import streamlit as st
#allows computer to choose random selection
from numpy import random

#title of the app
st.title('The Rock Paper Scissors Game')
st.caption('This is single round Rock Paper Scissors game.')

#user input box
player = str(st.text_input("Type Rock, Paper, or Scissor :")).lower()

if st.button("Begin Game"):
    # Checks input is string
    if player.isalpha():
        #checks input is from selected choices.
        if player == "rock" or player == "paper" or  player == "scissors":
            # computer randomly chooses from 3 choices
            computer = random.choice(["Rock", "Paper", "Scissor"]).lower()
            #ouputs to user the seleciton of the computer
            st.write("Computer selected: ", computer)
            #calculates winner
            if player == "rock" and computer == "paper":
                st.write("Computer Won 😔")
            elif player == "paper" and computer == "scissor":
                st.write("Computer Won 😔")
            elif player == "scissor" and computer == "rock":
                st.write("Computer Won 😔")
            elif player == computer:
                st.write("Tie 🫤")
            else:
                st.write("You Won 🎉")
                st.baloons()
        else:
            st.error("NameError : Please enter only rock, paper or scissors...")
    else:
        st.error("TypeError : Please only enter input as a string.")         
#instructs user how to use the app.
else:
    st.warning("Please type your chosen item, click the enter key and then click the begin game button.")
