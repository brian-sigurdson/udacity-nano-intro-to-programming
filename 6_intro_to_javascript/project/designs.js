// Variables
var colorPicker = document.getElementById('colorPicker');
var pixelCanvas = document.getElementById('pixelCanvas');
var sizePicker = document.getElementById('sizePicker');
var tableHeight = document.getElementById('inputHeight');
var tableWidth = document.getElementById('inputWidth');

// functions
function setCellColor(event) {
    console.log(event);
    event.target.bgColor = colorPicker.value;
    // console.log(event.color.bgColor);
    console.log(colorPicker.value);
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

    console.log("height = " + tableHeight.value);
    console.log("width = " + tableWidth.value);
    // console.log("pixelCanvas = " + pixelCanvas);

    // create the new table contents
    for (var row = 0; row < tableHeight.value; row++) {
        // create a new row
        var newRow = pixelCanvas.insertRow(row);

        // add cells to the new row
        for (var cell = 0; cell < tableWidth.value; cell++) {
            var newCell = newRow.insertCell(cell);
            // var hello = document.createTextNode("hello");
            // newCell.appendChild(hello);
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