"""
Exercise 2: Deployment Guide
Deploy the application to:
- Cloud platform (Heroku/DigitalOcean)
- Configure production database
- Set up CI/CD pipeline
(Provide a step-by-step guide as code comments and print statements, no real deployment.)
"""

def deployment_guide():
    print("=== Deployment Guide ===")
    print("1. Prepare your application for deployment:")
    print("   - Ensure requirements.txt is up to date.")
    print("   - Set environment variables for production (e.g., SECRET_KEY, DATABASE_URL).")
    print("2. Deploy to Heroku:")
    print("   - Install Heroku CLI and login.")
    print("   - Run: heroku create <app-name>")
    print("   - Run: git push heroku main")
    print("   - Set config vars: heroku config:set KEY=VALUE")
    print("   - Attach a production database: heroku addons:create heroku-postgresql:hobby-dev")
    print("3. Deploy to DigitalOcean:")
    print("   - Create a Droplet and SSH in.")
    print("   - Install Python, pip, and dependencies.")
    print("   - Set up Gunicorn and Nginx for serving Flask/Django.")
    print("   - Configure firewall and security settings.")
    print("4. Set up CI/CD pipeline:")
    print("   - Use GitHub Actions or GitLab CI.")
    print("   - Add workflow file to run tests and deploy on push.")
    print("   - Example: .github/workflows/deploy.yml")
    print("5. Monitor and maintain:")
    print("   - Set up logging and error monitoring (Sentry, Rollbar, etc.)")
    print("   - Regularly update dependencies and back up your database.")

def main():
    deployment_guide()

if __name__ == '__main__':
    main() 