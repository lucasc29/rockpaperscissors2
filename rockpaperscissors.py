#allows for use of streamlit
import streamlit as st
#allows computer to choose random selection
from numpy import random
#allows progressing "thinking" bar and code waiting
import time

#title of the app
st.title('The Rock Paper Scissors Game')
st.caption('This is single round Rock Paper Scissors game.')

#user input box
player = str(st.text_input("Type Rock, Paper, or Scissors :")).lower()

if st.button("Begin Game"):
    # Checks input is string
    if player.isalpha():
        #checks input is from selected choices.
        if player == "rock" or player == "paper" or  player == "scissors":
            # computer randomly chooses from 3 choices
            computer = random.choice(["Rock", "Paper", "Scissors"]).lower()
            #outputs computer selection
            st.write("Computer chose : ", computer)
            time.sleep(1)
            #shows the action of the game
            with st.spinner('Processing...'):
                time.sleep(1)
                time.sleep(0.5)
                st.write("Rock...")
                time.sleep(0.5)
                st.write("Paper...")
                time.sleep(0.5)
                st.write("Scissors...")
                time.sleep(1)
                st.write("...")
                time.sleep(0.5)
            st.success('GO!')
            #calculates winner
            if player == "rock" and computer == "paper":
                time.sleep(1)
                st.header("Computer Won 😔")
            elif player == "paper" and computer == "scissors":
                time.sleep(1)
                st.header("Computer Won 😔")
            elif player == "scissors" and computer == "rock":
                time.sleep(1)
                st.header("Computer Won 😔")
            elif player == computer:
                time.sleep(1)
                st.header("Tie 🫤")
            else:
                time.sleep(1)
                st.header("You Won 🎉")
                time.sleep(1)
                st.balloons()
        else:
            st.error("NameError : Please enter only rock, paper or scissors...")
    else:
        st.error("TypeError : Please only enter input as a string.")         
#instructs user how to use the app.
else:
    st.warning("Please type your chosen item, click the enter key and then click the begin game button.")
