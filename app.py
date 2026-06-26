from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def view():
    meals_name = request.args.get("meals_name")
    meal_name = None
    strInstructions = ""
    strCategory = None
    strArea = None
    strCountry = None
    strMealThumb = None
    strYoutube = None
    message = None
    if meals_name:
        try:
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={meals_name}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data["meals"]:
                    meal_name = data["meals"][0]["strMeal"]
                    strInstructions = data["meals"][0]["strInstructions"]
                    strCategory = data["meals"][0]["strCategory"]
                    strArea = data["meals"][0]["strArea"]
                    strCountry = data["meals"][0]["strCountry"]
                    strMealThumb = data["meals"][0]["strMealThumb"]
                    strYoutube = data["meals"][0]["strYoutube"]

                else:
                    message = "Recipes Not Found."
        except Exception as e:
            print(e)
    return render_template("index.html",
                           meal_name=meal_name,
                           strInstructions=strInstructions,
                           strCategory=strCategory,
                           strArea=strArea,
                           strCountry=strCountry,
                           strMealThumb=strMealThumb,
                           strYoutube=strYoutube,
                           message=message)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
