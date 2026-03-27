from flask import Flask, jsonify, render_template,redirect
import requests,random

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cat")
def get_cat():
  try:
    url = "https://cataas.com/cat?json=true"
    response = requests.get(url, timeout=5)
    if response.status_code!=200:
      return jsonify({"error":"Failed to fetch cat"}),500
    data = response.json()
    # Cataas doesn't have "status"
    if "url" not in data:
        return jsonify({"error": "Invalid cat response"}), 500
    # data contains cat in url
    if data["url"].startswith("http"):
        cat_url = data["url"]
    else:
        cat_url = "https://cataas.com" + data["url"]

    return jsonify({"image": cat_url})
  except Exception as e:
     return jsonify({"error":"server error"}),500

@app.route("/dog")
def get_dog():
  try:
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url, timeout=5)
    if response.status_code != 200:
      return jsonify({"error":"Failed to fetch dog"}),500
    data = response.json()
    if data.get("status")!="success":
      return jsonify({"error":"Dog api error"}),500
    dog_url = data["message"] 
    return jsonify({"image": dog_url})
  except Exception as e:
    return jsonify({"error":"Server error"}),500

@app.route("/fox")
def get_fox():
    try:
        response = requests.get("https://randomfox.ca/floof/", timeout=5)
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch fox"}), 500
        
        data = response.json()
        if "image" not in data:
            return jsonify({"error": "Invalid fox response"}), 500
        fox_url = data["image"]
        return jsonify({"image": fox_url})

    except Exception as e:
        print(e)  # helpful for debugging
        return jsonify({"error": "Fox API failed"}), 500  # helpful for debugging
      
    
@app.route("/panda")
def get_panda():
    try:
        response = requests.get("https://some-random-api.com/animal/panda", timeout=5)
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch panda"}), 500
        data = response.json()
        if "image" not in data:
            return jsonify({"error": "Invalid panda response"}), 500
        panda_url = data["image"]
        return jsonify({"image": panda_url})

    except Exception as e:
        print(e)  # helpful for debugging
        return jsonify({"error": "Panda API failed"}), 500
    

@app.route("/random")
def get_random():
    choice = random.choice(["cat", "dog", "fox", "panda"])
    return redirect(f"/{choice}")

if __name__ == "__main__":
    app.run(debug=True)
