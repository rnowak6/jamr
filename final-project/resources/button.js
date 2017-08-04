function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      window.location="/go?lat="+pos['lat']+"&lng="+pos['lng'];
    }, function() {
    });
  }

}

$(document).ready(function(){
  $("#go_button").click(getLocation);
});
