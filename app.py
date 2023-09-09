"""
This module contains the main application for the Conversational UAV Explorer.
"""

import time
import openai
import streamlit as st
import pydeck as pdk
from audiorecorder import audiorecorder
from uav_client import parse_command, send_command
from prompts import PROMPT_CHAT_RESPONSE
from fewshot import FewShot4UAVs

fewshot = FewShot4UAVs()
SERVER_URL = ""

UAV_STATUS = {
    "Taking off": "green",
    "On the way": "green",
    "Landing": "red"
}


def initialize_session():
    """Initializes the session state."""
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system",
                                      "content": PROMPT_CHAT_RESPONSE,
                                      "name": "System"}]


def set_page_configuration():
    """Sets the page configuration for the website."""
    st.set_page_config(page_title="UAV Explorer")
    st.title("🚁 Conversational UAV Explorer")


def get_audio_transcript(audio):
    """
    Retrieves the transcript from the recording

    :param audio: audio file
    :type audio: audio_file
    :return: transcript of the audio
    :rtype: str
    """
    with open(audio, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        user_transcript = transcript["text"]
        st.session_state.messages.append({"role": "user",
                                          "content": user_transcript,
                                          "name": "Operator"})
    return user_transcript


def get_uav_command(user_transcript):
    """
    Retrieves the UAV command from the user transcript

    :param user_transcript: transcript of the user's audio
    :type user_transcript: str
    :return: UAV command
    :rtype: str
    """
    uav_command = fewshot.get_command(user_transcript)
    st.session_state.messages.append({"role": "function",
                                      "content": uav_command,
                                      "name": "UAV"})
    return uav_command


def get_uav_response():
    """
    Get the UAV response.

    :return: UAV response
    :rtype: str
    """
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=st.session_state.messages)
    uav_response = response["choices"][0]["message"]["content"]
    st.session_state.messages.append({"role": "assistant",
                                      "content": uav_response,
                                      "name": "Assistant"})
    return uav_response


def transcribe(audio):
    """
    Transcribe the audio and send the command to the UAV.

    :param audio: audio file
    :type audio: audio_file
    :return: none
    """
    user_transcript = get_audio_transcript(audio)
    uav_command = get_uav_command(user_transcript)
    get_uav_response()

    if SERVER_URL:
        command, location = parse_command(uav_command)
        send_command(SERVER_URL, command, location)
    else:
        pass

    display_latest_messages()


def text_delay(prefix, message):
    """
    Display the message with a live texting effect.

    :param prefix: role of the person typing.
    :type prefix: str
    :param message: message
    :type message: str
    """
    placeholder = st.empty()
    response = prefix
    for chunk in message.split():
        response += chunk + " "
        time.sleep(0.05)
        placeholder.markdown(response + "▌")
    placeholder.markdown(response)


def display_latest_messages():
    """Display latest messages in the chat"""
    for message in st.session_state.messages[-3:]:
        role = message["role"]
        content = message["content"]
        prefix = f"**{message['name']}**: "

        if role == "user":
            with st.chat_message("user"):
                text_delay(prefix, content)
        elif role == "function":
            with st.chat_message("UAV", avatar="🚁"):
                text_delay(prefix, content)
        elif role == "assistant":
            with st.chat_message("assistant"):
                text_delay(prefix, content)


def record_button():
    """Display the record button and transcribe the audio"""
    audio = audiorecorder("Start Voice Command", "End Voice Command")
    if len(audio) > 0:
        audio_filename = "temp_audio.wav"
        with open(audio_filename, "wb") as wav_file:
            wav_file.write(audio.tobytes())
        transcribe(audio_filename)


def display_sidebar():
    """Display the sidebar"""
    with st.sidebar:
        st.subheader("Instructions")
        st.write("1. Click on *Start Voice Command* to record a command.\n"
                 "2. Once you're done saying a command, click *End Voice Command*.")

        st.subheader("Commands")
        st.write("- Go to <location>\n"
                 "- Take a picture of <description>\n"
                 "- Land\n"
                 "- Take off")

        st.subheader("Examples")
        st.write("- Take a picture of the second floor of the green house on W Grace St.\n"
                 "- Go to the Chick-fil-A on W Broad St.\n"
                 "- Check out the Edgar Allan Poe Museum in Richmond.\n"
                 "- Snap a photo of James Madison's Montpelier.\n"
                 "- Head to Roots Natural Kitchen in Charlottesville, VA.")


def display_main_tab():
    """Display the main tab where the conversational UAV is running"""
    global SERVER_URL
    SERVER_URL = st.text_input("Server URL",
                               key="uav_server_url",
                               placeholder="http://127.0.0.1:8080")
    with st.chat_message("assistant"):
        st.write("**Assistant**: Where would you like me to go today?")

    with st.spinner("Fetching command..."):
        record_button()


def display_history_tab():
    """Display entire transcript of the chat"""
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]
        prefix = f"**{message['name']}**: "

        if role == "user":
            st.write(prefix, content)
        elif role == "function":
            st.write(prefix, content)
        elif role == "assistant":
            st.write(prefix, content + "\n\n")


def display_map_tab():
    """Display the map tab with details about the UAV"""
    st.subheader("Satellite")
    map_data = pdk.Deck(
        map_style="mapbox://styles/mapbox/satellite-streets-v11",
        initial_view_state={
            "latitude": 37.541290,
            "longitude": -77.434769,
            "zoom": 11,
            "pitch": 25,
        },
        layers=[],
    )
    st.pydeck_chart(map_data)

    st.subheader("UAV Status")
    st.text("Battery: 80%")
    st.text("Altitude: 1000 ft")
    st.text("Speed: 15 mph")


def display_logo():
    """Display the logos in the footer"""
    logo = """
        <style>
            .footer {
                position: relative;
                bottom: 0;
                left: 0;
                width: 100%;
                text-align: center;
                padding: 40px;
            }
        </style>

        <div class="footer">
            <img src="https://i.imgur.com/j46TmcD.png" width=200>
            <span style="font-size: 35px; margin: 0px 0px 0px 30px;">×</span>
            <img src="https://i.imgur.com/tWq1v4N.png" width=190>
        </div>
    """
    st.markdown(logo, unsafe_allow_html=True)


def main():
    """Runs the entire application"""
    initialize_session()
    set_page_configuration()
    display_sidebar()

    main_tab, history_tab, map_tab = st.tabs(["Main", "History", "Map"])
    with main_tab:
        display_main_tab()
    with history_tab:
        display_history_tab()
    with map_tab:
        display_map_tab()

    display_logo()


if __name__ == '__main__':
    main()
