document.addEventListener('DOMContentLoaded', function () {
    const display = document.getElementById('display');
    let current = '';
    let resetNext = false;

    function updateDisplay(val) {
        display.value = val;
    }

    function appendValue(val) {
        if (resetNext) {
            current = '';
            resetNext = false;
        }
        if (current === '0' && val !== '.') {
            current = val;
        } else {
            current += val;
        }
        updateDisplay(current);
    }

    function clearDisplay() {
        current = '';
        updateDisplay('0');
    }

    function calculate() {
        try {
            // Only allow numbers and operators
            if (/^[0-9+\-*/. ]+$/.test(current)) {
                // eslint-disable-next-line no-eval
                let result = eval(current);
                updateDisplay(result);
                current = result.toString();
                resetNext = true;
            } else {
                updateDisplay('Err');
                current = '';
                resetNext = true;
            }
        } catch {
            updateDisplay('Err');
            current = '';
            resetNext = true;
        }
    }

    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('click', function () {
            const val = this.getAttribute('data-value');
            if (this.id === 'clear') {
                clearDisplay();
            } else if (this.id === 'equals') {
                calculate();
            } else if (val) {
                appendValue(val);
            }
        });
    });

    clearDisplay();
});
