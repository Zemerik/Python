class Logger:
    def log(self, message):
        print(f"LOG: {message}")

class Validator:
    def validate(self, data):
        print("Validating data...")

class DatabaseHandler(Logger, Validator):
    def save(self, data):
        self.validate(data)
        self.log("Saving to database...")
        print("Data saved")

# MRO demonstration
print(DatabaseHandler.__mro__)