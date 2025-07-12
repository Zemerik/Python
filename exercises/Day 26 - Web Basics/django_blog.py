"""
Exercise 2: Django Blog
Build a Django blog with:
- Post model (title, content, date)
- Admin interface
- List/detail views
(Simulate models/views as code, no real migrations.)
"""

# Simulated Django models.py
class Post:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date

# Simulated admin.py registration
class AdminSite:
    def register(self, model):
        print(f"Registered {model.__name__} with admin site.")

admin_site = AdminSite()
admin_site.register(Post)

# Simulated views.py
from datetime import datetime

posts = [
    Post("First Post", "This is the first post.", datetime(2024, 6, 1)),
    Post("Second Post", "This is the second post.", datetime(2024, 6, 2)),
]

def post_list():
    print("=== Blog Posts ===")
    for post in posts:
        print(f"- {post.title} ({post.date.strftime('%Y-%m-%d')})")

def post_detail(title):
    for post in posts:
        if post.title == title:
            print(f"=== {post.title} ===\n{post.content}\nDate: {post.date.strftime('%Y-%m-%d')}")
            return
    print("Post not found.")

def main():
    print("=== Django Blog Simulation ===")
    post_list()
    print("\nViewing details for 'First Post':")
    post_detail("First Post")

if __name__ == "__main__":
    main() 