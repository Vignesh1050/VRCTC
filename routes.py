'''from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import get_db_connection
from config import ADMIN_API_KEY

routes_bp = Blueprint('routes', __name__)

# Route to add a new train
@routes_bp.route('/add_train', methods=['POST'])
def add_train():
    api_key = request.headers.get("X-API-KEY")
    if api_key != ADMIN_API_KEY:
        return jsonify({"message": "Unauthorized"}), 403

    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO trains (name, source, destination, total_seats, available_seats) VALUES (%s, %s, %s, %s, %s)",
                   (data['name'], data['source'], data['destination'], data['total_seats'], data['total_seats']))
    conn.commit()
    conn.close()

    return jsonify({"message": "Train added successfully!"}), 201

# Route to book a seat on a train
@routes_bp.route('/book_seat', methods=['POST'])
@jwt_required()
def book_seat():
    user = get_jwt_identity()
    data = request.get_json()
    train_id = data['train_id']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT available_seats FROM trains WHERE id=%s FOR UPDATE", (train_id,))
    train = cursor.fetchone()

    if train and train[0] > 0:
        cursor.execute("INSERT INTO bookings (user_id, train_id) VALUES (%s, %s)", (user['id'], train_id))
        cursor.execute("UPDATE trains SET available_seats = available_seats - 1 WHERE id=%s", (train_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Seat booked successfully!"}), 200
    else:
        conn.close()
        return jsonify({"message": "No seats available"}), 400

# Route to get all trains based on source and destination
@routes_bp.route('/trains', methods=['GET'])
def get_trains():
    source = request.args.get('source')
    destination = request.args.get('destination')

    if not source or not destination:
        return jsonify({"message": "Both source and destination must be provided"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM trains WHERE source = %s AND destination = %s"
    cursor.execute(query, (source, destination))
    trains = cursor.fetchall()

    conn.close()

    if trains:
        # Return the list of trains as a JSON response
        train_list = []
        for train in trains:
            train_list.append({
                "id": train[0],
                "name": train[1],
                "source": train[2],
                "destination": train[3],
                "total_seats": train[4],
                "available_seats": train[5]
            })
        return jsonify(train_list), 200
    else:
        return jsonify({"message": "No trains found for the given route"}), 404'''
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import get_db_connection
from config import ADMIN_API_KEY

routes_bp = Blueprint('routes', __name__)

# Route to add a new train
@routes_bp.route('/add_train', methods=['POST'])
def add_train():
    api_key = request.headers.get("X-API-KEY")
    if api_key != ADMIN_API_KEY:
        return jsonify({"message": "Unauthorized"}), 403

    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO trains (name, source, destination, total_seats, available_seats) VALUES (%s, %s, %s, %s, %s)",
                   (data['name'], data['source'], data['destination'], data['total_seats'], data['total_seats']))
    conn.commit()
    conn.close()

    return jsonify({"message": "Train added successfully!"}), 201

# Route to book a seat on a train
@routes_bp.route('/book_seat', methods=['POST'])
@jwt_required()
def book_seat():
    user = get_jwt_identity()
    data = request.get_json()
    train_id = data['train_id']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT available_seats FROM trains WHERE id=%s FOR UPDATE", (train_id,))
    train = cursor.fetchone()

    if train and train[0] > 0:
        cursor.execute("INSERT INTO bookings (user_id, train_id) VALUES (%s, %s)", (user['id'], train_id))
        cursor.execute("UPDATE trains SET available_seats = available_seats - 1 WHERE id=%s", (train_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Seat booked successfully!"}), 200
    else:
        conn.close()
        return jsonify({"message": "No seats available"}), 400

# Route to get all trains based on source and destination
@routes_bp.route('/trains', methods=['GET'])
def get_trains():
    source = request.args.get('source')
    destination = request.args.get('destination')

    if not source or not destination:
        return jsonify({"message": "Both source and destination must be provided"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM trains WHERE source = %s AND destination = %s"
    cursor.execute(query, (source, destination))
    trains = cursor.fetchall()

    conn.close()

    if trains:
        train_list = []
        for train in trains:
            train_list.append({
                "id": train[0],
                "name": train[1],
                "source": train[2],
                "destination": train[3],
                "total_seats": train[4],
                "available_seats": train[5]
            })
        return jsonify(train_list), 200
    else:
        return jsonify({"message": "No trains found for the given route"}), 404


