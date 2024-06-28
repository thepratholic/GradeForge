from flask import Flask, render_template, request

app = Flask(__name__)

class GradeSheet:
    def calculate_marks(self, specialization, marks):
        if specialization == "DE":
            diploma_spi = sum(marks)
            diploma_cpi = sum(marks) / 6
            diploma_cgpa = sum(marks[2:]) / 4

            return {
                "total_spi": diploma_spi,
                "cpi": diploma_cpi,
                "cgpa": diploma_cgpa
            }

        else:
            degree_spi = sum(marks)
            degree_cpi = sum(marks) / 8
            degree_cgpa = sum(marks[2:6]) / 4

            return {
                "total_spi": degree_spi,
                "cpi": degree_cpi,
                "cgpa": degree_cgpa
            }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    specialization = request.form['specialization']
    marks = [float(request.form[f'sem_{i}']) for i in range(1, 9 if specialization == 'BE' else 7)]
    gs = GradeSheet()
    results = gs.calculate_marks(specialization, marks)
    eligibility = results['cgpa'] >= 5.5

    return render_template('index.html', results=results, eligibility=eligibility)

if __name__ == "__main__":
    app.run(debug=True)