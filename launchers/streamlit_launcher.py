import subprocess

from interfaces import clear_screen


def streamlit_launcher():
    """
    Launch the streamlit dashboard
    """

    clear_screen()

    subprocess.run(
        [
            "streamlit", 
            "run", 
            "interfaces/streamlit_app.py"],
        check=True
    )