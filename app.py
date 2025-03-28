from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "YOUR_SECRET_KEY_HERE"

class GradeCalculator:
    def calculate(self, program, marks):
        num_semesters = len(marks)
        total_spi = sum(marks)
        cpi = total_spi / num_semesters
        cgpa = cpi
        percentage = (cpi / 10) * 100
        return {
            "total_spi": round(total_spi, 2),
            "cpi": round(cpi, 2),
            "cgpa": round(cgpa, 2),
            "percentage": round(percentage, 2)
        }

@app.route('/', methods=['GET', 'POST'])
def index():
    semesters_map = {
        "DE": 6,
        "BE": 8,
        "ME": 4
    }

    if request.method == 'POST':
        program = request.form.get('program', 'DE')
        
        # Determine number of semesters
        if program == 'GEN':
            try:
                num_semesters = int(request.form.get('num_semesters', '0'))
                if num_semesters <= 0:
                    raise ValueError
            except ValueError:
                session['error'] = "Please enter a valid number of semesters for Generic program."
                return redirect(url_for('index'))
        else:
            num_semesters = semesters_map.get(program, 6)
        
        # Validate and parse semester marks
        marks = []
        for i in range(1, num_semesters + 1):
            field_name = f'sem_{i}'
            sem_val_str = request.form.get(field_name, '').strip()
            if not sem_val_str:
                session['error'] = "All semester marks must be filled in."
                return redirect(url_for('index'))
            try:
                sem_val = float(sem_val_str)
            except ValueError:
                session['error'] = "Please enter valid numeric SPI values for all semesters."
                return redirect(url_for('index'))
            marks.append(sem_val)

        # Calculate
        calc = GradeCalculator()
        results = calc.calculate(program, marks)
        eligibility = results['cgpa'] >= 5.5

        # Store in session, then redirect
        session['results'] = results
        session['eligibility'] = eligibility
        return redirect(url_for('index'))

    # GET request: retrieve data from session, then pop it out
    results = session.pop('results', None)
    eligibility = session.pop('eligibility', None)
    error = session.pop('error', None)
    return render_template('index.html', results=results, eligibility=eligibility, error=error)

if __name__ == "__main__":
    app.run(debug=True)
