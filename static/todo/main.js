$(function() {

    // Submit post on submit
    $('#search_name').on('change', function(event){
        console.log("form submitted!")  // sanity check
        showCPList();
    });
	
	$('#search_plant').on('change', function(event){
        showCPList();
    });

    // AJAX for posting
    function showCPList() {
        $.ajax({
			dataType: "json",
            url : "results?name=".concat($('#search_name').val(), "&plant=", $('#search_plant').val()), // the endpoint
            type : "GET", // http method
            // handle a successful response
            success : function(json) {
                console.log("success"); // another sanity check
				var items = [];
				$.each(json, function(i, item) {
					items.push("<tr><td>" + item.pseid + "</td><td>" + item.name + "</td><td>" + item.value + "</td><td>" + item.plant + "</td></tr>");
				});
				$("#cp_list").empty().append("<table style=\"width:100%\">" + items.join("") + "</table>");
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log("not successful"); // provide a bit more info about the error to the console
            }
        });

    };
	
});