from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)


@app.route("/")
def my_site():
    return render_template("index.html")


@app.route("/<page_name>")
def my_site_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('databse.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csvwriter = csv.writer(database, delimiter=',',
                               quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')


if __name__ == "__main__":
    app.run(debug=True)
