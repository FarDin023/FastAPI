from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Define the users table
users = Table(
    'users', MetaData(),
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('password', String(255))
)

# Create an engine to connect to the MySQL database
engine = create_engine("mysql+pymysql://root@localhost:3306/test")
meta = MetaData()

# Create the users table if it doesn't exist
meta.create_all(engine, tables=[users])

# Establish a connection to the database
conn = engine.connect()

# Example query to fetch data from the users table
result = conn.execute(users.select()).fetchall()
print(result)
