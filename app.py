import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cricket AI")

st.title("🏏 Cricket Ball Tracker (AI)")

video = st.file_uploader("Upload cricket bowling video", type=["mp4"])

if video:
    st.video(video)
    st.success("✅ Video uploaded successfully")

    # Fake demo data (AI comes later)
    x = np.linspace(0, 10, 20)
    y = np.sin(x)

    st.subheader("Ball Trajectory (Demo)")
    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)

    st.info("Ball speed: 120 km/h (demo)")
