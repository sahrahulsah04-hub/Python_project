import streamlit as st
import random

# Initialize session state
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.com_score = 0
    st.session_state.result = ""
    st.session_state.game_over = False  # New flag

st.set_page_config(page_title="Stone Paper Scissors", page_icon="🎮")
st.title("🎮 Stone Paper Scissors Game")
st.write("First to score **5 points** wins the game")

st.divider()

# Scoreboard
st.subheader("📊 Score Board")
col1, col2 = st.columns(2)
col1.metric("🙋 You", st.session_state.user_score)
col2.metric("🤖 Computer", st.session_state.com_score)

st.divider()

# Restart game button (always visible)
if st.session_state.game_over:
    if st.button("🔄 Restart Game"):
        st.session_state.user_score = 0
        st.session_state.com_score = 0
        st.session_state.result = ""
        st.session_state.game_over = False

# Only allow playing if game is not over
if not st.session_state.game_over:
    # User choice
    choice = st.radio(
        "Choose your move:",
        ("Stone 🪨", "Paper 📄", "Scissors ✂️")
    )

    play = st.button("▶️ Play")

    moves = {"Stone 🪨": 1, "Paper 📄": 2, "Scissors ✂️": 3}
    reverse_moves = {1: "Stone 🪨", 2: "Paper 📄", 3: "Scissors ✂️"}

    if play:
        user = moves[choice]
        computer = random.randint(1, 3)

        st.write(f"🙋 You chose: **{reverse_moves[user]}**")
        st.write(f"🤖 Computer chose: **{reverse_moves[computer]}**")

        # Game logic
        if user == computer:
            st.session_state.result = "😐 It's a DRAW!"
        elif (user == 1 and computer == 3) or \
             (user == 2 and computer == 1) or \
             (user == 3 and computer == 2):
            st.session_state.result = "✅ You WON this round!"
            st.session_state.user_score += 1
        else:
            st.session_state.result = "❌ Computer WON this round!"
            st.session_state.com_score += 1

        # Check if someone won the game
        if st.session_state.user_score == 5:
            st.session_state.result = "🎉 CONGRATULATIONS! You WON the game!"
            st.session_state.game_over = True
        elif st.session_state.com_score == 5:
            st.session_state.result = "🤖 Computer WON the game!"
            st.session_state.game_over = True

# Show result
st.subheader("📢 Result")
st.info(st.session_state.result)
