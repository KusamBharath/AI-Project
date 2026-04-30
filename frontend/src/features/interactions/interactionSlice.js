import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

import {
  getInteractionsAPI,
  createInteractionAPI,
  updateInteractionAPI,
  deleteInteractionAPI,
  chatLogInteractionAPI,
} from "./interactionAPI";

export const fetchInteractions = createAsyncThunk(
  "interactions/fetchInteractions",
  async () => {
    return await getInteractionsAPI();
  }
);

export const createInteraction = createAsyncThunk(
  "interactions/createInteraction",
  async (interactionData) => {
    return await createInteractionAPI(interactionData);
  }
);

export const updateInteraction = createAsyncThunk(
  "interactions/updateInteraction",
  async ({ id, interactionData }) => {
    return await updateInteractionAPI(id, interactionData);
  }
);

export const deleteInteraction = createAsyncThunk(
  "interactions/deleteInteraction",
  async (id) => {
    return await deleteInteractionAPI(id);
  }
);

export const chatLogInteraction = createAsyncThunk(
  "interactions/chatLogInteraction",
  async (message) => {
    return await chatLogInteractionAPI(message);
  }
);

const interactionSlice = createSlice({
  name: "interactions",
  initialState: {
    items: [],
    loading: false,
    error: null,
    aiResult: null,
  },
  reducers: {
    clearAiResult: (state) => {
      state.aiResult = null;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchInteractions.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchInteractions.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload;
      })
      .addCase(fetchInteractions.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      })

      .addCase(createInteraction.fulfilled, (state, action) => {
        state.items.unshift(action.payload);
      })

      .addCase(updateInteraction.fulfilled, (state, action) => {
        const index = state.items.findIndex(
          (item) => item.id === action.payload.id
        );

        if (index !== -1) {
          state.items[index] = action.payload;
        }
      })

      .addCase(deleteInteraction.fulfilled, (state, action) => {
        state.items = state.items.filter((item) => item.id !== action.payload);
      })

      .addCase(chatLogInteraction.pending, (state) => {
        state.loading = true;
        state.aiResult = null;
      })
      .addCase(chatLogInteraction.fulfilled, (state, action) => {
        state.loading = false;
        state.aiResult = action.payload;
        state.items.unshift(action.payload.saved_interaction);
      })
      .addCase(chatLogInteraction.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  },
});

export const { clearAiResult } = interactionSlice.actions;
export default interactionSlice.reducer;