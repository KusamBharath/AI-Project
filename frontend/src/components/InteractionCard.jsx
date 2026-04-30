import { useState } from "react";
import { useDispatch } from "react-redux";

import { deleteInteraction } from "../features/interactions/interactionSlice";
import EditInteractionModal from "./EditInteractionModal";

function InteractionCard({ interaction }) {
  const dispatch = useDispatch();
  const [showEditModal, setShowEditModal] = useState(false);

  const handleDelete = () => {
    const confirmed = window.confirm(
      `Delete interaction with ${interaction.hcp_name}?`
    );

    if (confirmed) {
      dispatch(deleteInteraction(interaction.id));
    }
  };

  return (
    <>
      <article className="interaction-card">
        <div className="card-header-row">
          <div>
            <h3>{interaction.hcp_name}</h3>
            <p>
              {interaction.specialty || "General"} •{" "}
              {interaction.organization || "Unknown Organization"}
            </p>
          </div>

          <span className="badge">{interaction.sentiment || "neutral"}</span>
        </div>

        <p>
          <strong>Type:</strong> {interaction.interaction_type}
        </p>

        <p>
          <strong>Date:</strong> {interaction.interaction_date}
        </p>

        <p>
          <strong>Product:</strong>{" "}
          {interaction.products_discussed || "Not specified"}
        </p>

        <p>
          <strong>Summary:</strong>{" "}
          {interaction.ai_summary || interaction.notes}
        </p>

        <p>
          <strong>Follow-up:</strong>{" "}
          {interaction.follow_up_required ? "Required" : "Not required"}
        </p>

        {interaction.next_follow_up_date && (
          <p>
            <strong>Next Date:</strong> {interaction.next_follow_up_date}
          </p>
        )}

        {interaction.next_best_action && (
          <p>
            <strong>Next Best Action:</strong> {interaction.next_best_action}
          </p>
        )}

        <div className="actions">
          <button
            type="button"
            className="secondary"
            onClick={() => setShowEditModal(true)}
          >
            Edit
          </button>

          <button className="danger" onClick={handleDelete}>
            Delete
          </button>
        </div>
      </article>

      {showEditModal && (
        <EditInteractionModal
          interaction={interaction}
          onClose={() => setShowEditModal(false)}
        />
      )}
    </>
  );
}

export default InteractionCard;