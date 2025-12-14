import streamlit as st

st.title("🤖 AI Assistant")

st.caption("Ask questions about Cybersecurity, Data Science, or IT Operations")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask the AI something...")

def ai_response(question: str) -> str:
    q = question.lower()

    # Cybersecurity
    if "phishing" in q:
        return (
            "📧 **Cybersecurity Insight:**\n\n"
            "There is a spike in phishing incidents. These cases typically remain open longer "
            "than other incident types, indicating an incident response bottleneck. "
            "Recommendation: Prioritise phishing triage or automate email analysis."
        )

    # Data Science
    if "dataset" in q or "data" in q:
        return (
            "📊 **Data Science Insight:**\n\n"
            "IT-owned datasets consume more storage than HR datasets. "
            "Large log datasets should be archived or compressed to reduce resource usage. "
            "This supports better data governance."
        )

    # IT Operations
    if "ticket" in q or "it" in q:
        return (
            "🛠 **IT Operations Insight:**\n\n"
            "The 'Open' ticket status causes the biggest delay. "
            "Staff member Alex is handling the most tickets, suggesting workload imbalance. "
            "Recommendation: Redistribute tickets or improve workflow at the Open stage."
        )

    # Fallback
    return (
        "🤖 I can help analyse:\n"
        "- Cybersecurity incidents\n"
        "- Dataset governance\n"
        "- IT service desk performance\n\n"
        "Try asking about phishing, datasets, or IT tickets."
    )

# Handle input
if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response
    response = ai_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)