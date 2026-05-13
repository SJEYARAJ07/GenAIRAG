const API_BASE = process.env.REACT_APP_API_BASE_URL || "http://localhost:8001";

//export async function askQuestion(question) {
//  const response = await fetch(`${API_BASE}/ask`, {
//    method: "POST",
//    headers: {
//      "Content-Type": "application/json",
//    },
//    body: JSON.stringify({ query: question }),
//  });
//
//  if (!response.ok) {
//    const text = await response.text();
//    throw new Error(text || `Request failed with status ${response.status}`);
//  }
//
//  return response.json();
//}

export async function askQuestion(question, docId = null) {
  const response = await fetch(`${API_BASE}/ask`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      query: question,
      doc_id: docId,
    }),
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(text || `Request failed with status ${response.status}`);
  }

  return response.json();
}