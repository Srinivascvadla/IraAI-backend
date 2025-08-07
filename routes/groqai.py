from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from extensions import db
from models import Prompt
from utils.openai_service import ask_groq 

Prompt_bp = Blueprint('groqai_prompt', __name__)

@Prompt_bp.route('/prompt', methods=['POST'])
@jwt_required()
def create_prompt():
    data = request.get_json()
    user_id = get_jwt_identity()
    prompt_text = data.get('prompt')

    if not prompt_text:
        return jsonify({"msg": "Prompt text is required"}), 400

    # Create a new prompt
    new_prompt = Prompt(user_id=user_id, prompt=prompt_text)
    
    # Get response from Groq AI
    response_text = ask_groq(prompt_text)
    new_prompt.response = response_text

    db.session.add(new_prompt)
    db.session.commit()

    return jsonify({"msg": "Prompt created successfully", "response": response_text}), 201

@Prompt_bp.route('/prompts', methods=['GET'])
@jwt_required()
def get_prompts():
    user_id = get_jwt_identity()
    prompts = Prompt.query.filter_by(user_id=user_id).all()
    
    return jsonify([{"id": prompt.id, "prompt": prompt.prompt, "response": prompt.response, "created_at": prompt.created_at} for prompt in prompts]), 200

@Prompt_bp.route('/prompt/<int:prompt_id>', methods=['GET'])
@jwt_required()
def get_prompt(prompt_id):
    user_id = get_jwt_identity()
    prompt = Prompt.query.filter_by(id=prompt_id, user_id=user_id).first()

    if not prompt:
        return jsonify({"msg": "Prompt not found"}), 404

    return jsonify({"id": prompt.id, "prompt": prompt.prompt, "response": prompt.response, "created_at": prompt.created_at}), 200

@Prompt_bp.route('/prompt/<int:prompt_id>', methods=['PUT'])
@jwt_required()
def update_prompt(prompt_id):
    data = request.get_json()
    user_id = get_jwt_identity()
    prompt = Prompt.query.filter_by(id=prompt_id, user_id=user_id).first()

    if not prompt:
        return jsonify({"msg": "Prompt not found"}), 404

    prompt_text = data.get('prompt')
    if prompt_text:
        prompt.prompt = prompt_text
        prompt.response = ask_groq(prompt_text)  # Use Groq AI for update

    db.session.commit()

    return jsonify({"msg": "Prompt updated successfully", "response": prompt.response}), 200

@Prompt_bp.route('/prompt/<int:prompt_id>', methods=['DELETE'])
@jwt_required()
def delete_prompt(prompt_id):
    user_id = get_jwt_identity()
    prompt = Prompt.query.filter_by(id=prompt_id, user_id=user_id).first()

    if not prompt:
        return jsonify({"msg": "Prompt not found"}), 404

    db.session.delete(prompt)
    db.session.commit()

    return jsonify({"msg": "Prompt deleted successfully"}), 200
