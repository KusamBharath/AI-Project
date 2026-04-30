import { useEffect } from "react";
import { useDispatch } from "react-redux";

import { fetchInteractions } from "../features/interactions/interactionSlice";
import LogInteractionForm from "../components/LogInteractionForm";
import ChatLogger from "../components/ChatLogger";
import InteractionList from "../components/InteractionList";

function Dashboard() {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchInteractions());
  }, [dispatch]);

  return (
    <main className="dashboard">
      <section className="hero-section">
        <p className="eyebrow">AI-First CRM</p>
        <h1>HCP Interaction Logger</h1>
        <p>
          Log Healthcare Professional interactions using a structured form or
          AI-powered conversational assistant.
        </p>
      </section>

      <section className="grid-layout">
        <LogInteractionForm />
        <ChatLogger />
      </section>

      <InteractionList />
    </main>
  );
}

export default Dashboard;