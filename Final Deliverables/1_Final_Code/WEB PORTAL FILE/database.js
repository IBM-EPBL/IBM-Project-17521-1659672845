
const cap_status = document.getElementById('cap_status');
const alert_msg = document.getElementById('alert_msg');

var ref = firebase.database().ref();

ref.on("value", function(snapshot) 
 {
    snapshot.forEach(function (childSnapshot) {
        var value = childSnapshot.val();
	
		const alert_msg_val = value.alert;
		const cap_status_val = value.distance_status;
		

		alert_msg.innerHTML= `${alert_msg_val}`;
    });
 }, function (error) {
    console.log("Error: " + error.code);
 });