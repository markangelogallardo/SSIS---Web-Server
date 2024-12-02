$(document).ready(function(){
    $("#studentSearch").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      console.log(value)
      $("#studDeats tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });



  