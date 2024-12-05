$(document).ready(function () {
    $(".delBtn").each(function(){
        $(this).unbind( "click" );
        $(this).on('click', function(event){
            event.preventDefault()
            var prog_code = $(this).attr('data-id');
            var form = $(this).closest('form');
            $.confirm({
                title: 'Are you certain?',
                content: 'Program with Program Code: ' + prog_code + ' will be permanently deleted!' ,
                buttons: {
                    yes: {
                        text: "Yes",
                        action: function(){
                            $.alert({
                                title: "Sucess",
                                content: "Program with Program Code: " + prog_code + " is sucessfully deleted!",
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