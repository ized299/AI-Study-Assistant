import {useState} from 'react';
import ReactMarkdown from 'react-markdown';
import Quiz from './components/Quiz';
import Flashcards from './components/Flashcards';

function App() {
  const [question, setQuestion] = useState("");
  const [task, setTask] =useState("explain");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateResponse = async () => {
    setLoading(true);
    const response =await fetch("http://localhost:8000/ask-ai", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
      question: question,
      task: task,
      }),
    });
    const data = await response.json();
    setResponse(data);
    setLoading(false);
  };
  return (
    <div>
      <h1>AI Study Assistant</h1>
      <p>Learn smarter with AI!</p>

      <textarea
        placeholder="Type your questions or topic here..."
        rows="5"
        value={question}
        onChange ={(event) => setQuestion(event.target.value)}
      />
      <div>
        <button onClick={() => setTask("explain")}>Explain</button>
        <button onClick={() => setTask("quiz")}>Quiz</button>
        <button onClick={() => setTask("summarize")}>Summarize</button>
        <button onClick={() => setTask("flashcards")}>Flashcards </button>
      </div>

      <button onClick={generateResponse} disabled={loading}>
        {loading ? "Generating..." : "Generate"}
      </button>

      {response && (
        <div>
          <h2>Result</h2>
          {task === "quiz" ? (
            <Quiz quiz={response.response} />
          ) : task === "flashcards" ? (
            <Flashcards flashcards={response.response} />
          ) : (
            <ReactMarkdown>{response.response}</ReactMarkdown>
          )}
        </div>
      )}

    </div>
  );
}
export default App;