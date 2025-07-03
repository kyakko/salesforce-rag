let history = [];
const API_URL = '/chat';

export async function sendMessage(query) {
    const body = { query, history };
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
    });
    const data = await response.json();
    history.push({ role: 'user', content: query });
    history.push({ role: 'assistant', content: data.answer });
    return data;
}

export function getHistory() {
    return [...history];
}

export function clearHistory() {
    history = [];
}
