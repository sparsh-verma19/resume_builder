from flask import Flask, render_template, request
from fpdf import FPDF

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = request.form
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt=f"{data['name']}'s Resume", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Email: {data['email']}", ln=True)
        pdf.cell(200, 10, txt=f"Phone: {data['phone']}", ln=True)
        pdf.cell(200, 10, txt=f"Skills: {data['skills']}", ln=True)
        pdf.multi_cell(0, 10, txt=f"Education: {data['education']}")
        pdf.multi_cell(0, 10, txt=f"Experience: {data['experience']}")

        pdf.output("static/resume.pdf")

        return render_template("resume.html", name=data['name'])

    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)
