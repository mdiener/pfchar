from pfchar.settings import DEBUG
from pfchar import app

if __name__ == "__main__":
    app.run(debug=DEBUG, host='localhost')
