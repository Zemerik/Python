# Dictionary with set values
movie_ratings = {
    "action": {"John", "Mike", "Sarah"},
    "comedy": {"Mike", "Emma"},
    "drama": {"Sarah", "Emma"}
}

# Add new voter to genre
movie_ratings["action"].add("Emma")

# Find voters of multiple genres
action_fans = movie_ratings["action"]
drama_fans = movie_ratings["drama"]
both_genres = action_fans & drama_fans

print(f"Fans of both action and drama: {both_genres}")