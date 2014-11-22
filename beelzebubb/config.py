from beelzebubb import app

# key used to encrypt sessions - should be complex and kept secret
app.secret_key = 'secret key here'

# database connection settings
DB_ENGINE = 'postgresql'
DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = 'beelzebubb'
DB_PASSWORD = 'beelzebubb'
DB_NAME = 'beelzebubb'