import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import {
  chatLogInteraction,
  clearAiResult,
} from "../features/interactions/interactionSlice";

function ChatLogger() {
  const [message, setMessage] = useState("");

  const dispatch = useDispatch();
  const { loading, aiResult } = useSelector((state) => state.interactions);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!message.trim()) return;

    dispatch(chatLogInteraction(message));
    setMessage("");
  };

  return (
    <div className="card">
      <h2>AI Chat Logger</h2>

      <form onSubmit={handleSubmit}>
        <div className="form-group full">
          <label>Describe Interaction</label>
          <textarea
            placeholder="Example: I met Dr. Sharma at Apollo Hospital..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
        </div>

        <div className="actions">
          <button type="submit" disabled={loading}>
            {loading ? "Processing..." : "Log with AI"}
          </button>

          {aiResult && (
            <button
              type="button"
              className="secondary"
              onClick={() => dispatch(clearAiResult())}
            >
              Clear
            </button>
          )}
        </div>
      </form>

      {aiResult && (
        <div className="ai-result">
          <strong>AI Response:</strong>
          <p>{aiResult.message}</p>
        </div>
      )}
    </div>
  );
}

export default ChatLogger;