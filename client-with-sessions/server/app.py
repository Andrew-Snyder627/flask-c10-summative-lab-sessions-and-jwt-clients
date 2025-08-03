# app.py
from flask import request, session, jsonify
from config import app, db, bcrypt
from models import User, Task

# --------------------
# Authentication Routes
# --------------------

@app.post("/signup")
def signup():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    password_confirmation = data.get("password_confirmation")

    if not username or not password or password != password_confirmation:
        return jsonify({"errors": ["Invalid signup details"]}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"errors": ["Username already exists"]}), 409

    user = User(username=username)
    user.password_hash = password
    db.session.add(user)
    db.session.commit()

    session["user_id"] = user.id
    return jsonify({"id": user.id, "username": user.username}), 201

@app.post("/login")
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.authenticate(password):
        session["user_id"] = user.id
        return jsonify({"id": user.id, "username": user.username})
    return jsonify({"errors": ["Invalid credentials"]}), 401

@app.get("/check_session")
def check_session():
    user_id = session.get("user_id")
    if user_id:
        user = User.query.get(user_id)
        if user:
            return jsonify({"id": user.id, "username": user.username})
    return jsonify({}), 401

@app.delete("/logout")
def logout():
    session["user_id"] = None
    return {}, 204