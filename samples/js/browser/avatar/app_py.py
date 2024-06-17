import streamlit as st
import streamlit.components.v1 as components

def run():
    iframe_src = "https://icy-sky-0f4e8cf03.5.azurestaticapps.net/"
    components.iframe(iframe_src, height = 800, width = 800, scrolling = True)
   # You can add height and width to the component of course.

if __name__ == "__main__":
    run()