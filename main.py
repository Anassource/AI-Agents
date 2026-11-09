from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Retrieve the API key from environment variables
print(GOOGLE_API_KEY)  # Print the API key to verify it's loaded correctly