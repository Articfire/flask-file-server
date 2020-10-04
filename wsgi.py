from app import app
from config import ProductionConfig

if __name__ == "__main__":
    app.config.from_object(ProductionConfig())
    app.run()