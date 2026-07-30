import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

import "../styles/layout.css";

function DashboardLayout({ children }) {
  return (
    <div className="layout">

      <Sidebar />

      <div className="main-content">

        <Navbar />

        <main className="page-content">
          {children}
        </main>

      </div>

    </div>
  );
}

export default DashboardLayout;