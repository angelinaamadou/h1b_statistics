#!/bin/bash
python3 ../src/h1b_top10.py ./tests/test_1/input/h1b_input.csv ./tests/test_1/output/top_10_states.txt ./tests/test_1/output/top_10_occupations.txt
python3 ../src/h1b_top10.py ./tests/test_2/input/h1b_input.csv ./tests/test_2/output/top_10_states.txt ./tests/test_2/output/top_10_occupations.txt
python3 ../src/h1b_top10.py ./tests/test_3/input/h1b_input.csv ./tests/test_3/output/top_10_states.txt ./tests/test_3/output/top_10_occupations.txt
python3 ../src/h1b_top10.py ./tests/test_4/input/h1b_input.csv ./tests/test_4/output/top_10_states.txt ./tests/test_4/output/top_10_occupations.txt

