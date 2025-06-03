document.getElementById('cityForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const city = document.getElementById('cityInput').value.trim();
    if (!city) return;
    const list = document.getElementById('timeList');
    list.innerHTML = '';
    try {
        const response = await fetch(`/time/${encodeURIComponent(city)}`);
        if (!response.ok) {
            const data = await response.json();
            const li = document.createElement('li');
            li.className = 'error';
            li.textContent = data.detail || 'Error fetching time.';
            list.appendChild(li);
            return;
        }
        const data = await response.json();
        const li = document.createElement('li');
        li.innerHTML = `<strong>City:</strong> ${data.city}<br><strong>Time:</strong> ${data.time}<br><strong>Timezone:</strong> ${data.timezone}`;
        list.appendChild(li);
    } catch (err) {
        const li = document.createElement('li');
        li.className = 'error';
        li.textContent = 'Network error.';
        list.appendChild(li);
    }
});
