import openai
import streamlit as st
from command_handler import parse_command, send_command
from prompts import prompt_chat_response
from fewshot import FewShot4UAVs
from audiorecorder import audiorecorder
import pydeck as pdk
import time

fewshot = FewShot4UAVs()


def initialize_session():
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": prompt_chat_response, "name": "System"}]
    if "hide_history" not in st.session_state:
        st.session_state.hide_history = False


def set_page_configuration():
    st.set_page_config(page_title="UAV Explorer")
    st.title("🚁 Conversational UAV Explorer")


def get_audio_transcript(audio):
    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    user_transcript = transcript["text"]
    st.session_state.messages.append({"role": "user", "content": user_transcript, "name": "Operator"})
    return user_transcript


def get_uav_command(user_transcript):
    uav_command = fewshot.get_command(user_transcript)
    st.session_state.messages.append({"role": "function", "content": uav_command, "name": "UAV"})
    return uav_command


def get_uav_response():
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    uav_response = response["choices"][0]["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": uav_response, "name": "Assistant"})
    return uav_response


def transcribe(audio):
    user_transcript = get_audio_transcript(audio)
    uav_command = get_uav_command(user_transcript)
    uav_response = get_uav_response()

    # command, location = parse_command(uav_command)
    # send_command(command, location)

    display_latest_messages()


def text_delay(prefix, message):
    placeholder = st.empty()
    response = prefix
    for chunk in message.split():
        response += chunk + " "
        time.sleep(0.05)
        placeholder.markdown(response + "▌")
    placeholder.markdown(response)


def display_previous_messages():
    for message in st.session_state.messages[:-3]:
        role = message["role"]
        content = message["content"]
        prefix = f"**{message['name']}**: "

        if role != "system":
            st.markdown(prefix + content)


def display_latest_messages():
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
    audio = audiorecorder("Start Voice Command", "End Voice Command")
    if len(audio) > 0:
        audio_filename = "temp_audio.wav"
        with open(audio_filename, "wb") as wav_file:
            wav_file.write(audio.tobytes())
        transcribe(audio_filename)


def display_sidebar():
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
    with st.chat_message("assistant"):
        st.write(f"**Assistant**: Where would you like me to go today?")
    record_button()


def display_map_tab():
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
    logo = """
        <style>
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                text-align: center;
                padding: 40px;
            }
        </style>

        <div class="footer">
            <img src="host vcu logo" width=200>
            <span style="font-size: 30px; margin: 0 15px;">×</span>
            <img src="host uva logo" width=120>
        </div>
    """
    st.markdown(logo, unsafe_allow_html=True)


def main():
    initialize_session()
    set_page_configuration()
    display_sidebar()

    main_tab, history_tab, map_tab = st.tabs(["Main", "Chat History", "Map"])

    with main_tab:
        display_main_tab()
    with history_tab:
        display_previous_messages()
    with map_tab:
        display_map_tab()

    display_logo()


if __name__ == '__main__':
    main()
