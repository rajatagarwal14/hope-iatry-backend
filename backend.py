"""
Hope-iatry AI Coaching Platform - Backend Server
Flask server with Claude API integration
"""

from flask import Flask, request, jsonify, send_from_directory, render_template_string
from flask_cors import CORS
import os
import json
import traceback
from datetime import datetime
from pathlib import Path
import requests

# Load environment variables
def load_env_file():
    """Load environment variables from .env file"""
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()

load_env_file()

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)  # Enable CORS for all routes

# Configuration - Using Groq API (Fast and Free!)
GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'
MODEL = 'llama-3.3-70b-versatile'  # Latest Groq model - fast & smart

# Alternative Groq models you can use:
# - llama-3.3-70b-versatile (recommended - latest & fastest)
# - llama-3.1-8b-instant (very fast, smaller model)
# - mixtral-8x7b-32768 (large context window)
# - gemma2-9b-it (Google's model)

# In-memory storage (in production, use a database)
users_db = []
conversations_db = {}

# Clinical keywords for guardrails
CLINICAL_KEYWORDS = [
    'suicide', 'suicidal', 'kill myself', 'self harm', 'self-harm', 'cutting',
    'depression', 'depressed', 'anxiety disorder', 'anxious', 'panic disorder',
    'bipolar', 'schizophrenia', 'psychosis', 'ptsd', 'trauma', 'traumatic',
    'abuse', 'abused', 'panic attack', 'mental breakdown',
    'medication', 'prescribe', 'diagnosis', 'diagnose', 'mental illness',
    'therapist', 'therapy', 'counseling', 'counselor', 'psychologist', 'psychiatrist',
    'hurt myself', 'end my life', 'want to die', 'dying', 'crisis', 'emergency',
    'hopeless', 'worthless', "can't go on", 'give up'
]

def detect_clinical_content(text):
    """Check if text contains clinical keywords"""
    lower_text = text.lower()
    return any(keyword in lower_text for keyword in CLINICAL_KEYWORDS)

def get_system_prompt(mode):
    """Get system prompt based on coaching mode"""
    if mode == 'life':
        return """You are a Life Wellness Coach for Hope-iatry mental health practice. Your responses must be:

RESPONSE STYLE:
- Concise and actionable (2-4 sentences maximum)
- Warm, encouraging, and supportive tone
- Focus on ONE specific actionable tip per response
- Use simple, everyday language

YOUR ROLE:
- Provide daily wellness guidance (sleep, stress, habits, mindfulness)
- Encourage small, achievable goals
- Offer practical self-care strategies
- Support work-life balance

STRICT BOUNDARIES - YOU MUST NOT:
- Diagnose or treat mental health conditions
- Discuss medications, therapy techniques, or clinical treatments
- Provide advice on mental illness, trauma, or serious psychological issues
- Replace professional mental health care

IF CLINICAL TOPICS ARISE:
Immediately redirect: "This requires professional support. Please contact Hope-iatry to schedule with a licensed therapist."

FOCUS AREAS ONLY:
✓ Daily routines and habits
✓ Stress management techniques (breathing, walks, breaks)
✓ Sleep hygiene tips
✓ Mindfulness and gratitude practices
✓ Exercise motivation
✓ Healthy work-life boundaries

Keep responses brief, specific, and immediately actionable."""
    else:
        return """You are a Career Coach for Hope-iatry. Your responses must be:

RESPONSE STYLE:
- Direct and practical (2-4 sentences maximum)
- Professional and results-oriented
- Focus on ONE specific action step per response
- Use clear, professional language

YOUR ROLE:
- Resume optimization and formatting
- Interview preparation strategies
- Job search techniques and networking
- Career planning and goal setting
- Professional development advice

STRICT BOUNDARIES - YOU MUST NOT:
- Provide mental health counseling or therapy
- Discuss anxiety, depression, or psychological issues
- Act as a therapist or counselor

IF MENTAL HEALTH TOPICS ARISE:
Immediately redirect: "For mental health support, please contact Hope-iatry's licensed therapists."

FOCUS AREAS ONLY:
✓ Resume writing (format, keywords, achievements)
✓ Interview tips (prep, questions, follow-up)
✓ Job search strategies (networking, applications)
✓ Career transitions and planning
✓ LinkedIn optimization
✓ Salary negotiation basics

Keep responses brief, specific, and immediately actionable with clear next steps."""

@app.route('/')
def home():
    """Serve the main application"""
    return send_from_directory('static', 'index.html')

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'message': 'Hope-iatry Backend Server is running',
        'api_configured': bool(GROQ_API_KEY),
        'provider': 'Groq',
        'model': MODEL,
        'version': '1.0.0'
    })

@app.route('/api/register', methods=['POST'])
def register_user():
    """Register a new user"""
    try:
        data = request.json
        
        user = {
            'id': len(users_db) + 1,
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
            'address': data.get('address'),
            'registered_at': datetime.now().isoformat(),
            'flagged_for_services': False,
            'conversations_count': 0
        }
        
        users_db.append(user)
        conversations_db[user['id']] = []
        
        return jsonify({
            'success': True,
            'user': user
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.json
        user_id = data.get('user_id')
        user_message = data.get('message')
        chat_mode = data.get('mode')  # 'life' or 'career'
        conversation_history = data.get('history', [])
        
        print(f"\n📨 Chat Request:")
        print(f"   User ID: {user_id}")
        print(f"   Mode: {chat_mode}")
        print(f"   Message: {user_message}")
        
        # Check for clinical content
        if detect_clinical_content(user_message):
            print(f"   ⚠️  Clinical content detected - flagging user")
            
            # Flag user
            for user in users_db:
                if user['id'] == user_id:
                    user['flagged_for_services'] = True
                    break
            
            response_text = """I appreciate you sharing this with me, but this topic requires the expertise of a licensed mental health professional.

**Please contact Hope-iatry directly to schedule an appointment with a licensed therapist.** They're equipped to provide the professional care and support you deserve.

Is there anything else related to daily wellness habits or career development I can help you with today?"""
            
            return jsonify({
                'success': True,
                'response': response_text,
                'flagged': True
            })
        
        # Prepare API request
        if not GROQ_API_KEY:
            return jsonify({
                'success': False,
                'error': 'API key not configured. Please set GROQ_API_KEY in .env file'
            }), 500
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {GROQ_API_KEY}'
        }
        
        # Build messages from history with system message
        messages = [
            {'role': 'system', 'content': get_system_prompt(chat_mode)}
        ]
        
        # Add conversation history
        for msg in conversation_history[-6:]:  # Last 6 messages for context
            messages.append({
                'role': msg['role'],
                'content': msg['content']
            })
        
        # Add current user message
        messages.append({
            'role': 'user',
            'content': user_message
        })
        
        payload = {
            'model': MODEL,
            'messages': messages,
            'max_tokens': 400,
            'temperature': 0.7
        }
        
        print(f"   🤖 Calling Groq API...")
        
        response = requests.post(
            GROQ_API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            assistant_message = result['choices'][0]['message']['content']
            
            print(f"   ✅ Response received")
            
            # Store conversation
            if user_id in conversations_db:
                conversations_db[user_id].append({
                    'user_message': user_message,
                    'assistant_message': assistant_message,
                    'mode': chat_mode,
                    'timestamp': datetime.now().isoformat()
                })
                
                # Update user conversation count
                for user in users_db:
                    if user['id'] == user_id:
                        user['conversations_count'] = len(conversations_db[user_id])
                        break
            
            return jsonify({
                'success': True,
                'response': assistant_message,
                'flagged': False
            })
        else:
            error_msg = f"API Error {response.status_code}: {response.text}"
            print(f"   ❌ {error_msg}")
            return jsonify({
                'success': False,
                'error': error_msg
            }), 500
            
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/admin/users', methods=['GET'])
def get_users():
    """Get all users (admin endpoint)"""
    return jsonify({
        'success': True,
        'users': users_db,
        'total': len(users_db),
        'flagged': len([u for u in users_db if u.get('flagged_for_services')])
    })

@app.route('/api/admin/export', methods=['GET'])
def export_users():
    """Export users as CSV"""
    import io
    import csv
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Header
    writer.writerow(['Name', 'Email', 'Phone', 'Address', 'Registered', 'Conversations', 'Flagged'])
    
    # Data
    for user in users_db:
        writer.writerow([
            user['name'],
            user['email'],
            user['phone'],
            user['address'],
            user['registered_at'],
            user['conversations_count'],
            'YES' if user['flagged_for_services'] else 'NO'
        ])
    
    output.seek(0)
    return output.getvalue(), 200, {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename=hope-iatry-users.csv'
    }

if __name__ == '__main__':
    print("=" * 70)
    print("🌟 Hope-iatry AI Coaching Platform - Backend Server")
    print("=" * 70)
    print()
    
    if GROQ_API_KEY:
        masked_key = f"{GROQ_API_KEY[:10]}...{GROQ_API_KEY[-5:]}"
        print(f"✅ Groq API Key configured: {masked_key}")
    else:
        print("⚠️  WARNING: GROQ_API_KEY not set!")
        print("   Create a .env file with: GROQ_API_KEY=your_key_here")
        print("   Get free API key from: https://console.groq.com")
    
    print(f"✅ Model: {MODEL}")
    print()
    print("📡 Server Configuration:")
    print("   • Local access: http://127.0.0.1:5000")
    print("   • Network access: http://YOUR_IP_ADDRESS:5000")
    print()
    print("🔌 Endpoints:")
    print("   • GET  /              - Main application")
    print("   • GET  /health        - Health check")
    print("   • POST /api/register  - Register user")
    print("   • POST /api/chat      - Chat endpoint")
    print("   • GET  /api/admin/users - Get all users (admin)")
    print("   • GET  /api/admin/export - Export users CSV")
    print()
    print("=" * 70)
    print()
    print("🚀 Starting server...")
    print()
    
    # Run on all network interfaces so others can access
    app.run(host='0.0.0.0', port=5001, debug=True)
