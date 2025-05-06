document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('taskForm');
    const taskList = document.getElementById('taskList');

    // Load tasks on startup
    fetch('/api/tasks')
        .then(res => res.json())
        .then(tasks => renderTasks(tasks));

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const newTask = {
            title: document.getElementById('title').value,
            description: document.getElementById('description').value
        };

        fetch('/api/tasks', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(newTask)
        })
        .then(() => location.reload());
    });

    function renderTasks(tasks) {
        taskList.innerHTML = tasks.map(task => `
            <div class="task">
                <h3>${task.title}</h3>
                <p>${task.description}</p>
                <button onclick="deleteTask(${task.id})">Complete</button>
            </div>
        `).join('');
    }
});

function deleteTask(id) {
    fetch(`/api/tasks/${id}`, { method: 'DELETE' })
        .then(() => location.reload());
}