
function initialize() {
  
  var mapProp = {
    	center:new google.maps.LatLng(document.getElementById("lat_long")),
    	zoom:5,
    	mapTypeId:google.maps.MapTypeId.ROADMAP
  				};
  var map=new google.maps.Map(document.getElementById("googleMap"), mapProp);
			}
	google.maps.event.addDomListener(window, 'load', initialize);