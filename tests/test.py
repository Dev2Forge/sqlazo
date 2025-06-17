import random
import string
from sqlazo import Database

# https://docs.dev2forge.software/sqlazo
# https://docs.dev2forge.software/chromologger
# https://docs.dev2forge.software/chromolog

def random_name(length=8):
	"""
	Generate a random ASCII name of given length.
	"""
	return ''.join(random.choices(string.ascii_letters, k=length))

def stress_test(db: Database, num_records: int = 1000):
	"""
	Insert a large number of random records to stress-test the table.
	- name: random 8-character string
	- age: random integer between 1 and 100
	- score: random float between 0.00 and 1000.00
	"""
	for _ in range(num_records):
		name = random_name()
		age = random.randint(1, 100)
		score = round(random.random() * 1000, 2)
		# Insert only the specified columns ('name', 'age', 'score') into 'user'
		db.insert_data([name, age, score], ['name', 'age', 'score'], 'user')

def main():
	# Use an in-memory SQLite database (lives only during this process)
	db = Database('test.db')

	# Define table schema: id is primary key, name & email are TEXT, age is INT, score is REAL
	columns = [
		'id INTEGER PRIMARY KEY',
		'name TEXT NOT NULL',
		'age INTEGER NOT NULL',
		'email TEXT UNIQUE',
		'score REAL DEFAULT 0.0'
	]
	# Create the 'user' table
	db.create_table('user', columns)

	# Insert a few initial users
	initial_users = [
		('Santiago', 19, 'santiago@example.com'),
		('Ana', 17,      'ana@example.com'),
		('Pedro', 20,    'pedro@example.com'),
	]
	for name, age, email in initial_users:
		db.insert_data([name, age, email], ['name', 'age', 'email'], 'user')

	# Show all rows
	print("=== Initial data ===")
	for row in db.get_data_all('user'):
		print(row)

	# Query only name & email for users younger than 20
	print("\n=== Users under 20 (name & email only) ===")
	for row in db.get_data_where('user', 'age < 20', 'name,email'):
		print(row)

	# Run a stress test: insert 500 random users
	print("\n=== Performing stress test (100 inserts) ===")
	stress_test(db, num_records=100)
	total = len(db.get_data_all('user').fetchall())
	print(f"Total records after stress test: {total}")

	# Delete all under‑18s and show remaining count
	print("\n=== Deleting under‑18 users ===")
	db.delete_data('user', 'age < 18')
	remaining = db.get_data_all('user').fetchall()
	print(f"Remaining users: {len(remaining)}")
	# Preview first five remaining
	for row in remaining[:5]:
		print(row)

	# Finally close
	db.close()
	print("\nTest complete.")

if __name__ == '__main__':
	main()
