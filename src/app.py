from flask import Flask, render_template, request

app = Flask(__name__)

class GradeSheet:
    def calculate_marks(self, specialization, marks):
        num_semesters = len(marks)
        total_marks = sum(marks)
        
        if specialization == "DE":
            diploma_spi = total_marks
            diploma_cpi = total_marks / 6
            diploma_cgpa = sum(marks[2:]) / 4

            # Assuming each semester is out of 10, change if needed
            total_percentage = (total_marks / (10 * num_semesters)) * 100

            return {
                "total_spi": diploma_spi,
                "cpi": diploma_cpi,
                "cgpa": diploma_cgpa,
                "percentage": total_percentage
            }

        elif specialization == "BE":
            degree_spi = total_marks
            degree_cpi = total_marks / 8
            degree_cgpa = sum(marks[2:6]) / 4

            # Assuming each semester is out of 10, change if needed
            total_percentage = (total_marks / (10 * num_semesters)) * 100

            return {
                "total_spi": degree_spi,
                "cpi": degree_cpi,
                "cgpa": degree_cgpa,
                "percentage": total_percentage
            }

        elif specialization == "ME":
            me_spi = total_marks
            me_cpi = total_marks / 4
            me_cgpa = total_marks / 4

            # Assuming each semester is out of 10, change if needed
            total_percentage = (total_marks / (10 * num_semesters)) * 100

            return {
                "total_spi": me_spi,
                "cpi": me_cpi,
                "cgpa": me_cgpa,
                "percentage": total_percentage
            }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    specialization = request.form['specialization']
    num_semesters = 6 if specialization == 'DE' else 8 if specialization == 'BE' else 4
    marks = [float(request.form[f'sem_{i}']) for i in range(1, num_semesters + 1)]
    gs = GradeSheet()
    results = gs.calculate_marks(specialization, marks)
    eligibility = results['cgpa'] >= 5.5

    return render_template('index.html', results=results, eligibility=eligibility)

if __name__ == "__main__":
    app.run(debug=True)

