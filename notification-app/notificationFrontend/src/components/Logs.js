import React, { useState, useEffect } from "react";
import axios from "axios";
import Navbar from "./Navbar";
import { Box } from "@mui/material";

const Logs = () => {
  const [logs, setLogs] = useState([]);
  useEffect(() => {
    axios
      .get(`${process.env.REACT_APP_API_URL}logs/string`)
      .then(({ data }) => {
        setLogs(data);
      });
  }, []);

  return (
    <>
      <Navbar />
      <Box
        sx={{ width: "80%", margin: "auto", boxShadow: "0", marginTop: "28px" }}
      >
        {logs.map(({ log }) => (
          <Box
            key={log}
            sx={{
              backgroundColor: "#d3d3d3",
              marginBottom: "10px",
              padding: "7px",
              borderRadius: "6px",
              "&:hover": {
                background: "#808080",
                color: "#ffffff",
              },
            }}
          >
            {log}
          </Box>
        ))}
      </Box>
    </>
  );
};

export default Logs;
