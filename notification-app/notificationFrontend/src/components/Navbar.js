import { Box } from "@mui/material";
import React from "react";
import { Link } from "react-router-dom";
const Navbar = () => {
  return (
    <nav>
      <Box
        sx={{
          justifyContent: "center",
          alignItems: "center",
          display: "flex",
          marginBottom: "10px",
          flexDirection: "row",
          backgroundColor: "#494F55",
          color: "#fffff",
        }}
      >
        <Box
          sx={{
            padding: "10px",
            display: "flex",
            flexDirection: "row",
            justifyContent: "space-between",
            textDecoration: "none",
          }}
        >
          <Box
            sx={{
              margin: "6px",
              "&:hover": {
                textDecoration: "underline",
              },
            }}
          >
            <Link
              style={{
                color: "white",
                textDecoration: "none",
              }}
              to={"/"}
            >
              Home
            </Link>
          </Box>
          <Box
            sx={{
              margin: "6px",
              "&:hover": {
                textDecoration: "underline",
              },
            }}
          >
            <Link
              style={{ color: "white", textDecoration: "none" }}
              to={"/logs"}
            >
              Logs
            </Link>
          </Box>
        </Box>
      </Box>
    </nav>
  );
};

export default Navbar;
