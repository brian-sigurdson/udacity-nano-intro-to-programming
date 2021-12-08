// Variables
var colorPicker = document.getElementById('colorPicker');
var pixelCanvas = document.getElementById('pixelCanvas');
var sizePicker = document.getElementById('sizePicker');
var tableHeight = document.getElementById('inputHeight');
var tableWidth = document.getElementById('inputWidth');

// functions
function setCellColor(event) {
    // set the cell's background color
    event.target.bgColor = colorPicker.value;
}

function makeGrid(event) {
    // turn off default event behavior
    event.preventDefault();

    // remove any prior contents of the table
    pixelCanvas.innerHTML = "";
    // get the desired table height
    tableHeight = document.getElementById('inputHeight');
    // get the desired table width
    tableWidth = document.getElementById('inputWidth');

    // create the new table contents
    for (var row = 0; row < tableHeight.value; row++) {
        // create a new row
        var newRow = pixelCanvas.insertRow(row);

        // add cells to the new row
        for (var cell = 0; cell < tableWidth.value; cell++) {
            // create a new cell for the row
            var newCell = newRow.insertCell(cell);

            // add an event listener here for the cell
            newCell.addEventListener('click', setCellColor);
        }
    }

}

// listeners
// document.getElementById('sizePicker').addEventListener('click', makeGrid);
document.getElementById('sizePicker').addEventListener('submit', makeGrid);
// window.addEventListener('load', makeGrid);
// document.addEventListener('load', makeGrid);