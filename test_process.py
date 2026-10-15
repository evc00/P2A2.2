
import pytest
from process import process_grade


@pytest.mark.statement
@pytest.mark.parametrize(
    "grade, expected",
    [
        (80, "Aprobado"),
        (50, "Reprobado"),
        ("abc", "Error: calificación inválida"),
        (-5, "Error: calificación fuera de rango"),
    ],
)
def test_statement_coverage(grade, expected):
    assert process_grade(grade) == expected


@pytest.mark.branch
@pytest.mark.parametrize(
    "grade, expected",
    [
        ("abc", "Error: calificación inválida"),
        (120, "Error: calificación fuera de rango"),
        (70, "Aprobado"),
        (69, "Reprobado"),
        (0, "Reprobado"),
        (100, "Aprobado"),
    ],
)
def test_branch_coverage(grade, expected):
    assert process_grade(grade) == expected


@pytest.mark.path
@pytest.mark.parametrize(
    "grade, expected",
    [
        ("abc", "Error: calificación inválida"),
        (-1, "Error: calificación fuera de rango"),
        (101, "Error: calificación fuera de rango"),
        (85, "Aprobado"),
        (40, "Reprobado"),
    ],
)
def test_path_coverage(grade, expected):
    assert process_grade(grade) == expected
