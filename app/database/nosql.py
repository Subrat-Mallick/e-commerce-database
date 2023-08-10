from pymongo import MongoClient

from app.config.database import get_mongodb_url

# Create a MongoDB client
MONGODB_URL = get_mongodb_url()
client = MongoClient(MONGODB_URL)

# Select your MongoDB database
db = client.get_database("ECommerceNoSQL")

# Define your MongoDB collections here
# Example:
# product_reviews_collection = db["ProductReviews"]
# customer_preferences_collection = db["CustomerPreferences"]

# Add your MongoDB utility functions here
# Example:
# def get_product_reviews_by_product_id(product_id):
#     return product_reviews_collection.find({"product_id": product_id})

# Implement other MongoDB queries and operations as needed
