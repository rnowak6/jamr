function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      window.location="https://sonic-potion-175714.appspot.com/go?lat="+pos['lat']+"&lng="+pos['lng'];
    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  }

}

$(document).ready(function(){
  $("#go_button").click(getLocation);
});
