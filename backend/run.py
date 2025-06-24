from dotenv import load_dotenv
import os
load_dotenv()

from app import create_app, socketio, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.getenv('PORT', 5000))
    socketio.run(app, debug=True, host='0.0.0.0', port=port, allow_unsafe_werkzeug=True)
