import { useState } from "react";
import { useDispatch } from "react-redux";

import { updateInteraction } from "../features/interactions/interactionSlice";

function EditInteractionModal({ interaction, onClose }) {
  const dispatch = useDispatch();

  const [formData, setFormData] = useState({
    hcp_name: interaction.hcp_name || "",
    specialty: interaction.specialty || "",
    organization: interaction.organization || "",
    interaction_type: interaction.interaction_type || "",
    interaction_date: interaction.interaction_date || "",
    products_discussed: interaction.products_discussed || "",
    notes: interaction.notes || "",
    ai_summary: interaction.ai_summary || "",
    sentiment: interaction.sentiment || "neutral",
    samples_given: interaction.samples_given || false,
    follow_up_required: interaction.follow_up_required || false,
    next_follow_up_date: interaction.next_follow_up_date || "",
    next_best_action: interaction.next_best_action || "",
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleUpdate = (e) => {
    e.preventDefault();

    const payload = {
      ...formData,
      next_follow_up_date: formData.next_follow_up_date || null,
    };

    dispatch(
      updateInteraction({
        id: interaction.id,
        interactionData: payload,
      })
    );

    onClose();
  };

  return (
    <div className="modal-backdrop">
      <div className="modal-card">
        <div className="modal-header">
          <h2>Edit Interaction</h2>
          <button type="button" className="secondary" onClick={onClose}>
            Close
          </button>
        </div>

        <form onSubmit={handleUpdate} className="form-grid">
          <div className="form-group">
            <label>HCP Name</label>
            <input
              name="hcp_name"
              value={formData.hcp_name}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Specialty</label>
            <input
              name="specialty"
              value={formData.specialty}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Organization</label>
            <input
              name="organization"
              value={formData.organization}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Interaction Type</label>
            <input
              name="interaction_type"
              value={formData.interaction_type}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Interaction Date</label>
            <input
              type="date"
              name="interaction_date"
              value={formData.interaction_date}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Products Discussed</label>
            <input
              name="products_discussed"
              value={formData.products_discussed}
              onChange={handleChange}
            />
          </div>

          <div className="form-group full">
            <label>Notes</label>
            <textarea
              name="notes"
              value={formData.notes}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group full">
            <label>Summary</label>
            <textarea
              name="ai_summary"
              value={formData.ai_summary}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Sentiment</label>
            <select
              name="sentiment"
              value={formData.sentiment}
              onChange={handleChange}
            >
              <option value="positive">Positive</option>
              <option value="neutral">Neutral</option>
              <option value="negative">Negative</option>
            </select>
          </div>

          <div className="form-group">
            <label>Next Follow-up Date</label>
            <input
              type="date"
              name="next_follow_up_date"
              value={formData.next_follow_up_date}
              onChange={handleChange}
            />
          </div>

          <div className="form-group full">
            <label>Next Best Action</label>
            <textarea
              name="next_best_action"
              value={formData.next_best_action}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>
              <input
                type="checkbox"
                name="samples_given"
                checked={formData.samples_given}
                onChange={handleChange}
              />
              {" "}Samples Given
            </label>
          </div>

          <div className="form-group">
            <label>
              <input
                type="checkbox"
                name="follow_up_required"
                checked={formData.follow_up_required}
                onChange={handleChange}
              />
              {" "}Follow-up Required
            </label>
          </div>

          <div className="actions full">
            <button type="submit">Update Interaction</button>
            <button type="button" className="secondary" onClick={onClose}>
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default EditInteractionModal;