import pdb

def analyze_data(data):
    # Post-mortem debugging
    results = []
    for item in data:
        pdb.set_trace()
        if item < 0:  # Break when negative values appear
            results.append(0)
        else:
            results.append(item * 2)
    return results

# Test with problematic data
data = [1, 3, -5, 8]
analyze_data(data)