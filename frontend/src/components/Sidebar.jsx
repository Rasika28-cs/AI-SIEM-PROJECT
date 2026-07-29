import { Link } from "react-router-dom";

function Sidebar() {
  return (
    <div
      style={{
        width: "220px",
        background: "#1e293b",
        color: "white",
        minHeight: "100vh",
        padding: "20px",
      }}
    >
      <h2>AI SIEM</h2>

      <hr />

      <p><Link to="/dashboard">Dashboard</Link></p>

      <p><Link to="/logs">Logs</Link></p>

      <p><Link to="/alerts">Alerts</Link></p>

      <p><Link to="/agents">Agents</Link></p>
    </div>
  );
}

export default Sidebar;