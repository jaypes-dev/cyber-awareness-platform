from flask import Blueprint, jsonify
import random

phishing_bp = Blueprint('phishing', __name__)

@phishing_bp.route('/api/generate_phishing')
def generate_email():
    emails = [
        "🚨 Your password is expiring! Reset now: http://fake-it.com",
        "🎁 You've won an Amazon Gift Card! Click to claim",
        "📤 Urgent invoice from HR – please review"
    ]
    return jsonify({'email_body': random.choice(emails)})
