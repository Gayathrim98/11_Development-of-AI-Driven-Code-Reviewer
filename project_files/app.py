import webbrowser

import os
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from datetime import datetime
from ast_engine.analyzer import analyze_code
from ai_engine.openai_reviewer import get_openai_review

app = Flask(__name__, static_folder="frontend/dist", template_folder="frontend/dist")
CORS(app)

# Database config (your existing setup)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://neondb_owner:npg_M4Nlvr6AyFuT@ep-wandering-mode-a1w7po4n-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Database model (your existing setup)
class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Text, nullable=False)
    analysis = db.Column(db.JSON)
    ai_review = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "analysis": self.analysis,
            "ai_review": self.ai_review,
            "created_at": self.created_at.isoformat()
        }

with app.app_context():
    db.create_all()

# ----------------- API Endpoints -----------------
@app.route("/review", methods=["POST"])
def review():
    data = request.get_json()
    if not data or "code" not in data:
        return jsonify({"error": "No code provided"}), 400

    code = data["code"]
    analysis = analyze_code(code)
    ai_review = get_openai_review(code)

    new_review = Review(code=code, analysis=analysis, ai_review=ai_review)
    db.session.add(new_review)
    db.session.commit()

    return jsonify({"analysis": analysis, "ai_review": ai_review})

@app.route("/reviews", methods=["GET"])
def get_reviews():
    reviews = Review.query.order_by(Review.created_at.desc()).all()
    return jsonify([r.to_dict() for r in reviews])

# ----------------- Serve React App -----------------
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

# ----------------- Run -----------------
if __name__ == "__main__":
    webbrowser.open("https://code-mind-reviewer--rahulsecret2004.replit.app")

    app.run(debug=True)
