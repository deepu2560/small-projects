// importing required liberaries
const express = require("express");

// importing model and multer middleware
const FilesModel = require("../Models/uploadModel");
const { upload, uploadSingle } = require("../Middleware/fileUpload");

// router to creating all routes
const router = express.Router();

// uploading file to upload folder and storing path as a string in database
router.post("/upload", uploadSingle("file"), async (req, res) => {
  try {
    let files = await FilesModel.create({ file: req.file.path });

    console.log("==> Uploading file to upload folder");
    res
      .status(200)
      .send({ error: false, files, message: "Uploaded file successfully" });
  } catch (error) {
    console.log("==>> Uploading file Server error :", error);
    res.status(502).send({
      error: true,
      message: `upload file server errror: ${error.message}`,
    });
  }
});

router.get("/get", async (req, res) => {
  try {
    let files = await FilesModel.find().lean().exec();

    console.log("==> Showing all files");
    res.status(200).send({ error: false, files, message: "Showing all files" });
  } catch (error) {
    console.log("==>> Uploading file Server error :", error);
    res.status(502).send({
      error: true,
      message: `upload file server errror: ${error.message}`,
    });
  }
});

// exporting router
module.exports = router;
