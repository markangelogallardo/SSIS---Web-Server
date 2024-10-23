$(document).ready(function () {
    $('#addModal').on('show.bs.modal',
        function (event) {
            $(this).data('bs.modal').
                _config.backdrop = 'static';

            $(this).data('bs.modal').
                _config.keyboard = false;
        });
});

$(document).ready(function() {
    $("#add-student").click(function(event) {
        event.preventDefault()
        $.ajax({
            url: "/student/add",
            method: "POST",
            headers: {
                'X-CSRFToken': $("input[name='csrf_token']").val()  // Include CSRF token in headers
            },
            success: function(response) {
                console.log('Response', response)
                if(!response.success){
                    $('#errorMessage').text("u fucked").show();
                    console.log(response.message);  // Log message in console
                } else {
                    console.log("wassup")
                }
            },
            error: function(xhr) {
                console.log(xhr.responseText)
            }
        });
        
    });
});



        
