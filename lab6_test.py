"""test code for TIL Python programming jupyter notebook Lab 6 - Data Visualization"""
from unittest import result
import pytest
import matplotlib.pyplot as plt
from testbook import testbook


@pytest.fixture(scope='module')
def tb():
    with testbook('lab6_2025.ipynb', execute=True) as tb:
        yield tb

# Q1 test the plot_one_stock function
def test_plot_one_stock(tb):
    plot_one_stock = tb.ref("plot_one_stock")
    result = plot_one_stock()
    assert result["xlabel"] == "Date", "Error: x-axis label is incorrect"
    assert result["ylabel"] == "Stock Value", "Error: y-axis label is incorrect"
    assert result["num_lines"] == 1, "Error: There should be one line plotted"

# Q2 test the plot_all_stocks function
def test_plot_all_stocks(tb):
    plot_all_stocks = tb.ref("plot_all_stocks")
    result = plot_all_stocks()
    assert result["num_lines"] == 6, "Error: There should be six lines plotted"
    assert result['legend_exists'], "Error: Legend does not exist."

# Q3: test the sns.relplot function
def test_sns_relplot(tb):
    # Reference the relplot function in the notebook
    result = tb.ref("test_result_g1")

    # Assertions
    assert result["num_axes"] == 2, "Error: There should be 2 subplots (one for each time)."
    assert "time = Lunch" in result["col_titles"], "Error: Missing title for Lunch subplot."
    assert "time = Dinner" in result["col_titles"], "Error: Missing title for Dinner subplot."


# Q4: test plotly express line plot
def test_px_line(tb):
    result = tb.ref("test_result_g2")
    assert result["num_lines"] == 6, "Error: There should be six lines plotted"


# Q5: test plotly express scatter plot with facets
def test_px_scatter(tb):
    result = tb.ref("test_result_g3")
    expected_facets = ["time=Lunch", "time=Dinner"]
    assert all(facet in result["facet_titles"] for facet in expected_facets), "Error: Facet titles are incorrect."

