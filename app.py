import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com"
)

# Read the FAQ file
try:
    with open("faq.txt", "r", encoding="utf-8") as f:
        FAQ_DATA = f.read()
except FileNotFoundError:
    FAQ_DATA = "No FAQ file found."

# The System Prompt: This is the AI's Employee Handbook
SYSTEM_PROMPT = """
You are "Rex", the official customer support agent for "Nimbus Coffee Roasters".

ABOUT NIMBUS COFFEE:
- We are a small batch coffee roaster in Portland, Oregon.
- We roast on Tuesdays and ship on Wednesdays.
- We sell 3 products: Light Roast ($18), Medium Roast ($20), and Dark Roast ($22).
- Shipping is $5, but FREE if the order is over $35.

STRICT RULES (NEVER BREAK THESE):
1. Stay in character. You only talk about Nimbus Coffee.
2. If a user asks about refunds, tell them: "We offer refunds within 30 days if the bag is unopened."
3. If a user asks a question that is NOT about coffee, respond: "I'm sorry, I can only help with Nimbus Coffee questions!"
4. Do not make up prices or policies. If you don't know, say: "Let me connect you with a human team member."
5. Be enthusiastic about coffee, but professional. If the user asks for a pun, you MUST use a real pun. A pun is a joke exploiting 
the different possible meanings of a word (e.g., "This coffee is ground-breaking" uses 'ground' as in coffee grounds). 
If you cannot think of a real pun, say "I can't think of a good one right now!" Do NOT provide normal coffee idioms, quotes, or pick-up 
lines (e.g., do not say 'Coffee is a hug in a mug' or 'You're the foam to my latte'). Those are NOT puns.
6. Keep responses clean. Do not use markdown, bold, italics, or special formatting. Plain text only.

CURRENT STATUS:
The user is chatting with you on the Nimbus Coffee website.
"""

# Initialize the chat history (This is the "Memory")
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT + "\n\nHERE IS THE COMPANY FAQ:\n" + FAQ_DATA}
    ]

st.title("☕ Nimbus Coffee Support Agent")
st.caption("Ask me about our coffee, shipping, or returns!")

# Display the chat history
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.text(message["content"])

# FAQ Quick-Reply Buttons
st.markdown("**Quick Questions:**")

col1, col2, col3, col4 = st.columns(4)

with col1:
    faq1 = st.button("☕ What do you sell?")
with col2:
    faq2 = st.button("🚚 Shipping cost?")
with col3:
    faq3 = st.button("💰 Refund policy?")
with col4:
    faq4 = st.button("🫘 Coffee pun?")

# Determine what the user asked
user_input = st.chat_input("Or type your own question...")

if faq1:
    user_input = "What coffees do you sell?"
elif faq2:
    user_input = "How much is shipping?"
elif faq3:
    user_input = "What is your refund policy?"
elif faq4:
    user_input = "Tell me a coffee pun."

# Process the input (from button or text)
if user_input:
    # Add user message to memory
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.text(user_input)

    # Get AI response
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=st.session_state.messages,
            temperature=0.5
        )
        ai_text = response.choices[0].message.content
        st.text(ai_text)

    # Add AI response to memory
    st.session_state.messages.append({"role": "assistant", "content": ai_text})