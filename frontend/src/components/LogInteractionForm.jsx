import { useState } from "react";
import { useDispatch } from "react-redux";

import { createInteraction } from "../features/interactions/interactionSlice";

const initialForm = {
  hcp_name: "",
  specialty: "",
  organization: "",
  interaction_type: "In-person meeting",
  interaction_date: new Date().toISOString().split("T")[0],
  products_discussed: "",
  notes: "",
  ai_summary: "",
  sentiment: "neutral",
  samples_given: false,
  follow_up_required: false,
  next_follow_up_date: "",
  next_best_action: "",
};

function LogInteractionForm() {
  const [formData, setFormData] = useState(initialForm);
  const dispatch = useDispatch();

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const payload = {
      ...formData,
      next_follow_up_date: formData.next_follow_up_date || null,
    };

    dispatch(createInteraction(payload));
    setFormData(initialForm);
  };

  return (
    <div className="card">
      <h2>Structured Log Form</h2>

      <form onSubmit={handleSubmit} className="form-grid">
        <div className="form-group">
          <label>HCP Name *</label>
          <input
            name="hcp_name"
            value={formData.hcp_name}
            onChange={handleChange}
            placeholder="Dr. Rajesh Sharma"
            required
          />
        </div>

        <div className="form-group">
          <label>Specialty</label>
          <input
            name="specialty"
            value={formData.specialty}
            onChange={handleChange}
            placeholder="Cardiologist"
          />
        </div>

        <div className="form-group">
          <label>Organization</label>
          <input
            name="organization"
            value={formData.organization}
            onChange={handleChange}
            placeholder="Apollo Hospital"
          />
        </div>

        <div className="form-group">
          <label>Interaction Type *</label>
          <select
            name="interaction_type"
            value={formData.interaction_type}
            onChange={handleChange}
            required
          >
            <option>In-person meeting</option>
            <option>Phone call</option>
            <option>Email</option>
            <option>Conference</option>
            <option>Virtual meeting</option>
          </select>
        </div>

        <div className="form-group">
          <label>Interaction Date *</label>
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
            placeholder="CardioPlus"
          />
        </div>

        <div className="form-group full">
          <label>Notes *</label>
          <textarea
            name="notes"
            value={formData.notes}
            onChange={handleChange}
            placeholder="Enter interaction notes..."
            required
          />
        </div>

        <div className="form-group full">
          <label>AI Summary / Manual Summary</label>
          <textarea
            name="ai_summary"
            value={formData.ai_summary}
            onChange={handleChange}
            placeholder="Short summary..."
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
            placeholder="Schedule follow-up and share clinical evidence..."
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
          <button type="submit">Save Interaction</button>
        </div>
      </form>
    </div>
  );
}

export default LogInteractionForm;