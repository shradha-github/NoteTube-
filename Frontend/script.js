const API_URL = "https://notetube-gtc8.onrender.com";

async function generateNotes() {
    const urlInput = document.getElementById("url");
    const output = document.getElementById("output");
    const url = urlInput.value.trim();

    // 🚫 Step 1: Validate input
    if (!url) {
        alert("Enter a YouTube URL first.");
        return;
    }

    // ⏳ Step 2: Show loading
    output.innerText = "Processing... please wait";

    try {
        console.log("Sending URL:", url);

        const response = await fetch(`${API_URL}/generate-notes`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ youtube_url: url })
        });

        console.log("Response status:", response.status);

        // 🚫 Step 3: Handle backend errors
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();
        console.log("Response data:", data);

        // 🚫 Step 4: Handle missing data
        if (!data.notes) {
            throw new Error("No notes returned from API");
        }

        // ✅ Success
        output.innerText = data.notes;

    } catch (error) {
        console.error("Error:", error);
        output.innerText = "❌ Failed to generate notes. Check backend.";
    }
}