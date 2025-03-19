from flask import Flask, jsonify, request
from src.datastructure import FamilyStructure

app = Flask(__name__)

jackson_family = FamilyStructure('Jackson')

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)

    if member is None:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member), 200

@app.route('/member', methods=['POST'])
def add_member():
    data = request.json

    if not all(key in data for key in ["first_name", "age", "lucky_numbers"]):
        return jsonify({"error": "Missing required fields"}), 400

    jackson_family.add_member(data)
    return jsonify({"success": True}), 200


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    success = jackson_family.delete_member(member_id)
    if not success:
        return jsonify({"error": "Member not found"}), 404
    return jsonify({"done": True}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)

