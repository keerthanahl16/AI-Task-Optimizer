from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/predict', methods=['POST'])  # Must allow POST
def predict():
    data = request.get_json()
    if not data or 'taskDesc' not in data or 'category' not in data:
        return jsonify({"error": "Invalid request"}), 400

    skill_map = {
        "Backend": "Python, Java, Node.js, Kotlin, Rust, Spring Boot",
        "Frontend": "HTML, CSS, JavaScript, React",
        "Data Science": "Python, Machine Learning, Pandas",
        "DevOps": "Docker, Kubernetes, AWS"
    }
    
    category = data['category']
    predicted_skill = skill_map.get(category, "General Programming")

    return jsonify({"skill": predicted_skill})

if __name__ == '__main__':
    app.run(debug=True)
