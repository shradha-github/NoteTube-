const API_URL = "https://your-backend.onrender.com";

async function generateNotes() {
    const url = document.getElementById("url").value;

    const response = await fetch(`${API_URL}/generate-notes`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ youtube_url: url })
    });

    const data = await response.json();

    document.getElementById("output").innerText = data.notes;
}