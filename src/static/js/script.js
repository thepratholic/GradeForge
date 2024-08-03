document.addEventListener('DOMContentLoaded', (event) => {
    adjustSemesters();
});

function adjustSemesters() {
    const specialization = document.getElementById('specialization').value;
    const semestersContainer = document.getElementById('semesters');
    semestersContainer.innerHTML = '';

    let numSemesters = 6;
    if (specialization === 'BE') {
        numSemesters = 8;
    } else if (specialization === 'ME') {
        numSemesters = 4;
    }

    for (let i = 1; i <= numSemesters; i += 2) {
        const div = document.createElement('div');
        div.classList.add('semesters-pair');

        const label1 = document.createElement('label');
        label1.setAttribute('for', `sem_${i}`);
        label1.textContent = `Enter SPI of semester ${i}:`;
        const input1 = document.createElement('input');
        input1.setAttribute('type', 'number');
        input1.setAttribute('step', '0.01');
        input1.setAttribute('id', `sem_${i}`);
        input1.setAttribute('name', `sem_${i}`);
        input1.required = true;

        div.appendChild(label1);
        div.appendChild(input1);

        if (i + 1 <= numSemesters) {
            const label2 = document.createElement('label');
            label2.setAttribute('for', `sem_${i + 1}`);
            label2.textContent = `Enter SPI of semester ${i + 1}:`;
            const input2 = document.createElement('input');
            input2.setAttribute('type', 'number');
            input2.setAttribute('step', '0.01');
            input2.setAttribute('id', `sem_${i + 1}`);
            input2.setAttribute('name', `sem_${i + 1}`);
            input2.required = true;

            div.appendChild(label2);
            div.appendChild(input2);
        }

        semestersContainer.appendChild(div);
    }
}

