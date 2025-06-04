const boardElem = document.getElementById('board');
const statusElem = document.getElementById('status');
const restartBtn = document.getElementById('restart');
const pvpBtn = document.getElementById('pvp');
const cpuBtn = document.getElementById('cpu');

let board, currentPlayer, gameActive, mode;

const WIN_COMBOS = [
    [0,1,2],[3,4,5],[6,7,8], // rows
    [0,3,6],[1,4,7],[2,5,8], // cols
    [0,4,8],[2,4,6]          // diags
];

function initBoard() {
    board = Array(9).fill('');
    currentPlayer = 'X';
    gameActive = true;
    statusElem.textContent = `Player X's turn`;
    renderBoard();
}

function renderBoard() {
    boardElem.innerHTML = '';
    board.forEach((cell, idx) => {
        const cellElem = document.createElement('div');
        cellElem.className = 'cell';
        cellElem.textContent = cell;
        cellElem.addEventListener('click', () => handleCellClick(idx));
        boardElem.appendChild(cellElem);
    });
}

function handleCellClick(idx) {
    if (!gameActive || board[idx]) return;
    board[idx] = currentPlayer;
    renderBoard();
    if (checkWin(currentPlayer)) {
        statusElem.textContent = `Player ${currentPlayer} wins!`;
        gameActive = false;
        return;
    }
    if (board.every(cell => cell)) {
        statusElem.textContent = "It's a draw!";
        gameActive = false;
        return;
    }
    if (mode === 'cpu' && currentPlayer === 'X') {
        currentPlayer = 'O';
        statusElem.textContent = `CPU's turn`;
        setTimeout(cpuMove, 500);
    } else {
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        statusElem.textContent = `Player ${currentPlayer}'s turn`;
    }
}

function checkWin(player) {
    return WIN_COMBOS.some(combo => combo.every(idx => board[idx] === player));
}

function cpuMove() {
    if (!gameActive) return;
    // Simple AI: win, block, or random
    let move = findBestMove('O') || findBestMove('X') || randomMove();
    board[move] = 'O';
    renderBoard();
    if (checkWin('O')) {
        statusElem.textContent = `CPU wins!`;
        gameActive = false;
        return;
    }
    if (board.every(cell => cell)) {
        statusElem.textContent = "It's a draw!";
        gameActive = false;
        return;
    }
    currentPlayer = 'X';
    statusElem.textContent = `Player X's turn`;
}

function findBestMove(player) {
    for (let combo of WIN_COMBOS) {
        const [a, b, c] = combo;
        const line = [board[a], board[b], board[c]];
        if (line.filter(x => x === player).length === 2 && line.includes('')) {
            return combo[line.indexOf('')];
        }
    }
    return null;
}

function randomMove() {
    const empty = board.map((cell, idx) => cell ? null : idx).filter(x => x !== null);
    return empty[Math.floor(Math.random() * empty.length)];
}

restartBtn.addEventListener('click', initBoard);
pvpBtn.addEventListener('click', () => {
    mode = 'pvp';
    initBoard();
});
cpuBtn.addEventListener('click', () => {
    mode = 'cpu';
    initBoard();
});

// Default mode
mode = 'pvp';
initBoard();
