import { useEffect, useState } from "react";
import DashboardLayout from "../layouts/DashboardLayout";
import API from "../services/api";
import "../styles/logs.css";

function Logs() {

    const [data, setData] = useState(null);

    const [search, setSearch] = useState("");
    const [severity, setSeverity] = useState("");
    const [eventType, setEventType] = useState("");
    const [agent, setAgent] = useState("");
    const [time, setTime] = useState("");
    const [page, setPage] = useState(1);

    function fetchLogs() {

        API.get("/logs/api/", {

            params: {
                search,
                severity,
                event_type: eventType,
                agent,
                time,
                page,
            }

        })

        .then((response) => {

            setData(response.data);

        })

        .catch((error) => {

            console.log(error);

        });

    }

   useEffect(() => {

        fetchLogs();

        const interval = setInterval(() => {

            fetchLogs();

        }, 5000);

        return () => clearInterval(interval);

    }, [search, severity, eventType, agent, time, page]);



    if (!data) {

        return (

            <DashboardLayout>

                <h2>Loading Logs...</h2>

            </DashboardLayout>

        );

    }


    return (

        <DashboardLayout>

            <h2>Security Logs</h2>

            <div className="filter-bar">

                <input
                    type="text"
                    placeholder="Search..."
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
                    <option value="">All Severities</option>
                    <option value="LOW">LOW</option>
                    <option value="MEDIUM">MEDIUM</option>
                    <option value="HIGH">HIGH</option>
                </select>


                <select
                    value={eventType}
                    onChange={(e) => {
                        setEventType(e.target.value);
                        setPage(1);
                    }}
                >

                    <option value="">All Events</option>

                    {data.event_types.map(event => (

                        <option
                            key={event}
                            value={event}
                        >
                            {event}
                        </option>

                    ))}

                </select>


                <select
                    value={agent}
                    onChange={(e) => {
                        setAgent(e.target.value);
                        setPage(1);
                    }}
                >

                    <option value="">All Agents</option>

                    {data.agents.map(a => (

                        <option
                            key={a.id}
                            value={a.id}
                        >
                            {a.hostname}
                        </option>

                    ))}

                </select>


                <select
                    value={time}
                    onChange={(e) => {
                        setTime(e.target.value);
                        setPage(1);
                    }}
                >
                    <option value="">All Time</option>
                    <option value="today">Today</option>
                    <option value="24h">Last 24 Hours</option>
                    <option value="7d">Last 7 Days</option>
                    <option value="30d">Last 30 Days</option>
                </select>

            </div>


            <table>

                <thead>

                    <tr>

                        <th>Time</th>
                        <th>Agent</th>
                        <th>Event</th>
                        <th>Severity</th>
                        <th>Source</th>
                        <th>Message</th>

                    </tr>

                </thead>

                <tbody>

                    {data.logs.length === 0 ? (

                        <tr>

                            <td colSpan="6">
                                No logs available.
                            </td>

                        </tr>

                    ) : (

                        data.logs.map((log, index) => (

                            <tr key={index}>

                                <td>{log.timestamp}</td>
                                <td>{log.agent__hostname}</td>
                                <td>{log.event_type}</td>
                                <td>{log.severity}</td>
                                <td>{log.source}</td>
                                <td>{log.message}</td>

                            </tr>

                        ))

                    )}

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

export default Logs;