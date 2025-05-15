async function fetchNotes() {
    const res = await fetch('/notes');
    const notes = await res.json();
    const notesDiv = document.getElementById('notes');
    notesDiv.innerHTML = '';
    notes.forEach(note => {
        notesDiv.innerHTML += `
            <div class="note-card" id="note-${note.id}">
                <div class="note-title">${note.title}</div>
                <div class="note-content">${note.content}</div>
                <div class="note-actions">
                    <button class="edit" onclick="editNote(${note.id}, '${encodeURIComponent(note.title)}', '${encodeURIComponent(note.content)}')">Edit</button>
                    <button class="delete" onclick="deleteNote(${note.id})">Delete</button>
                </div>
            </div>
        `;
    });
}

async function deleteNote(id) {
    await fetch('/notes/' + id, { method: 'DELETE' });
    fetchNotes();
}

function editNote(id, title, content) {
    title = decodeURIComponent(title);
    content = decodeURIComponent(content);
    document.getElementById('title').value = title;
    document.getElementById('content').value = content;
    document.getElementById('noteForm').onsubmit = async function(e) {
        e.preventDefault();
        const newTitle = document.getElementById('title').value;
        const newContent = document.getElementById('content').value;
        await fetch('/notes/' + id, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: newTitle, content: newContent })
        });
        this.reset();
        this.onsubmit = addNoteHandler;
        fetchNotes();
    };
}

async function addNoteHandler(e) {
    e.preventDefault();
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;
    await fetch('/notes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, content })
    });
    this.reset();
    fetchNotes();
}

document.getElementById('noteForm').onsubmit = addNoteHandler;

fetchNotes();