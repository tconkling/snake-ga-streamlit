from unittest import mock
import pygame
import streamlit as st

st.title("Snake!")
st.markdown("Reference article: [Teach an AI to play games](https://towardsdatascience.com/how-to-teach-an-ai-to-play-games-deep-reinforcement-learning-28f9b920440a)")

st.image("snake.gif")

result_text = None
results_chart = None
def on_game_finished(game_counter, score):
	global results_chart
	global result_text
	if results_chart is None:
		result_text = st.empty()
		results_chart = st.line_chart()

	result_text.markdown(f"Game {game_counter} score: {score}")
	results_chart.add_rows({"score": [score]})

# mock out pygame when running in Streamlit, because it breaks when
# not on the main thread!
with mock.patch("snakeClass.pygame"):
	import snakeClass

	pygame.font.init()
	params = snakeClass.define_parameters()
	params['bayesian_optimization'] = False
	params['train'] = True
	snakeClass.run(display_option=False, speed=50, params=params, on_game_finished=on_game_finished)
