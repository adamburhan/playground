from airflow_project.helper_functions import example
from playground.dev.airflow_project.helper_functions.example import example_func


def test_example_func():
    result = example_func(2, 3)
    assert result == 5
