#More configuration in __init__.py inside 'app' folder 
from app import app
 
if __name__ == "__main__":
    app.run(debug=False)