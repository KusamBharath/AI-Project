import apiClient from "../../services/apiClient";

export const getInteractionsAPI = async () => {
  const response = await apiClient.get("/api/interactions");
  return response.data;
};

export const createInteractionAPI = async (interactionData) => {
  const response = await apiClient.post("/api/interactions", interactionData);
  return response.data;
};

export const updateInteractionAPI = async (id, interactionData) => {
  const response = await apiClient.put(`/api/interactions/${id}`, interactionData);
  return response.data;
};

export const deleteInteractionAPI = async (id) => {
  await apiClient.delete(`/api/interactions/${id}`);
  return id;
};

export const chatLogInteractionAPI = async (message) => {
  const response = await apiClient.post("/api/agent/chat-log", { message });
  return response.data;
};