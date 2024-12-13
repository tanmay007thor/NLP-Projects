function analyzeComment() {
    const comment = document.getElementById("comment").value;

    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ comment: comment })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("emotion").innerText = data.emotion;
        document.getElementById("emoji").innerText = data.emoji;
    })
    .catch(error => console.error("Error:", error));
}
