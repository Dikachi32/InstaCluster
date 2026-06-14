from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load saved model and scaler
MODEL_PATH = 'instagram_kmeans_model.pkl'
SCALER_PATH = 'instagram_scaler.pkl'

km_model = joblib.load(MODEL_PATH)
scaler   = joblib.load(SCALER_PATH)

# Human-readable cluster descriptions based on your 5-cluster KMeans
CLUSTER_INFO = {
    0: {
        "name": "Casual Browsers",
        "color": "#EF4444",
        "description": "Low visit frequency and low spending rank. These users occasionally browse Instagram but rarely make purchases.",
        "insight": "Low engagement, low conversion potential. Consider re-engagement campaigns."
    },
    1: {
        "name": "Window Shoppers",
        "color": "#3B82F6",
        "description": "Moderate Instagram visits but low spending. They explore content without committing to purchases.",
        "insight": "High visit interest but low spend — ideal targets for discount or incentive campaigns."
    },
    2: {
        "name": "High-Value Engagers",
        "color": "#22C55E",
        "description": "High visit frequency paired with high spending rank. These are your most valuable customers.",
        "insight": "Top-tier segment. Prioritise retention, loyalty rewards and premium offers."
    },
    3: {
        "name": "Passive Spenders",
        "color": "#06B6D4",
        "description": "Low visit scores but surprisingly high spending rank. They buy without heavy browsing.",
        "insight": "Efficient converters — targeted direct offers will resonate well with this group."
    },
    4: {
        "name": "Active Explorers",
        "color": "#EC4899",
        "description": "High Instagram activity with moderate spending. Very engaged but selective buyers.",
        "insight": "Great for brand awareness. Nurture with quality content to convert exploration into sales."
    },
}


@app.route('/')
def home():
    return render_template('insta.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        visit_score   = float(data['visit_score'])
        spending_rank = float(data['spending_rank'])

        # Validate ranges
        if not (0 <= visit_score <= 100):
            return jsonify({'error': 'Instagram Visit Score must be between 0 and 100.'}), 400
        if not (0 <= spending_rank <= 100):
            return jsonify({'error': 'Spending Rank must be between 0 and 100.'}), 400

        # Scale input the same way the model was trained
        input_df = pd.DataFrame({
            'Instagram visit score':    [visit_score],
            'Spending_rank(0 to 100)': [spending_rank]
        })
        scaled_input = scaler.transform(input_df)

        # Predict
        cluster_label = int(km_model.predict(scaled_input)[0])
        info = CLUSTER_INFO.get(cluster_label, {
            "name": f"Cluster {cluster_label + 1}",
            "color": "#94A3B8",
            "description": "No description available.",
            "insight": ""
        })

        # Distance to each centroid (confidence proxy)
        distances = np.linalg.norm(km_model.cluster_centers_ - scaled_input, axis=1)
        closest_dist   = float(distances[cluster_label])
        max_dist       = float(distances.max())
        confidence_pct = round((1 - closest_dist / (max_dist + 1e-9)) * 100, 1)

        return jsonify({
            'cluster':     cluster_label,
            'cluster_num': cluster_label + 1,
            'name':        info['name'],
            'color':       info['color'],
            'description': info['description'],
            'insight':     info['insight'],
            'confidence':  confidence_pct,
            'visit_score':   visit_score,
            'spending_rank': spending_rank
        })

    except (KeyError, ValueError) as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.route('/clusters', methods=['GET'])
def clusters():
    """Return all cluster information for the info panel."""
    return jsonify(CLUSTER_INFO)


if __name__ == '__main__':
    app.run(debug=True)