import streamlit as st
import json
import os
import random

# Memory file
MEMORY_FILE = "memory.json"

# Load memory
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

# Save memory
def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

# Fake AI (topic-based)
def ask_ai(role, topic):

    # AI REPLACE TEACHERS
    if topic == "Should AI replace teachers?":
        pro = "AI can personalize learning and provide 24/7 support to students."
        against = "AI cannot replace human emotions, mentorship, and real classroom experience."

    # SOCIAL MEDIA
    elif topic == "Is social media harmful to society?":
        pro = "Social media connects people globally and spreads awareness quickly."
        against = "It can harm mental health and spread misinformation."

    # COLLEGE DEGREE
    elif topic == "Should college degrees be mandatory for jobs?":
        pro = "Degrees ensure structured education and basic qualification standards."
        against = "Skills matter more than degrees in today’s world."

    # REMOTE WORK
    elif topic == "Is remote work better than office work?":
        pro = "Remote work gives flexibility and better work-life balance."
        against = "It reduces team collaboration and can cause isolation."

    # AI REGULATION
    elif topic == "Should governments regulate AI strictly?":
        pro = "Regulation prevents misuse and ensures safety."
        against = "Too much regulation can slow innovation."

    # TECHNOLOGY SOCIAL
    elif topic == "Is technology making people less social?":
        pro = "Technology helps people stay connected worldwide."
        against = "It reduces real-life human interaction."

    # STUDENTS AI
    elif topic == "Should students rely on AI for studying?":
        pro = "AI helps students learn faster and understand concepts."
        against = "It reduces independent thinking and creativity."

    # PRIVACY VS SECURITY
    elif topic == "Is privacy more important than security?":
        pro = "Privacy protects individual freedom and personal rights."
        against = "Security is more important to protect society from threats."

    else:
        pro = "This is a positive perspective."
        against = "This is a critical perspective."

    if role == "pro":
        return pro
    elif role == "against":
        return against
    elif role == "bias":
        return f"Bias Analysis: The debate on '{topic}' may include general assumptions and lacks diverse perspectives."
    else:
        confidence = random.randint(65, 95)
        return f"""Final Conclusion on '{topic}':
Both sides have valid arguments. A balanced approach is necessary.

Key Insights:
- Every decision has trade-offs
- Context matters
- Human judgment is important

Confidence Score: {confidence}%"""

# UI
st.set_page_config(page_title="AI Debate System")

st.title("🧠 AI Debate + Bias Reduction System")

topics = [
    "Should AI replace teachers?",
    "Is social media harmful to society?",
    "Should college degrees be mandatory for jobs?",
    "Is remote work better than office work?",
    "Should governments regulate AI strictly?",
    "Is technology making people less social?",
    "Should students rely on AI for studying?",
    "Is privacy more important than security?"
]

topic = st.selectbox("Select a debate topic:", topics)

if st.button("Run Debate"):

    memory = load_memory()

    pro = ask_ai("pro", topic)
    against = ask_ai("against", topic)
    conclusion = ask_ai("conclusion", topic)
    bias = ask_ai("bias", topic)

    # Save memory
    memory.append({
        "topic": topic,
        "conclusion": conclusion
    })
    save_memory(memory)

    st.subheader("🟢 Pro Argument")
    st.write(pro)

    st.subheader("🔴 Against Argument")
    st.write(against)

    st.subheader("⚖️ Conclusion")
    st.write(conclusion)

    st.subheader("🧠 Bias Analysis")
    st.write(bias)

    st.success("Memory updated! 🚀")