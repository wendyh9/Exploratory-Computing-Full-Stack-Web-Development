// calculate function
const calculate = (firstNum, secondNum, operator) => {
    // need to convert from str to float
    const num1 = parseFloat(firstNum)
    const num2 = parseFloat(secondNum)
    
    if (operator === 'add') {
      return num1 + num2
    }
    else if (operator === 'subtract') {
      return num1 - num2
    }
    else if (operator === 'multiply') {
      return num1 * num2
    }
    else if (operator === 'divide') {
      return num1 / num2
    }
    
  }
  
  const calculator = document.querySelector('.calculator')
  const display = document.querySelector('.calculator-display')
  const btns = calculator.querySelector('.calculator-buttons')
  
  
  btns.addEventListener('click', e => {
    if (e.target.matches('button')) {
      const btn = e.target
      const action = btn.dataset.action
      // value of button that's pressed
      const btnContent = btn.textContent
      // what is displayed in calculator screen
      const displayedNum = display.textContent
      // keep track of previous button type
      const previousBtnType = calculator.dataset.previousBtnType

      Array.from(btn.parentNode.children)
        .forEach(b => b.classList.remove('highlighted'))
      
      if (!action) {
        // console.log('number button')
        if (displayedNum === '0' || previousBtnType === 'operator' || previousBtnType === 'calculate') {
          display.textContent = btnContent
        }
        // append number to non-zero number
        else {
          display.textContent = displayedNum + btnContent
        }
        calculator.dataset.previousBtnType = 'number'
      }
      
      if (action === 'add' || action === 'subtract' || action === 'multiply' || action === 'divide') {
        // add custom attribute to keep track of previous button type
        const firstVal = calculator.dataset.firstVal
        const secondVal = displayedNum
        const operator = calculator.dataset.operator
         // console.log('operator button')
        
        if (firstVal && operator && previousBtnType !== 'operator' && previousBtnType !== 'calculate') {
          const calcVal = calculate(firstVal, secondVal, operator)
          display.textContent = calcVal
          // update calculated value as first value
          calculator.dataset.firstVal = calcVal
        }
        // if no calculations, set displayedNum as the firstVal
        else {
          calculator.dataset.firstVal = displayedNum
        }
        btn.classList.add('highlighted')
        calculator.dataset.previousBtnType = 'operator'
        calculator.dataset.operator = action
      }
      
      // check if there is already a decimal   
      if (action === 'decimal') {
        if (!displayedNum.includes('.')) {
            display.textContent = displayedNum + '.' 
        }
        else if (previousBtnType === 'operator' || previousBtnType === 'calculate') {
          display.textContent = '0.'
        }
        
        calculator.dataset.previousBtnType = 'decimal'
      }
  
      if (action === 'clear') {
        // console.log('clear button')
        if (btn.textContent === 'C') {
          calculator.dataset.firstVal = ''
          calculator.dataset.modVal = ''
          calculator.dataset.operator = ''
          calculator.dataset.previousBtnType = ''
        }
        else {
          btn.textContent = 'C'
        }
        display.textContent = 0
        calculator.dataset.previousBtnType = 'clear'
      }
      
      if (action !== 'clear') {
        const clearButton = calculator.querySelector('[data-action=clear]')
        clearButton.textContent = 'CE'
      }
  
      if (action === 'calculate') {
        // console.log('equal button')
        let firstVal = calculator.dataset.firstVal
        let secondVal = displayedNum
        const operator = calculator.dataset.operator
        
        if (firstVal) {
          if (previousBtnType === 'calculate') {
            firstVal = displayedNum
            secondVal = calculator.dataset.modVal
          }
          display.textContent = calculate(firstVal, secondVal, operator)
        }
        
        calculator.dataset.previousBtnType = 'calculate'
        calculator.dataset.modVal = secondVal
      }    
   }
})
  