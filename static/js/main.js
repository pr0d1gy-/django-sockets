var socket = io.connect("/notifications");

var $log = $("#log");
var $input = $("#input-echo");

socket.on('msg', function (msg) {
	console.log(msg);
    $log.append($("<p>" + msg + "</p>"));
});

socket.on('connect', function(d){
	console.info('Connected: ' + d);
});

$("#form-echo").on("submit", function(event){
    event.preventDefault();
    var msg = $input.val();
    $input.val("");
    console.log(socket.emit("msg", msg));
});