# How to execute the API and the DB

# make sure to install all of these packages
pip install fastapi fastapi-sqlalchemy pydantic alembic psycopg2 uvicorn python-dotenv

# to execute docker
docker-compose build
docker-compose up

# to prepare the migration
docker-compose run app alembic revision --autogenerate -m "New Migration"
docker-compose run app alembic upgrade head