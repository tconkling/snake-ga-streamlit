from unittest import mock
import pygame
import streamlit as st

st.write("Initializing snake!")

# mock out pygame when running in Streamlit, because it breaks when
# not on the main thread!
with mock.patch("snakeClass.pygame"):
	import snakeClass

	pygame.font.init()
	params = snakeClass.define_parameters()
	params['bayesian_optimization'] = False
	snakeClass.run(display_option=False, speed=50, params=params)
