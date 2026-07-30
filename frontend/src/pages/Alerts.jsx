import { useEffect, useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";
import API from "../services/api";
import { Link } from "react-router-dom";

import "../styles/alerts.css";

function Alerts() {

  const [data, setData] = useState(null);

  const [search, setSearch] = useState("");
  const [severity, setSeverity] = useState("");
  const [status, setStatus] = useState("");

  const [page, setPage] = useState(1);

  function fetchAlerts() {

    API.get("/alerts/api/", {

      params: {

        search,
        severity,
        status,
        page

      }

    })

      .then(response => {

        setData(response.data);

      })

      .catch(console.log);

  }

  useEffect(() => {

    fetchAlerts();

    const interval = setInterval(() => {

      fetchAlerts();

    }, 5000);

    return () => clearInterval(interval);

  }, [search, severity, status, page]);



  if (!data) {

    return (

      <DashboardLayout>

        <h2>Loading Alerts...</h2>

      </DashboardLayout>

    );

  }



  return (

    <DashboardLayout>

      <h2>Alert Management</h2>

      <div className="alert-filters">

        <input

          type="text"

          placeholder="Search Attack"

          value={search}

          onChange={(e) => {

            setSearch(e.target.value);

            setPage(1);

          }}

        />



        <select

          value={severity}

          onChange={(e) => {

            setSeverity(e.target.value);

            setPage(1);

          }}

        >

          <option value="">All Severity</option>
          <option value="HIGH">HIGH</option>
          <option value="MEDIUM">MEDIUM</option>
          <option value="LOW">LOW</option>

        </select>



        <select

          value={status}

          onChange={(e) => {

            setStatus(e.target.value);

            setPage(1);

          }}

        >

          <option value="">All Status</option>
          <option value="Open">Open</option>
          <option value="Investigating">Investigating</option>
          <option value="Resolved">Resolved</option>

        </select>

      </div>


      <table>

        <thead>

          <tr>

            <th>Time</th>
            <th>Attack</th>
            <th>Severity</th>
            <th>Agent</th>
            <th>Status</th>

          </tr>

        </thead>

        <tbody>

          {

            data.alerts.map(alert => (

              <tr key={alert.id}>

                <td>{alert.created_time}</td>

                <td>

                  <Link to={`/alerts/${alert.id}`}>

                    {alert.attack_type}

                  </Link>

                </td>

                <td>{alert.severity}</td>

                <td>{alert.log__agent__hostname}</td>

                <td>{alert.status}</td>

              </tr>

            ))

          }

        </tbody>

      </table>


      <div className="pagination">

        <button

          disabled={!data.pagination.has_previous}

          onClick={() => setPage(1)}

        >

          First

        </button>


        <button

          disabled={!data.pagination.has_previous}

          onClick={() => setPage(data.pagination.previous_page)}

        >

          Previous

        </button>


        <span>

          Page {data.pagination.page} of {data.pagination.pages}

        </span>


        <button

          disabled={!data.pagination.has_next}

          onClick={() => setPage(data.pagination.next_page)}

        >

          Next

        </button>


        <button

          disabled={!data.pagination.has_next}

          onClick={() => setPage(data.pagination.pages)}

        >

          Last

        </button>

      </div>

    </DashboardLayout>

  );

}

export default Alerts;