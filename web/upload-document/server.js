// importing express and configering dotenv
const express = require("express");
require("dotenv").config();

// importing connect function to connect server and database
const connect = require("./src/Configs/db");

// importing file upload controller
const fileController = require("./src/Controller/uploadControl");

// app for accessing express functionalities
const app = express();

// .file route to for file controller
app.use("/file", fileController);

// app.listen to start server
app.listen(process.env.PORT || 8080, async (req, res) => {
  try {
    await connect();

    console.log("===>>> Server started successfully");
  } catch (error) {
    console.log("===>>> Server starting error:", error);
  }
});
