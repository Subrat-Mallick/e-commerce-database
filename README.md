# Multi-Tier E-commerce Database Project

## Introduction
This project aims to design and implement a multi-tier e-commerce database system to support the operations of an online retail store. The system is built with a combination of SQL (MySQL or PostgreSQL) for structured data and MongoDB for NoSQL data storage.

## Database Architecture
The project follows a multi-tier architecture, comprising three tiers:
- Presentation Tier: User interface layer.
- Application Tier: Handles business logic and user requests.
- Data Tier: Stores and manages data using SQL and NoSQL databases.

## SQL Database Schema (MySQL/PostgreSQL)
### Entities and Relationships
- Customers
- Products
- Orders
- Order_Items
- Categories

### Attributes
- Customers: customer_id, first_name, last_name, email, password, address
- Products: product_id, name, price, description, stock_quantity, category_id
- Orders: order_id, customer_id, order_date, total_amount
- Order_Items: order_item_id, order_id, product_id, quantity
- Categories: category_id, name

## NoSQL Database Schema (MongoDB)
Collections:
- ProductReviews: product_id, reviews array (reviewer_id, rating, comment)
- CustomerPreferences: customer_id, preferences object (category preferences, etc.)

## Implementation
### SQL Database (MySQL/PostgreSQL)
1. Create a database named "ECommerceDB."
2. Implement tables for Customers, Products, Orders, Order_Items, and Categories.
3. Establish relationships using foreign keys.
4. Write SQL queries for CRUD operations.

### NoSQL Database (MongoDB)
1. Set up a MongoDB database named "ECommerceNoSQL."
2. Create collections for ProductReviews and CustomerPreferences.
3. Store product reviews and customer preferences.

### Integration and Application Logic
1. Develop the application layer for user interactions, order processing, and account management.
2. Implement APIs to connect the presentation tier with the application tier.
3. Utilize appropriate libraries or frameworks for backend development.

## Usage
1. Clone the repository: `git clone https://github.com/your-username/e-commerce-database.git`
2. Set up the required databases (SQL and MongoDB).
3. Run the application layer code to start the e-commerce system.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For inquiries or feedback, please contact [Subrat Kumar Mallick.](mallicksubrat765@gmail.com).
