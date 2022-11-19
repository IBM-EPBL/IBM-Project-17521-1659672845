const database = firebase.database();

function myMap() 
{
	var ref1 = firebase.database().ref();
	
		ref1.on("value", function(snapshot) 
		 {
		    snapshot.forEach(function (childSnapshot) {
		        var value = childSnapshot.val();
				const latitude = value.latitude;
				const longitude = value.longitude;

				var latlong = { lat: latitude, lng: longitude}
				var mapProp =
				{
					center: new google.maps.LatLng(latlong),
					zoom: 10,
				};
				var map = new google.maps.Map(document.getElementById("map"), mapProp);
			
				var marker = new google.maps.Marker({ position: latlong });
				marker.setMap(map);
		    });
		 }, function (error) {
		    console.log("Error: " + error.code);
		 });
	
}
