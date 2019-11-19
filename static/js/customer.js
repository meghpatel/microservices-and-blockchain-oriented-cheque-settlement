$(document).ready(function(){
	var dataTable = $("#dataTable").DataTable()
	var customerChannel = pusher.subscribe('customer');
	customerChannel.bind('add', function(data) {
	var date = new Date();
	dataTable.row.add([
	    data.name,
	    data.AccNo,
	    data.Amount,
	    data.IFSC,
	    `${date.getFullYear()}/${date.getMonth()}/${date.getDay()}`,
	    data.salary
	  ]).draw( false );
	});
});