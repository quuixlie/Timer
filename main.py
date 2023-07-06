from src.ui import init_ui, play_confetti_animation, set_color, destroy_ui
from src.timer import start_timer
from src.input_handler import get_user_input


work_time_in_seconds = get_user_input()

init_ui()
set_color("cyan")
start_timer(work_time_in_seconds)
while True:
    play_confetti_animation()