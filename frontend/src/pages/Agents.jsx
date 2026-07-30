import { useEffect, useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";
import API from "../services/api";

import "../styles/agents.css";

function Agents() {

    const [agents, setAgents] = useState([]);

    function fetchAgents() {

        API.get("/agents/api/")

            .then(response => {

                setAgents(response.data.agents);

            })

            .catch(console.log);

    }

    useEffect(() => {

        fetchAgents();

        const interval = setInterval(() => {

            fetchAgents();

        }, 2000);

        return () => clearInterval(interval);

    }, []);

    return (

        <DashboardLayout>

            <h2>Connected Agents</h2>

            <p>

                Registered systems monitored by AI SIEM

            </p>

            <table>

                <thead>

                    <tr>

                        <th>Hostname</th>
                        <th>Agent ID</th>
                        <th>IP Address</th>
                        <th>Operating System</th>
                        <th>Status</th>
                        <th>Last Seen</th>

                    </tr>

                </thead>

                <tbody>

                    {

                        agents.length === 0 ?

                        (

                            <tr>

                                <td colSpan="6">

                                    No agents connected.

                                </td>

                            </tr>

                        )

                        :

                        (

                            agents.map(agent => (

                                <tr key={agent.id}>

                                    <td>{agent.hostname}</td>

                                    <td>{agent.agent_id}</td>

                                    <td>{agent.ip_address}</td>

                                    <td>{agent.operating_system}</td>

                                    <td>

                                        <span
                                            className={
                                                agent.status === "Online"
                                                    ? "online"
                                                    : "offline"
                                            }
                                        >

                                            {agent.status}

                                        </span>

                                    </td>

                                    <td>{agent.last_seen}</td>

                                </tr>

                            ))

                        )

                    }

                </tbody>

            </table>

        </DashboardLayout>

    );

}

export default Agents;