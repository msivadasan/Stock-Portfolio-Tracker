//Daily trigger (after trading hours) code based on David Weiss youtube tutorial:https://www.youtube.com/watch?v=5BYhGGPQlyA 
function setTrigger() {
  ScriptApp.newTrigger('importCSVFromGoogleDrive')
  .timeBased()
  .onWeekDay.atHour(21).nearMinute(30)
  .create();
}

// Code to update sheet using csv file borrowed from https://stackoverflow.com/questions/41282250/import-data-from-csv-file-in-google-drive-to-google-sheet
function importCSVFromGoogleDrive() {
  var file = DriveApp.getFilesByName("pv.csv").next();
  var csvData = Utilities.parseCsv(file.getBlob().getDataAsString());
  var sheet = SpreadsheetApp.getActive().getSheetByName("updated")
  sheet.getRange(1, 1, csvData.length, csvData[0].length).setValues(csvData);
} 

