document.getElementById('districtform').addEventListener('submit',function(e){
  e.preventDefault();
  var districtname = document.getElementById('districtname').value.trim().toLowerCase();
  window.location.href = 'heatmap.html?district=' + districtname;
});



