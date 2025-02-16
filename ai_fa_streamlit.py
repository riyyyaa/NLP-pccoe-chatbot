import streamlit as st
from nltk.chat.util import Chat, reflections
import nltk
nltk.download('punkt')


# Define conversation pairs
pairs = [
    [r"my name is (.*)", ["Hello %1, welcome to PCCOE's IT Department! How can I assist you today?"]],
    [r"(.*)help(.*)", ["I’m here to help! You can ask about admissions, courses, faculty, placements, contact details, or the student corner."]],
    [r"what is your name?", ["I’m your PCCOE IT guide bot. How may I assist you?"]],
    [r"how are you?", ["I’m doing great and ready to help! How can I assist you today?"]],
    [r"(hi|hey|hello|hola|holla)(.*)", ["Hi there! Welcome to PCCOE's IT Department website. How can I assist you today?"]],

    # Courses and Admissions
    [r"(.*) courses (.*)|(courses)|(curriculum)", ["We offer B.Tech in IT and M.Tech in AI & Data Science."]],
    [r"(.*) admissions (.*)|(admissions)|(admission)", ["Admissions are open! Apply here: [Admissions](https://forms.zohopublic.in/pcet/form/CourseApplicationForm/formperma/Zr0u0jP3t36iheLlMd0R2qrKfxZBRs0E-U_MMRCyLM8)"]],

    # Contact and Faculty Details
    [r"(.*) contact (.*)|(contact)|(reach out)", ["You can contact us at: Email - it@pccoepune.org, Phone - +91 20 27653168. More info: [Contact Us](https://it.pccoepune.com/contact)"]],
    [r"(.*) hod (.*)|(hod)", ["Our HOD is Dr. Jayshree Katti. Learn more: [HOD Details](https://it.pccoepune.com/hod)"]],
    [r"(.*) faculty (.*)|(faculty)|(teachers)|(professors)", ["Our experienced faculty members are here to guide you. Check their profiles here: [Faculty Profiles](https://it.pccoepune.com/faculty-profile)"]],

    # Placements and Facilities
    [r"(.*) placements (.*)|(placement)|(placements)", ["We have strong placement support with top recruiters. Explore more: [Placements](https://it.pccoepune.com/placements) [Internships](https://it.pccoepune.com/internships)"]],
    [r"(.*) facilities (.*)|(facilities)", ["Our department offers state-of-the-art labs, library, and research facilities. Find out more: [Facilities](https://it.pccoepune.com/infrastructure)"]],

    # Student Corner
    [r"(.*) student corner (.*)|(student)|(student corner)", ["Visit the Student Corner for academic resources and activities: [Student Corner](https://it.pccoepune.com/stud-achievements)"]],

    # General Information
    [r"(.*) location (.*)|(location)|(address)", ["We are located near Akurdi Railway Station, Nigdi, Pune. Directions: [Location](https://www.google.com/maps/place/PCCOE+-+Pimpri+Chinchwad+College+Of+Engineering/@18.6523177,73.7486793,16z/data=!4m10!1m2!2m1!1spccoe!3m6!1s0x3bc2b9e76c8fa205:0x1b210131915734fd!8m2!3d18.6517288!4d73.7616398!15sCgVwY2NvZZIBB2NvbGxlZ2XgAQA!16s%2Fm%2F05zr96v?hl=en&entry=ttu)"]],

    # Default Response
    [r"quit", ["Goodbye! Feel free to return anytime if you need more information about PCCOE."]],
    [r"(.*)", ["I didn’t quite catch that. You can ask about admissions, courses, faculty, placements, or contact details."]]
]


# Initialize chatbot
chat = Chat(pairs, reflections)

# Streamlit App
st.title("PCCOE Chatbot")
st.write("Hi, I'm PCCOE_Chatbot and I like to chat 😊 Type your queries below to start a conversation. Type 'quit' to leave.")

# User input
user_input = st.text_input("You: ")

# Display bot response
if user_input:
    if user_input.lower() == "quit":
        st.write("Bot: Goodbye! Feel free to return anytime if you need more information about PCCOE.")
    else:
        bot_response = chat.respond(user_input)
        st.write(f"Bot: {bot_response}")
