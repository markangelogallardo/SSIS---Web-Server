$(document).ready(function () {
    $(".delBtn").each(function(){
        $(this).unbind( "click" );
        $(this).on('click', function(event){
            event.preventDefault()
            var id = $(this).attr('data-id');
            var form = $(this).closest('form');
            $.confirm({
                title: 'Are you certain?',
                content: 'Student with ID Number: ' + id + ' will be permanently deleted!' ,
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
    
       
    });        
        
        
}); 
