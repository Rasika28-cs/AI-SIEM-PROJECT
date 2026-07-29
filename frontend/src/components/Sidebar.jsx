import { NavLink } from "react-router-dom";
import {
  FaTachometerAlt,
  FaFileAlt,
  FaBell,
  FaDesktop,
  FaSignOutAlt,
} from "react-icons/fa";

import "../styles/sidebar.css";

function Sidebar() {
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

      <div className="logout">

        <NavLink to="/" className="menu-item">
          <FaSignOutAlt />
          <span>Logout</span>
        </NavLink>

      </div>

    </aside>
  );
}

export default Sidebar;