import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import tempfile
from ball_tracker import track_ball

st.set_page_config(page_title="Cricket AI")

st.title("🏏 Cricket Ball Tracker (AI)")

video = st.file_uploader("Upload cricket bowling video", type=["mp4"])

if video:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(video.read())
        video_path = tmp.name

    st.video(video_path)
    st.info("⏳ AI is analyzing the video...")

    positions = track_ball(video_path)

    if positions:
        x = [p[0] for p in positions]
        y = [p[1] for p in positions]

        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o')
        ax.invert_yaxis()
        ax.set_title("Ball Trajectory")
        st.pyplot(fig)

        st.success("✅ Ball detected successfully")
    else:
        st.error("❌ Ball not detected. Try clear video.")
