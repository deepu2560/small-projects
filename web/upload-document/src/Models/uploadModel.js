// importing required liberaries
const mongoose = require("mongoose");

// file upload schema in this only file is required
const fileSchema = new mongoose.Schema(
  {
    file: { type: String, require: true },
  },
  {
    versionKey: false,
    timestamps: true,
  },
);

// exporting file upload model
module.exports = mongoose.model("files", fileSchema);
