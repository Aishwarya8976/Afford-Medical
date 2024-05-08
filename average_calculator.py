import requests
from flask import Flask, render_template, request

app = Flask(__name__)

window_size = 10
stored_numbers = []
prev_window_state = []


def fetch_numbers(number_type):
    url = f"http://20.244.56.144/test/{number_type}"
    headers = {"Authorization": "Bearer CALCULATOR"}  
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("numbers", [])
    return []

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def update_state(new_numbers):
    global stored_numbers, prev_window_state
    stored_numbers.extend(new_numbers)
    if len(stored_numbers) > window_size:
        prev_window_state = stored_numbers[:window_size]
        stored_numbers = stored_numbers[-window_size:]

@app.route('/numbers/<numberid>')
def get_numbers(numberid):
    global stored_numbers, prev_window_state
    new_numbers = []

    if numberid == 'p':
        new_numbers = fetch_numbers('primes')
    elif numberid == 'f':
        new_numbers = fetch_numbers('fibo')
    elif numberid == 'e':
        new_numbers = fetch_numbers('even')
    elif numberid == 'r':
        new_numbers = fetch_numbers('rand')

    
    update_state(new_numbers)

    average = calculate_average(stored_numbers)

    return render_template('response.html',
                           windowPrevState=prev_window_state,
                           windowCurrState=stored_numbers,
                           numbers=new_numbers,
                           avg=round(average, 2))

if __name__ == '__main__':
    app.run(debug=True)
