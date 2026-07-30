import { NavLink, useNavigate } from "react-router-dom";
import {
  FaTachometerAlt,
  FaFileAlt,
  FaBell,
  FaDesktop,
  FaSignOutAlt,
} from "react-icons/fa";

import API from "../services/api";
import "../styles/sidebar.css";

function Sidebar() {

  const navigate = useNavigate();

  function logout() {

    API.post("/logout/api/")

      .then(() => {

        navigate("/");

      })

      .catch(console.log);

  }

  return (

    <aside className="sidebar">

      <h2 className="logo">AI SIEM</h2>

      <NavLink to="/dashboard" className="menu-item">
        <FaTachometerAlt />
        <span>Dashboard</span>
      </NavLink>

      <NavLink to="/logs" className="menu-item">
        <FaFileAlt />
        <span>Logs</span>
      </NavLink>

      <NavLink to="/alerts" className="menu-item">
        <FaBell />
        <span>Alerts</span>
      </NavLink>

      <NavLink to="/agents" className="menu-item">
        <FaDesktop />
        <span>Agents</span>
      </NavLink>

      <button
        className="menu-item logout-btn"
        onClick={logout}
      >
        <FaSignOutAlt />
        <span>Logout</span>
      </button>

    </aside>

  );

}

export default Sidebar;