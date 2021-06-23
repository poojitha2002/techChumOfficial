function _(selector){
  return document.querySelector(selector);
}
function setup(){
  let canvas = createCanvas(650, 600);
  canvas.parent("canvas-wrapper");
  background(255);
}
function mouseDragged(){
  let type = _("#pen-pencil").checked? "pencil":"brush";
  if(_("#pen-eraser").checked)
  type="eraser";
  let size = parseInt(_("#pen-size").value);
  let color = _("#pen-color").value;
  fill(color);
  stroke(color);
  if(type == "pencil"){
    line(pmouseX, pmouseY, mouseX, mouseY);
  }
  else if (type=="eraser")
  {
   fill('white');
    stroke('white');
   ellipse(mouseX, mouseY, size, size);
  }
  else {
    ellipse(mouseX, mouseY, size, size);
  }
}

_("#reset-canvas").addEventListener("click", function(){
  background(255);
});


