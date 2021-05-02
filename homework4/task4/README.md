##Running doctests for the module with pytest

1. Acquire Python 3.8
1. Install pytest \
   `pip3 install pytest`
1. Clone repository where you please to \
    `git clone https://github.com/JeRusakow/epam_python_course`
1. Change directory to repository root. Everything is prepared to run the tests \
    * Run doctests only \
    `python3 -m doctest homework4/task4/task_4_doctest.py -v`
    * Run doctests and unit tests using pytest \
   `pytest --doctest-modules homework4/task4/task_4_doctest.py tests/test_homework4/test_task4_fizzbuzz.py`
