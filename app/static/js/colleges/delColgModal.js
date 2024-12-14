$(document).ready(function () {
    $(".delBtn").each(function(){
        $(this).unbind( "click" );
        $(this).on('click', function(event){
            event.preventDefault()
            var colg_code = $(this).attr('data-id');
            var form = $(this).closest('form');
            $.confirm({
                title: 'Are you certain?',
                content: 'College with College Code: ' + colg_code + ' will be permanently deleted!' ,
                buttons: {
                    yes: {
                        text: "Yes",
                        action: function(){
                            $.alert({
                                title: "Sucess",
                                content: "College with College Code: " + colg_code + " is sucessfully deleted!",
                                buttons:{
                                    ok:{
                                        action: function(){
                                            console.log("Yo here")
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