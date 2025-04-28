# File to test coverage for
def calculate_stats(numbers):
    return {
        "mean": sum(numbers)/len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

# Test file
def test_stats():
    result = calculate_stats([10, 20, 30])
    assert result["mean"] == 20
    assert result["min"] == 10
    assert result["max"] == 30