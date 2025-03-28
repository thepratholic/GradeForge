document.addEventListener('DOMContentLoaded', () => {
    adjustForm();
    
    // If user changes the program, re-generate fields
    document.getElementById('program').addEventListener('change', adjustForm);
    
    // If user changes the number of semesters for Generic, re-generate
    document.getElementById('num_semesters')?.addEventListener('input', adjustSemesters);
  });
  
  function adjustForm() {
    const program = document.getElementById('program').value;
    const genericField = document.getElementById('genericSemesters');
    
    // Show or hide the custom semesters input for Generic
    if (program === 'GEN') {
      genericField.classList.remove('hidden');
    } else {
      genericField.classList.add('hidden');
    }
    
    adjustSemesters();
  }
  
  function adjustSemesters() {
    const program = document.getElementById('program').value;
    const semestersContainer = document.getElementById('semesters');
    semestersContainer.innerHTML = '';
  
    // Default semester counts
    let numSemesters = 6; 
    if (program === 'BE') {
      numSemesters = 8;
    } else if (program === 'ME') {
      numSemesters = 4;
    } else if (program === 'GEN') {
      const inputVal = document.getElementById('num_semesters').value;
      numSemesters = parseInt(inputVal) || 0;
    }
  
    // Generate pairs of semester inputs
    if (numSemesters > 0) {
      for (let i = 1; i <= numSemesters; i += 2) {
        const rowDiv = document.createElement('div');
        rowDiv.classList.add('flex', 'flex-col', 'sm:flex-row', 'sm:space-x-4');
        
        // First input
        const field1 = document.createElement('div');
        field1.classList.add('flex-1');
        
        const label1 = document.createElement('label');
        label1.setAttribute('for', `sem_${i}`);
        label1.textContent = `Enter SPI for Semester ${i}:`;
        label1.classList.add('block', 'text-sm', 'font-medium', 'text-white', 'mt-2');
        
        const input1 = document.createElement('input');
        input1.type = 'number';
        input1.step = '0.01';
        input1.id = `sem_${i}`;
        input1.name = `sem_${i}`;
        input1.required = true;
        input1.classList.add(
          'mt-1', 'block', 'w-full', 'border', 'border-gray-300',
          'rounded-md', 'py-2', 'px-3', 'focus:outline-none', 'focus:border-indigo-500',
          'hover:shadow-md', 'transition-all'
        );
        
        field1.appendChild(label1);
        field1.appendChild(input1);
        rowDiv.appendChild(field1);
  
        // Second input (if there's another semester in the pair)
        if (i + 1 <= numSemesters) {
          const field2 = document.createElement('div');
          field2.classList.add('flex-1');
          
          const label2 = document.createElement('label');
          label2.setAttribute('for', `sem_${i + 1}`);
          label2.textContent = `Enter SPI for Semester ${i + 1}:`;
          label2.classList.add('block', 'text-sm', 'font-medium', 'text-white', 'mt-2');
          
          const input2 = document.createElement('input');
          input2.type = 'number';
          input2.step = '0.01';
          input2.id = `sem_${i + 1}`;
          input2.name = `sem_${i + 1}`;
          input2.required = true;
          input2.classList.add(
            'mt-1', 'block', 'w-full', 'border', 'border-gray-300',
            'rounded-md', 'py-2', 'px-3', 'focus:outline-none', 'focus:border-indigo-500',
            'hover:shadow-md', 'transition-all'
          );
  
          field2.appendChild(label2);
          field2.appendChild(input2);
          rowDiv.appendChild(field2);
        }
        
        semestersContainer.appendChild(rowDiv);
      }
    }
  }
  