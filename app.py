import streamlit as st
import matplotlib.pyplot as plt
import tempfile
from ball_tracker import track_ball
from speed_calc import calculate_speed

st.set_page_config(page_title="Cricket AI")

st.title("🏏 Cricket Ball Speed Analyzer")

video = st.file_uploader("Upload bowling video", type=["mp4"])

if video:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(video.read())
        video_path = tmp.name

    st.video(video_path)
    st.info("⏳ AI analyzing ball...")

    positions = track_ball(video_path)

    if positions:
        speed = calculate_speed(positions)

        x = [p[0] for p in positions]
        y = [p[1] for p in positions]

        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o')
        ax.invert_yaxis()
        ax.set_title("Ball Trajectory")
        st.pyplot(fig)

        st.success(f"🔥 Ball Speed: {speed} km/h")
    else:
        st.error("❌ Ball not detected. Use clear slow-motion video.")
