$(document).ready(function(){
    $("#studentSearch").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#studDeats tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });

  