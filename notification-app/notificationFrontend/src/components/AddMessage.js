import { Box } from "@mui/material";
import axios from "axios";
import React, { useState } from "react";

const AddMessage = () => {
  const [message, setMessage] = useState("");
  const [category, setCategory] = useState(1);
  const saveMessage = () => {
    if (message.length > 0) {
      axios
        .post(`${process.env.REACT_APP_API_URL}add/`, {
          message,
          category,
        })
        .then((data) => {
          alert("Message added Successfully.");
          setMessage("");
          setCategory(1);
        })
        .catch((e) => console.log(e.message));
    } else {
      alert("Message field cannot be empty.");
    }
  };
  return (
    <Box
      sx={{
        width: "50%",
        margin: "auto",
        display: "flex",
        justifyContent: "center",
        flexDirection: "column",
      }}
    >
      <Box
        sx={{
          marginTop: "20px",
          display: "flex",
          justifyContent: "start",
          marginBottom: "10px",
        }}
      >
        <label
          style={{
            marginRight: "64px",
            marginTop: "15px",
            fontSize: "13px",
            fontWeight: "bold",
          }}
          htmlFor="exampleFormControlInput1"
        >
          Message
        </label>
        <textarea
          rows="3"
          cols="60"
          className="form-control"
          id="messageInput"
          placeholder="Write your message here"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        ></textarea>
      </Box>
      <Box>
        <label
          style={{ marginRight: "20px", fontSize: "13px", fontWeight: "bold" }}
          htmlFor="exampleFormControlSelect1"
        >
          Select Category
        </label>
        <select
          onChange={(e) => e.target.value}
          value={category}
          className="form-control"
          id="categorySelection"
        >
          <option value={1}>Sports</option>
          <option value={2}>Finance</option>
          <option value={3}>Movies</option>
        </select>
      </Box>
      <Box
        sx={{ display: "flex", justifyContent: "flex-end", marginTop: "10px" }}
      >
        <button onClick={saveMessage}>Add Message</button>
      </Box>
    </Box>
  );
};

export default AddMessage;
