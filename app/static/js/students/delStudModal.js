$(document).ready(function () {
    $(".delBtn").each(function(){
        $(this).unbind( "click" );
        $(this).on('click', function(event){
            console.log("Called")
            event.preventDefault()
            var id = $(this).attr('data-id');
            var form = $(this).closest('form');
            $.confirm({
                title: 'Are you certain?',
                content: 'Student with ID Number:' + id + ' will be permanently deleted!' ,
                buttons: {
                    yes: {
                        text: "Yes",
                        action: function(){
                            $.alert({
                                title: "Sucess",
                                content: "Student with ID Number: " + id +" is sucessfully deleted!",
                                buttons:{
                                    ok:{
                                        action: function(){
                                            form.submit();
                                        }
                                    }
                                }
                            });
                        }
                        
                    },
                    no: function () {
                        $.alert('No delete happened!');
                    }
                }
        });
    })
    
        //console.log(id)
        /*if(confirm("Are your sure?") == true) {
            $.ajaxSetup({
                headers: {
                    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                }
            });
            
            $.ajax({url: url,
                method: 'GET',
                data:{id: id},
                success: function(){
                    console.log(id);
                    if(result.success) {
                        console.log("Success")
                        form.submit()
                        alert("success");
                        location.reload()
                    } else {
                        console.log("Failure")
                        alert("failure");
                        location.reload()
                    } 
                }});
        }
        else{
            alert("No delete happened");
        }*/
    });        
        
        
}); 
