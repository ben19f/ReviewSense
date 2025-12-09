document.getElementById("sendBtn").addEventListener("click", async () => {
    const text = document.getElementById("feedbackInput").value;

    const res = await fetch("http://127.0.0.1:8000/api/feedback/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ text })
    });

    const data = await res.json();
    console.log("Saved feedback:", data);
});