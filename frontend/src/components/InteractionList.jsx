import { useSelector } from "react-redux";

import InteractionCard from "./InteractionCard";

function InteractionList() {
  const { items, loading, error } = useSelector((state) => state.interactions);

  return (
    <section className="interaction-section">
      <div className="section-title">
        <div>
          <p className="eyebrow dark">CRM Records</p>
          <h2>Logged Interactions</h2>
        </div>

        <span className="count-badge">{items.length} records</span>
      </div>

      {loading && <p>Loading interactions...</p>}

      {error && <p className="error-text">{error}</p>}

      {!loading && items.length === 0 && (
        <div className="empty-state">
          <h3>No interactions logged yet</h3>
          <p>Use the structured form or AI chat logger to create your first HCP record.</p>
        </div>
      )}

      <div className="interaction-grid">
        {items.map((interaction) => (
          <InteractionCard
            key={interaction.id}
            interaction={interaction}
          />
        ))}
      </div>
    </section>
  );
}

export default InteractionList;