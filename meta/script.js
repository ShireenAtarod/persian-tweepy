var keys = Object.keys(meta[0]);
var table = document.getElementById("tableContainer");

// creating header
var headerRow = table.insertRow();
for (var i = 0; i <= keys.length; i++) {
  var cell = headerRow.insertCell(i);
  if (i > 0) {
    cell.innerHTML = keys[i - 1];
  } else {
    cell.innerHTML = 'WEEK NO.';
  }
}

for (var i = 0; i < meta.length; i++) {
  var rowData = meta[i];
  var row = table.insertRow();
  for (var j = 0; j <= keys.length; j++) {
    var cell = row.insertCell(j);
    if (j > 0) {
      var cellData = rowData[keys[j - 1]];

      var cellList = document.createElement('ul');
      var cellDataKeys = Object.keys(cellData);

      for (var k = 0; k < cellDataKeys.length; k++) {
        var cellListItem = document.createElement('li');
        cellListItem.innerHTML = (cellDataKeys[k] + ': ' + cellData[cellDataKeys[k]]);
        cellList.appendChild(cellListItem);
      }
      cell.appendChild(cellList);
    } else {
      cell.innerHTML = (i + 1);
    }
  }
}
