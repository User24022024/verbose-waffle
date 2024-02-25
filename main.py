import os
from dotenv import load_dotenv
from entry.entry import app

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 3000)))
