$(document).ready(function(){
  $("#search").on("keyup", function() {
    var field = $("#prog_fields").val()
    var value = $(this).val().toLowerCase();
    $("#details tr").each(function() {
      let matchColumn = true;
      if (value !== "") {
          let columnData = $(this).find("td:nth-child(" +
              (field === "College Code" ? 1 :
                  (field === "College Name" ? 2 : 3)) +
              ")").text().toLowerCase();
          matchColumn = columnData.indexOf(value) > -1;
      }

      $(this).toggle(matchColumn);
          //$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    })
  });
  
    
});



  