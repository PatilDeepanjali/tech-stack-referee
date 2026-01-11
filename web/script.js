document.getElementById("refereeForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const form = e.target;

    const userData = {
        background: form.background.value,
        time: form.time.value,
        goal: form.goal.value,
        budget: form.budget.value
    };

    const response = await fetch("/compare", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(userData)
    });

    const data = await response.json();

    const resultDiv = document.getElementById("result");
const table = `
<table border="1" cellpadding="8" cellspacing="0">
  <tr><th>Factor</th><th>MERN</th><th>Django</th></tr>
  <tr><td>Learning Curve</td><td>Easy</td><td>Medium</td></tr>
  <tr><td>Backend Structure</td><td>Moderate</td><td>Strong</td></tr>
  <tr><td>Time to MVP</td><td>Fast</td><td>Slower</td></tr>
  <tr><td>Career Depth</td><td>Medium</td><td>High</td></tr>
</table>
`;

resultDiv.innerHTML = `
  <h2>⚖️ Referee Result</h2>

  <p><strong>Referee Confidence:</strong> ${data.confidence}%</p>

  <h3>📊 Trade-offs at a Glance</h3>
  ${table}

  <h3>MERN Stack (Score: ${data.mern.score})</h3>
  <ul>${data.mern.reasons.map(r => `<li>${r}</li>`).join("")}</ul>

  <h3>Django + PostgreSQL (Score: ${data.django.score})</h3>
  <ul>${data.django.reasons.map(r => `<li>${r}</li>`).join("")}</ul>

  <h3>🔍 Referee Verdict</h3>
  <p>${data.verdict}</p>

  <h4>What if your priorities change?</h4>
  <ul>${data.what_if.map(w => `<li>${w}</li>`).join("")}</ul>
`;

});
