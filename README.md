# Mini SQL Query Engine (Python)

A simplified, in-memory SQL query engine built from scratch using Python.  
It demonstrates how SQL queries are parsed, filtered, and executed internally in a database engine.  
The tool loads CSV files into memory and executes SQL-like queries through an interactive command-line interface (CLI).

---

## 🚀 Features

- Load CSV files into memory (`list[dict]`)
- Parse a subset of SQL:
  - SELECT *
  - SELECT col1, col2
  - WHERE with operators: =, !=, >, <, >=, <=
  - COUNT(*)
  - COUNT(column)
- Execute filtering, projection, and aggregation
- Clean error handling
- Interactive CLI (REPL)

---

## 🧠 How the Engine Works

```
User Query → Parser → Execution Engine → Output
```

### Parser (`parser.py`)
Extracts:
- Columns to select  
- Table name  
- WHERE clause  
- COUNT details  

Example parsed output:

```python
{
  "select_cols": ["name", "age"],
  "from_table": "users",
  "where": {"column": "age", "operator": ">", "value": 30},
  "is_count": False,
  "count_column": None
}
```

### Execution Engine (`engine.py`)
- Loads CSV file based on the table name  
- Applies WHERE filter  
- Executes COUNT or SELECT projection  
- Returns rows as dictionaries  

### CLI (`cli.py`)
- Runs an interactive SQL prompt  
- Accepts SQL queries  
- Prints result rows or error messages  

---

## 📥 Installation & Setup

Clone the repository:

```sh
git clone https://github.com/Satyanagapraveen/mini-sql-engine-23A91A12A5
cd mini-sql-engine-23A91A12A5
```

Ensure Python 3 is installed:

```sh
python --version
```

Run the CLI:

```sh
python cli.py
```

Place CSV files (e.g., `users.csv`) in the same folder.

---

# 📘 Supported SQL Grammar

### Basic Syntax
```
SELECT <columns> FROM <table> [WHERE <column> <op> <value>];
```

### Examples

#### Select all columns
```sql
SELECT * FROM users;
```

#### Select specific columns
```sql
SELECT name, age FROM users;
```

#### WHERE filtering (single condition)
```sql
SELECT name FROM users WHERE age > 25;
```

Supported operators:
```
=   !=   >   <   >=   <=
```

#### Aggregations
```sql
SELECT COUNT(*) FROM users;
SELECT COUNT(country) FROM users WHERE age > 30;
```

---

# 🧪 Example Queries

```sql
SELECT * FROM users;
SELECT name, country FROM users WHERE age >= 30;
SELECT COUNT(*) FROM users;
SELECT COUNT(country) FROM users WHERE country = 'USA';
```

---

# ❗ Error Handling Examples

Invalid SQL:
```
SELECT * users;
→ Error: Missing FROM clause
```

Invalid WHERE operator:
```
SELECT * FROM users WHERE age >> 30;
→ Error: Invalid WHERE clause syntax
```

Unknown column:
```
SELECT abc FROM users;
→ Error: Column 'abc' not found.
```

Missing CSV file:
```
SELECT * FROM nosuchtable;
→ Error: CSV file 'nosuchtable.csv' not found.
```

---

# 📂 Sample CSV Files

### sample_users.csv
```
name,age,country
Alice,25,USA
Bob,30,India
Charlie,35,USA
Diana,28,UK
```

### sample_sales.csv
```
item,price,quantity
Pen,10,3
Notebook,40,2
Pencil,5,10
Bag,500,1
```

---

# 🧱 Project Structure

```
mini-sql-engine/
│
├── parser.py
├── engine.py
├── cli.py
├── sample_users.csv
├── sample_sales.csv
└── README.md
```

---

# 🏁 Conclusion

This project demonstrates:
- SQL parsing logic  
- Execution pipelines  
- Filtering & aggregation  
- CLI development  
- Error handling  

You can extend this engine to support ORDER BY, LIMIT, JOIN, or multiple WHERE conditions.

