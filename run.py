#from app import app

#if __name__ == "__main__":
#    app.config['ENV']="development"
    #app.run(host='0.0.0.0', port=5000)
#    app.run(debug=True)

from app import app
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
