<h2>Running doctests for the module with pytest</h2>
1. Acquire Python 3.8
2. Install pytest <br>
   `pip3 install pytest` <br>
3. Clone repository where you please to <br>
    `git clone https://github.com/JeRusakow/epam_python_course` <br>
4. Change directory to repository root
5. a) Run doctests only<br>
    `python3 -m doctest homework4/task4/task_4_doctest.py -v` <br>
   b) Run doctests and unit tests using pytest
   `pytest --doctest-modules homework4/task4/task_4_doctest.py tests/test_homework4/test_task4_fizzbuzz.py`
